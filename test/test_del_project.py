from model.project import Project
import random


def test_delete_some_project(app, config):
    username=config['webadmin']['username']
    password=config['webadmin']['password']
    if len(app.soap.get_project_list(username, password)) == 0:
        app.project.add_project(Project(name="for deletion"))
    old_list = app.soap.get_project_list(username, password)
    project = random.choice(old_list)
    app.project.delete_project_by_id(project.id)
    new_list = app.soap.get_project_list(username, password)
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project)
    assert sorted(new_list, key=Project.id_or_max) == sorted(old_list, key=Project.id_or_max)