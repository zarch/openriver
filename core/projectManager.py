import geometry as geom
import os as os

class Project:
    """            This class represents the project object
    """
    def __init__(self, name=None, simList=None,dependencyFilename=None):
        self.projectName = name
        self.simList = simList
        self.dependencyFilename= dependencyFilename
        self.projectPath
    
    def createProject(self,name,path):
        """ Creates a project ...
        """
        # Setting project name        
        self.projectName = name
        # Setting path to project
        self.projectPath = path+"/"+name
        # Creating project folder
        os.mkdir(self.projectPath)
        # Default creation of first simulation
        Simulation.createSimulation("sim0")
        # Initializes a simulations list
        self.simList = []
        # Creation of file for simulations' dependecy follow-up
        self.dependencyFilename = dependencyManager
        dePManFile = open(self.projectPath+"/depManFile","w")
              
class Simulation:
    """            This class represents the simulation object
    """
    def __init__(self, name=None):
        self.simName = name
        self.simPath = None
        self.geometryPath = None
        self.icsPath = None
        self.bcsPath = None
        self.paramPath = None
        self.resultsPath = None
    def createSimulation(self,name,parent=None):
        """ Creates a simulation 
        """
        # Define simulation name
        self.simName = str(name)
        # Define simulation path and create simulation directory
        self.simPath = Project.projectPath+"/"+self.simName
        os.mkdir(self.simPath)
        # Append simulation to project's simulation list
        Project.simList.append(self.simName)
        # Define geometry path and create simulation directory
        self.geometryPath = self.simPath+"/"+"geometry"
        os.mkdir(self.geometryPath)
        # Define Initial Conditions path and create simulation directory
        self.icsPath = self.simPath+"/"+"ics"
        os.mkdir(self.icsPath)
        # Define Boundary Conditions path and create simulation directory
        self.bcsPath = self.simPath+"/"+"bcs"
        os.mkdir(self.bcsPath)
        # Define Model Parameters path and create simulation directory
        self.paramPath = self.simPath+"/"+"param"
        os.mkdir(self.paramPath)
        # Define Simulation's Results path and create simulation directory
        self.resultsPath = self.simPath+"/"+"results"
        os.mkdir(self.resultsPath)
               
        # TODO incorporate subversions tracking....
            
        

        
        
    
        
        
    
        
