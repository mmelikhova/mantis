from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project_managment import project_helper
from fixture.james import JamesHelper

class Application:

    def __init__(self, browser, config):

        if browser == "firefox":
            self.wd=webdriver.Firefox()
        elif browser == "chrome":
            self.wd=webdriver.Chrome()
        elif browser == "ie":
            self.wd=webdriver.Ie()
        else:
            raise ValueError("ERROR: Unrecognized browser %s" % browser)
        self.session=SessionHelper(self)
        self.project = project_helper(self)
        self.james=JamesHelper(self)
        self.config = config
        self.base_url = config["web"]["baseUrl"]



    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_page(self):
        wd=self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
