import pytest
import urllib3
from flask import Flask, render_template, request
import os
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

db.create_all()

#testing for url routes
def test_homepage():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.148.36:5000/')
    assert 200 == r.status

def test_insert():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.148.36:5000/insert/')
    assert 404 == r.status

def test_update():
    http = urllib3.PoolManager()
    r = http.request('POST', 'http://35.242.148.36:5000/update/')
    assert 404 == r.status

def test_action_delete():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.242.148.36:5000/action/delete/')
    assert 404 == r.status
