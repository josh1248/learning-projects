from fastapi import status, HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

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
    board_state: list[str]

@app.get("/")
def read_root():
    return {"Hello": "Wddd"}


@app.post("/items")
async def next_move(grid: GameGrid):
    print(grid)
    if len(grid.board_state) != grid.size ** 2:
        raise HTTPException(
            status_code=400,
            detail='board state must reflect tic tac toe square.'
        )
    
    return {'toPlay': 3}