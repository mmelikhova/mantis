from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project_managment import project_helper


class Application:

    def __init__(self, browser, base_url):
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
        self.base_url = base_url
        self.wd.implicitly_wait(2)

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
