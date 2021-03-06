from model.project import Project
import random



def test_delete_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create_project(Project(name="Test for delete", description='Test for delete'))
    old_projects = app.soap.get_project_list(username=app.config["webadmin"]["username"], password=app.config["webadmin"]["password"])
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.soap.get_project_list(username=app.config["webadmin"]["username"], password=app.config["webadmin"]["password"])
    old_projects.remove(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

