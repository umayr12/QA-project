from flask import render_template, Flask, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

#connection to mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:anime@35.234.138.37:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

#creating tables
class Genre(db.Model):
    genreid = db.Column(db.Integer, primary_key=True)
    anime_genre = db.Column(db.String(200))
    suggestion = db.Column(db.String(200))


class Anime(db.Model):
    animeid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    dubbed = db.Column(db.String(3))
    total = db.Column(db.Integer)
    watched = db.Column(db.Integer)
    genreid = db.Column(db.Integer, db.ForeignKey('genre.genreid'))

    def __init__(self, name, dubbed, total, watched, genreid):
        self.name = name
        self.dubbed = dubbed
        self.total = total
        self.watched = watched
        self.genreid = genreid

db.create_all()

#homepage route
@app.route("/")
def index():
    all_data = Anime.query.all()

    return render_template('index.html', animes= all_data)


#create route
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        dubbed = request.form['dubbed']
        total = request.form['total']
        watched = request.form['watched']
        genreid = request.form['genre']


        my_data = Anime(name, dubbed, total, watched, genreid)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))



#update route
@app.route('/update', methods = ['GET','POST'])
def update():


    if request.method == 'POST':
        my_data = Anime.query.get(request.form.get('id'))

        my_data.name = request.form['name']
        my_data.dubbed = request.form['dubbed']
        my_data.total = request.form['total']
        my_data.watched = request.form['watched']
        my_data.genreid = request.form['genre']



        db.session.commit()

        return redirect(url_for('index'))




#delete route
@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):

    Anime.query.filter(Anime.animeid == id).delete()
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0') 