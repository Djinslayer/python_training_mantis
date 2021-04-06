from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.get_link()
        # Нажатие создание проекта
        self.add_new_project()
        #time.sleep(20)
        self.fill_project_form(project)
        wd.find_element_by_name("submit").click()
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
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_css_selector("input.button-small").click()

    def get_link(self):
        wd = self.app.wd
        link: str = "http://localhost/mantisbt-1.2.20/manage_overview_page.php"
        wd.get(link)

    def delete(self, project):
        wd = self.app.wd
        self.get_link()
        wd.find_element_by_link_text(f"{project.name}").click()
        wd.find_element_by_css_selector("input[value = 'Delete Project']").click()
        wd.find_element_by_css_selector("input[value = 'Delete Project']").click()

    project_cache = None