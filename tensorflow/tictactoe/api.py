from fastapi import status, HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from .AI_agent import select_move
from .minimax_agent import minimax_agent

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "https://localhost:8080",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class GameGrid(BaseModel):
    size: int
    board_state: list[int]

@app.get("/")
def read_root():
    return {"Hello": "Wddd"}


@app.post("/items")
async def next_move(grid: GameGrid):
    print(grid)
    if len(grid.board_state) != 9:
        raise HTTPException(
            status_code=400,
            detail='board state must reflect tic tac toe square.'
        )
    
    print(minimax_agent(grid.board_state))
    return {'toPlay': minimax_agent(grid.board_state)[2]}