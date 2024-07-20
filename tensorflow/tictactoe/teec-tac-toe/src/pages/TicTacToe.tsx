import { useState } from 'react';
import Button from '@mui/material/Button';


type SquareState = '' | 'X' | 'O';

type GridCell = {
    value: SquareState,
    color: string,
}

type SquareProps = {
    gridCell: GridCell,
    toDisable: boolean,
    updateGrid: () => void,
}

export const Square = ({ 
    gridCell,
    toDisable,
    updateGrid
}: SquareProps) => {
    return (
        <Button 
            variant="outlined"
            onClick={updateGrid}
            disabled={gridCell.value != '' || toDisable}
            sx={{ height: 80, width: 80, fontSize: '2em', backgroundColor: gridCell.color }}
        >
            {gridCell.value}
        </Button>
    )
}



const winningLineups = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
];
/** color grid if victory, returning true. Else, do not touch the grid and return false. */ 
const ColorVictoryIfAny = (
    grid: GridCell[]
): boolean => {
    var flag = false;
    winningLineups.forEach(lineup => {
        if (
            grid[lineup[0]].value === grid[lineup[1]].value &&
            grid[lineup[1]].value === grid[lineup[2]].value
        ) {
            if (grid[lineup[0]].value === 'X') {
                lineup.forEach(num => grid[num].color = 'green');
                flag = true;
            } else if (grid[lineup[0]].value === 'O') {
                lineup.forEach(num => grid[num].color = 'red');
                flag = true;
            }
        }
    });
    return flag;
}

const initialGrid = Array(9).fill(0).map(_ => ({value: '', color: 'white'} as GridCell));

export const TicTacToe = () => {
    const [gridStates, setGridStates] = useState([initialGrid]);

    // true - X. false - O.
    const [turn, setTurn] = useState(true);
    const [victoryFeedback, setVictoryFeedback] = useState('');
    const [loading, setLoading] = useState(false);

    const opponentTurn = async (grid: GridCell[][]) => {
        await fetch("http://localhost:8000/items", {
            method: "POST",
            body: JSON.stringify({
              size: 3,
              board_state: grid[grid.length - 1].map(cell => cell.value === 'X' ? 1 : cell.value === 'O' ? -1 : 0),
            }),
            headers: {
              "Access-Control-Allow-Origin": "*",
              "Content-type": "application/json",
            }
        })
        .then((response) => {
            return response.json();
        })
        .then((json) => {
            setTimeout(() => {
                var cellChosen: number = json.toPlay;

                grid[grid.length - 1][cellChosen].value = 'O';
                grid[grid.length - 1][cellChosen].color = 'gray';
                var won = ColorVictoryIfAny(grid[grid.length - 1]);
                if (won) { 
                    setVictoryFeedback('AI too stronk');
                    return
                }
                setGridStates([...grid]);
                setTurn(true);
                setLoading(false);
            }, 1200);
        });
    }

    const humanTurn = (position: number) => {
        return () => {
            setLoading(true);
            var tmp = gridStates[gridStates.length - 1].slice().map(cell => ({...cell} as GridCell));
            tmp[position].value = turn ? 'X' : 'O';
            tmp[position].color = 'gray';
            
            
            const newGrid = [...gridStates, tmp];
            setGridStates(newGrid);
            if (tmp.reduce((prev, curr) => (prev + (curr.value === '' ? 0 : 1)), 0) === 9) {
                setVictoryFeedback('Draw.');
                return;
            }
            var won = ColorVictoryIfAny(tmp);
            console.log(won);
            if (won) {
                setVictoryFeedback('You won!');
                return;
            }
            setTurn(false);
            opponentTurn(newGrid);
        };
    };
    
    return (
        <>
            <h1>teec tac toe</h1>
            {victoryFeedback !== '' && <h2>{victoryFeedback}</h2>}
            {victoryFeedback === '' && <h2>Turn: {turn ? 'X (Your turn)' : 'O (AI is "thinking"...)'}</h2>}
            <button 
                style={{borderColor: 'black'}}
                disabled={gridStates.length === 1}
                onClick={() => {
                    setGridStates([...gridStates.slice(0, gridStates.length - 1)]);
                    setVictoryFeedback('');
                    setTurn(true);
                    setLoading(false);
                }}
            >
                Undo
            </button>
            <button 
                style={{borderColor: 'black'}}
                onClick={() => {
                    setGridStates([initialGrid]);
                    setVictoryFeedback('');
                    setTurn(true);
                    setLoading(false);
                }}
            >
                Reset
            </button>
            {[...Array(3).keys()].map(row => {
                return (
                    <div key={row}>
                        {[...Array(3).keys()].map(col => {
                            const cellPosition = 3 * row + col;
                            return (
                                <Square
                                    key={cellPosition}
                                    toDisable={loading}
                                    gridCell={gridStates[gridStates.length - 1][cellPosition]}
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