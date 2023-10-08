import sys
import os
from cx_Freeze import setup, Executable

# Define the list of files you want to include (besides your script).
include_files = ["C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\wildspace.ico",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\mainwindow.py",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\bldgGen.py",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\encGen.py",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\form.ui",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\grpGen.py",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\npcGen.py",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\pwEngine.py",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\twnGen.py",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\ui_form.py",
                 "C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\worldManager.py"]

# Create an Executable object for your script.
target = Executable(
    script="C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\mainwindow.py",  # Replace with the name of your script.
    base="Win32GUI",  # Change to "Win32GUI" for a GUI application on Windows.
    icon="C:\\Users\\jammi\\Documents\\ProjectWildspace\\projWildspace\\wildspace.ico",  # Include the path to an icon file if needed.
)

# Define the modules and packages you want to include.
# Make sure to include PySide6 and its submodules.
packages = ["PySide6", "langchain"]

# Create the setup call.
setup(
    name="Project Wildspace",  # Change to your project name.
    version="0.0.1",
    description="Generative AI Worldbuilding Assistant",
    options={'build_exe': {'include_files': include_files, 'packages': packages}},
    executables=[target],
)
