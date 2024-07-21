from fastapi import status, HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from .AI_agent import select_move, train_model
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

class Response(BaseModel):
    agent: bool
    board_state: list[int]

@app.get("/")
def read_root():
    return {"Hello": "Wddd"}

model = train_model()
@app.post("/items")
async def next_move(res: Response):
    if len(res.board_state) != 9:
        raise HTTPException(
            status_code=400,
            detail='board state must reflect tic tac toe square.'
        )
    
    if res.agent:
        to_play, activations = select_move(model, res.board_state)
    else:
        _, _, to_play, activations = minimax_agent(res.board_state)

    return {'toPlay': to_play, 'activations': activations}