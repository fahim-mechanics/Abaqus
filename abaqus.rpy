# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-14.55.25 RELr426 190762
# Run by yehan on Thu Jun  4 03:10:30 2026
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=118.429168701172, 
    height=133.849075317383)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('Model-Hole.cae')
#: The model database "C:\Users\yehan\Desktop\Y E H A N\Mechanics of Sustainable Materials and Structures\Academic\Semester 2\Modeling and simulation of structures with Laboratory\Plate Theory\Project\Project 3\Homework 3\Abaqus files\Thick Plate  with Hole Analysis\Model-Hole.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Hole_Thick_HT_Course'].parts['Plate']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
