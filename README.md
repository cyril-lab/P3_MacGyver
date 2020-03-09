### MC GYVER LABYRINTH

Author : VERNHES Cyril

#### Description :

Help MacGyver get out of the labyrinth. 
He must recover three items before arriving in front of the guard,
otherwise he dies.

#### Prerequisites :

To work, the game requires the minimum versions of : 

Python 3.8 : https://www.python.org/downloads/

Pygame 1.9.6 : https://www.pygame.org/download.shtml

Pip 20.0.2 : https://pypi.org/project/pip/

Git : to download the project.

#### Start game and virtual environment : 

Download the project with Git and open the command line and go to project path :

###### Create the directory of virtualenv files named venv :
`python3 -m venv venv`

###### Activate the virtual environment
`venv\Scripts\activate.bat`

###### Install the libraries
`pip install -r requirements.txt`

or manually

 `pip install pygame`

###### Start game :
`main.py`

###### Stop virtual environment :
`deactivate`

#### Configurations :

You can change the game constants in the files named : constants.py

You can change the images of the game respecting their display size.
The name item must match with the name of the file. 
For example if the name of an item is " tube ", the name of the file must be " tube.png "

#### Controls :

Arrows of the directional pad for move the character.

Press escape for quit or enter for start game or replay.

