Why not get a tutorial into machine learning implementation by having the model play Tic-Tac-Toe, a game whose AI does not need ML at all? :D

# Devlog

## Misc

- If you need to create a virtual environment because there are different python module dependencies between your projects, have a look at Python's virtual environment, or `venv`.

## setting up your venv
https://www.youtube.com/watch?v=Y21OR1OPC9A

First-time setup:
Unix: `python3 -m venv (virtual environment name)`, conventionally `env`
Windows: `py -m venv env`

Then, to activate venv:
Unix: `source env/bin/activate`
Windows: `env/Scripts/activate.bat` or `env/Scripts/activate`
(Directory name in CLI should now contain the virtual environment name)

Deactivate to go back to global python installation:
Windows: `deactivate`

Installing packages in virtual env:
- `pip install (package name)` within the virtual env

See venv packages:
- `pip list` within the virtual env

Show installed dependencies:
- `pip freeze` within the virtual env

Save dependencies for virtual environment into `requirements.txt`:
- `pip freeze > requirements.txt` within the virtual env

Install dependencies based on someone else's requirements.txt:
- `pip install -r requirements.txt`


- Virtual environment created does not need to be shared and should be quickly generated
- Virtual environment files, for good practice, should start with `.` to be hidden, and should be ignored in `.gitignore`
