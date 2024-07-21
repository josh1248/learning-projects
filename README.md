# Setup for tic tac toe (now with AI :O)
- Clone this repository, or save it as a folder.
- Install Docker Desktop at `https://www.docker.com/products/docker-desktop/`
- Turn on the Docker desktop application.
- Change your directory in the command line (Powershell / Terminal) such that you are within the `tictactoe` folder. For example, if you have installed this folder in the Desktop folder and you are the base directory in Windows, you can run `cd Desktop/learning-projects/tensorflow/tictactoe`.
- Run `docker compose up`. Please wait for the project to build and the model to be completed (which you can tell once things stop appearing in the terminal). First-time setup should take ~5 minutes, and subsequent setups should take ~30 seconds (for the model to build).
- Access `localhost:5173/` for the game.
- Run `docker compose down` to stop the game.
- Run `docker compose up --build` if you have some modifications to the files you would like to test.