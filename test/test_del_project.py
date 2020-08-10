from model.project import Project
import random


def test_delete_some_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.add_project(Project(name="for del"))
    old_list = app.project.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project_by_id(project.id)
    new_list = app.project.get_project_list()
    assert len(old_list) - 1 == len(new_list)
    old_list.remove(project)
    assert sorted(new_list, key=Project.id_or_max) == sorted(old_list, key=Project.id_or_max)