import shutil as shutil
import os as os
from os.path import join as joinpath

class Project:
    """This class represents the project object
    """
    def __init__(self, projectName=None):
        self.projectName = projectName
        self.simList = []
        self.dependencyFilename= None
        self.projectPath = None

    def createProject(self,name,path):
        """ Creates a project ...
        """
        # Setting project name
        self.projectName = name
        # Setting path to project
        self.projectPath = joinpath(path, name)
        # Creating project folder
        os.mkdir(self.projectPath)
        os.chmod(self.projectPath,0o777)
        # Default creation of first simulation
        sim0 = Simulation("sim0")
        sim0.createSimulation("sim0",self.projectPath)
        # Append simulation to project's simulation list
        self.simList.append(sim0)
        # Creation of file for simulations' dependecy follow-up
        dePManFile = open(joinpath(self.projectPath+"depManFile"),"w")
        self.dependencyFilename = "depManFile"

class Simulation:
    """            This class represents the simulation object
    """
    def __init__(self, name=None):
        self.simName = name
        self.simPath = str
        self.geometryPath = str()
        self.icsPath = str
        self.bcsPath = str
        self.paramPath = str
        self.resultsPath = str

    def createSimulation(self,name,projectPath,parent=None):
        """ Creates a simulation
        """
        # Define simulation name
        self.simName = str(name)
        # Define simulation path and create simulation directory
        self.simPath = joinpath(projectPath, self.simName)
        os.mkdir(self.simPath)
        os.chmod(self.simPath,0o777)
        # Define geometry path and create simulation directory
        self.geometryPath = joinpath(self.simPath,"geometry")
        os.mkdir(self.geometryPath)
        os.chmod(self.geometryPath,0o777)
        # Define Initial Conditions path and create simulation directory
        self.icsPath = joinpath(self.simPath,"ics")
        os.mkdir(self.icsPath)
        os.chmod(self.icsPath,0o777)
        # Define Boundary Conditions path and create simulation directory
        self.bcsPath = joinpath(self.simPath,"bcs")
        os.mkdir(self.bcsPath)
        os.chmod(self.bcsPath,0o777)
        # Define Model Parameters path and create simulation directory
        self.paramPath = joinpath(self.simPath,"param")
        os.mkdir(self.paramPath)
        os.chmod(self.paramPath,0o777)
        # Define Simulation's Results path and create simulation directory
        self.resultsPath = joinpath(self.simPath,"results")
        os.mkdir(self.resultsPath)
        os.chmod(self.resultsPath,0o777)
        # TODO incorporate subversions tracking....

    def importGeometry(self,sectionsFile,pointsFile):
        """ Importing geometry and declaring a river reach """
        # Copy geometry files into geometry folder
        sectionsName = joinpath(self.geometryPath,"sections.ori")
        pointsName = joinpath(self.geometryPath,"points.ori")
        shutil.copy(sectionsFile,self.geometryPath)
        shutil.copy(pointsFile,self.geometryPath)
        self.sectionsName = joinpath(self.geometryPath,"sections.ori")
        self.pointsName = joinpath(self.geometryPath,"points.ori")











