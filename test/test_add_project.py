

def test_add_project(app, db, json_projects):
    project = json_projects
    old_projects = db.get_project_list()
    app.project.create_project(project)
    project.id = db.get_project_list()[-1].id
    old_projects.append(project)
    assert old_projects == db.get_project_list()