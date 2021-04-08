from model.project import Project


def test_add_project(app, db, json_projects):
    project = json_projects
    old_projects = app.soap.get_project_list(username=app.config["webadmin"]["username"], password=app.config["webadmin"]["password"])
    app.project.create_project(project)
    old_projects.append(project)
    new_project = app.soap.get_project_list(username=app.config["webadmin"]["username"], password=app.config["webadmin"]["password"])
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)