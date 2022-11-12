from urllib import request
from project import Project
import tomli



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_dict = tomli.loads(content)
        data = toml_dict["tool"]["poetry"]
        name = data["name"]
        description = data["description"]
        dependencies = list(data["dependencies"].keys())
        d_dependencies = list(data["dev-dependencies"].keys())

  
    
	# deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, d_dependencies)
