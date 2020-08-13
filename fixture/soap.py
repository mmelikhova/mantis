from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app=app

    def can_login(self, username, password):
        client = Client(self.app.soap_wsdl)
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        # получение списка проектов через soap
        client = Client(self.app.soap_wsdl)
        try:
            user_accessible = client.service.mc_projects_get_user_accessible(username, password)
            project_list = []
            for n in user_accessible:
                id = n.id
                name = n.name
                description = n.description
                project_list.append(Project(id=id, name=name, description=description))
            return list(project_list)
        except WebFault:
            return False
