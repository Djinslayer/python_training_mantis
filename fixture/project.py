import time


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        wd = self.app.wd
        self.get_link()
        self.add_new_project()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def add_new_project(self):
        wd = self.app.wd
        self.link_manage_projects()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def link_manage_projects(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def get_link(self):
        wd = self.app.wd
        link: str = "http://localhost/mantisbt-1.2.20/manage_overview_page.php"
        wd.get(link)

    def delete_project(self, project):
        wd = self.app.wd
        self.get_link()
        self.link_manage_projects()
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" % project.id).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    project_cache = None