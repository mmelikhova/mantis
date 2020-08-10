from model.project import Project
import data.project
import pytest


@pytest.mark.parametrize("project", data.project.testdata, ids=[repr(y) for y in data.project.testdata])
def test_add_project(app, project):
    old_list = app.project.get_project_list()
    app.project.add_project(project)
    new_list = app.project.get_project_list()
    assert len(old_list) + 1 == len(new_list)
    old_list.append(project)
    assert sorted(old_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)




