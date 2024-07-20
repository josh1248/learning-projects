from fastapi import status, HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from .AI_agent import select_move, train_model

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

model = train_model()

@app.post("/items")
async def next_move(grid: GameGrid):
    if len(grid.board_state) != 9:
        raise HTTPException(
            status_code=400,
            detail='board state must reflect tic tac toe square.'
        )
    prediction = select_move(model, grid.board_state)
    return {'toPlay': prediction}
    