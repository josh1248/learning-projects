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

    const registerTurn = (position: number) => {
        return () => {
            const tmp = gridState;
            tmp[position] = turn ? 'X' : 'O';
            setGridState([...tmp]);
            setTurn(turn => !turn);
        };
    }
    
    return (
        <>
            <h1>teec tac toe</h1>
            {[...Array(3).keys()].map(row => {
                return (
                    <div>
                        {[...Array(3).keys()].map(col => {
                            const cellPosition = 3 * row + col;

                            return (
                                <Square 
                                    value={gridState[cellPosition]}
                                    updateGrid={registerTurn(cellPosition)}
                                />
                            );
                        })}
                    </div>
                )
            })}
        </>
    )
}