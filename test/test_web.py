# import pytest
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options


# @pytest.fixture
# def browser():
#     opts = Options()
#     opts.headless = True
	
#     # driver = Chrome(options=opts, executable_path='/home/percy/.local/lib/python3.6/site-packages/chromedriver.exe')
#     location='chromedriver'
#     driver = Chrome(options=opts, executable_path=location)
#     driver.implicitly_wait(5)

#     yield driver

#     # For cleanup, quit the driver
#     driver.quit()


# def test_get_title(browser):
#     driver.get("http://35.242.148.36:5000/")

#     assert 'My html page' == browser.title


