import { useState } from 'react';
import Button from '@mui/material/Button';


type SquareState = '' | 'X' | 'O';

type SquareProps = {
    value: SquareState,
    updateGrid: () => void,
}

export const Square = ({ 
    value,
    updateGrid
}: SquareProps) => {
    return (
        <Button 
            variant="outlined"
            onClick={updateGrid}
            disabled={value != ''}
            sx={{ height: 80, width: 80 }}
        >
            {value}
        </Button>
    )
}

export const TicTacToe = () => {
    const [gridState, setGridState] = useState(Array(9).fill(''))

    // true - X. false - O.
    const [turn, setTurn] = useState(true);
    const [response, setResponse] = useState(['-']);

    const opponentTurn = async (grid: number[], turn: boolean) => {
        console.log(JSON.stringify({
            size: 3,
            board_state: grid,
          }));
        await fetch("http://localhost:8000/items", {
            method: "POST",
            body: JSON.stringify({
              size: 3,
              board_state: grid,
            }),
            headers: {
              "Access-Control-Allow-Origin": "*",
              "Content-type": "application/json",
            }
        })
        .then((response) => {
            console.log(response);
            return response.json();
        })
        .then((json) => {
            setResponse(json.toPlay);
        });
    }

    const humanTurn = (position: number) => {
        return () => {
            const tmp = gridState;
            tmp[position] = turn ? 'X' : 'O';
            setGridState([...tmp]);
            // prevent race condition on turn
            opponentTurn(tmp, turn);
        };
    };
    
    return (
        <>
            <h1>teec tac toe</h1>
            <h2>Turn: {turn ? 'X' : 'O'}</h2>
            <h2>Computer says: Play at {response}</h2>
            {[...Array(3).keys()].map(row => {
                return (
                    <div key={row}>
                        {[...Array(3).keys()].map(col => {
                            const cellPosition = 3 * row + col;

                            return (
                                <Square
                                    key={cellPosition}
                                    value={gridState[cellPosition]}
                                    updateGrid={humanTurn(cellPosition)}
                                />
                            );
                        })}
                    </div>
                )
            })}
        </>
    )
}