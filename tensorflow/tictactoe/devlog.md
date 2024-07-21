
## setting up your venv
- If you need to create a virtual environment because there are different python module dependencies between your projects, have a look at Python's virtual environment, or `venv`.
- 
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

## FastAPI setup
- Installation: `pip install fastapi` (Remember to do this in the virtual environment and then transfer dependencies!)
- Run the server: `fastapi dev api.py`, or the index python file with all the endpoints

## CORS
- Need CORS so that frontend and backend, which are from different ports, can talk
https://fastapi.tiangolo.com/tutorial/cors/

```Python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ...
```