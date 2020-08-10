from model.project import Project
from selenium.webdriver.support.ui import Select


class project_helper:

    def __init__(self, app):
        self.app = app

    def implicitly_wait(self, value):
        pass

    def open_project_create_page(self):
        wd =self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def open_project_manage_page(self):
        wd=self.app.wd
        wd.find_element_by_css_selector('td.menu:nth-child(1) > a:nth-child(7)').click()
        wd.find_element_by_css_selector('span.bracket-link:nth-child(2) > a:nth-child(1)').click()

    def input_project_data(self, project):
        wd=self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("status").click()
        Select(wd.find_element_by_name("status")).select_by_visible_text(project.status)
        wd.find_element_by_name("status").click()
        wd.find_element_by_name("view_state").click()
        Select(wd.find_element_by_name("view_state")).select_by_visible_text(project.view_state)
        wd.find_element_by_name("view_state").click()
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def submit_add_project(self):
        wd=self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def add_project(self, project):
        self.open_project_manage_page()
        self.open_project_create_page()
        self.input_project_data(project)
        self.submit_add_project()
        self.project_cache=None

    project_cache=None

    def get_project_list(self):
        wd=self.app.wd
        self.open_project_manage_page()
        self.project_cache=[]
        page_table=wd.find_elements_by_xpath("//table[@class='width100']")
        table=page_table[1]
        row=table.find_elements_by_xpath(".//tr[contains(@class, 'row')]")
        #row-1 or row-2
        del row[0] #удалить 0 строку для получения необходимой части табл
        for position in row:
            sector=position.find_elements_by_tag_name("td")
            name=sector[0].text
            description=sector[4].text
            link=wd.find_element_by_link_text(name).get_attribute("href")
            index=link.index('=') + 1
            id = link[index:] #получение идентификатора из текста ссылки /обрезка
            self.project_cache.append(Project(id=id, name=name, description=description))
        return list(self.project_cache)

    def select_project_by_id(self, id):
        wd=self.app.wd
        wd.find_element_by_xpath("//a[@href='manage_proj_edit_page.php?project_id=%s']" % id).click()

    def delete_project_by_id(self, id):
        wd=self.app.wd
        self.open_project_manage_page()
        self.select_project_by_id(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache=None
