from model.project import Project
import data.project
import pytest


@pytest.mark.parametrize("project", data.project.testdata, ids=[repr(y) for y in data.project.testdata])
def test_add_project(app, project, config):
    username = config['webadmin']['username']
    password = config['webadmin']['password']
    old_list = app.soap.get_project_list(username, password)
    app.project.add_project(project)
    new_list = app.soap.get_project_list(username, password)
    old_list.append(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)




