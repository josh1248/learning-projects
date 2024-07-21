import { useEffect, useMemo, useState } from 'react';
import { GridSquare } from './components/GridSquare';
import { GridCell } from './components/GridTypes';
import { ActivationSquare } from './components/ActivationSquare';




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

    const [player, setPlayer] = useState(true);
    const [agent, setAgent] = useState(true);

    const [turn, setTurn] = useState(0);
    const [victoryFeedback, setVictoryFeedback] = useState('');
    const [loading, setLoading] = useState(false);
    const [activations, setActivations] = useState(Array(9).fill('-'));

    useEffect(() => {
        if (turn === 0 && !player) {
            opponentTurn([initialGrid.slice().map(cell => ({...cell} as GridCell))]);
        }
    }, [turn, player]);

    const clearStates = useMemo(() => {
        return () => {
            setVictoryFeedback('');
            setTurn(0);
            setLoading(false);
            setActivations(Array(9).fill('-'));
        }
    }, []);

    const opponentTurn = async (grid: GridCell[][]) => {
        setLoading(true);
        await fetch("http://localhost:8000/items", {
            method: "POST",
            body: JSON.stringify({
              agent: agent,
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
                setActivations(json.activations[0]);

                grid[grid.length - 1][cellChosen].value = player ? 'O' : 'X';
                grid[grid.length - 1][cellChosen].color = 'gray';
                var won = ColorVictoryIfAny(grid[grid.length - 1]);
                if (won) { 
                    setVictoryFeedback('AI too stronk');
                    return
                }
                setGridStates([...grid]);
                setTurn(turn => turn + 1);
                setLoading(false);
            }, 1200);
        });
    }

    const humanTurn = (position: number) => {
        return () => {
            setLoading(true);
            var tmp = gridStates[gridStates.length - 1].slice().map(cell => ({...cell} as GridCell));
            tmp[position].value = player ? 'X' : 'O';
            tmp[position].color = 'gray';
            
            
            const newGrid = [...gridStates, tmp];
            setGridStates(newGrid);
            var won = ColorVictoryIfAny(tmp);
            if (won) {
                setVictoryFeedback('You won!');
                return;
            }
            if (tmp.reduce((prev, curr) => (prev + (curr.value === '' ? 0 : 1)), 0) === 9) {
                setVictoryFeedback('Draw.');
                return;
            }
            setTurn(turn => turn + 1);
            opponentTurn(newGrid);
        };
    };
    
    return (
        <>
            <h1>teec tac toe</h1>
            Play as: <br/>
            <button 
                style={{borderColor: 'black', backgroundColor: player ? 'yellow' : 'white'}}
                disabled={loading || player}
                onClick={() => {
                    setGridStates([initialGrid]);
                    setPlayer(true);
                    clearStates();
                }}
            >
                X
            </button>
            <button 
                style={{borderColor: 'black', backgroundColor: player ? 'white' : 'yellow'}}
                disabled={loading || !player}
                onClick={() => {
                    setGridStates([initialGrid]);
                    setPlayer(false);
                    clearStates();
                }}
            >
                O
            </button>
            <br />
            Use agent: <br />
            <button 
                style={{borderColor: 'black', backgroundColor: agent ? 'yellow' : 'white'}}
                disabled={loading || agent}
                onClick={() => {
                    setGridStates([initialGrid]);
                    setAgent(true);
                    clearStates();
                }}
            >
                Tensorflow (Machine learning)
            </button>
            <button 
                style={{borderColor: 'black', backgroundColor: agent ? 'white' : 'yellow'}}
                disabled={loading || !agent}
                onClick={() => {
                    setGridStates([initialGrid]);
                    setAgent(false);
                    clearStates();
                }}
            >
                Minimax (Board values)
            </button>
            {victoryFeedback !== '' && <h2>{victoryFeedback}</h2>}
            {victoryFeedback === '' && <h2>Turn: {turn % 2 === 0 ? 'X ' : 'O '} {(turn % 2 == (player ? 0 : 1)) ? '(Your turn)' : '(AI is "thinking"...)'}</h2>}
            <button 
                style={{borderColor: 'black'}}
                disabled={gridStates.length === 1}
                onClick={() => {
                    setGridStates(grid => grid.slice(0, grid.length - 1).map(cell => ({...cell})));
                    setPlayer(false);
                    clearStates();
                }}
            >
                Undo
            </button>
            <button 
                style={{borderColor: 'black'}}
                onClick={() => {
                    setGridStates([initialGrid]);
                    clearStates();
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
                                <GridSquare
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
            <div>
                <h3>
                    AI Activation: (The less negative the score, the more the AI wishes to place the item there.)
                </h3>
            {[...Array(3).keys()].map(row => {
            return (
                <div key={row}>
                    {[...Array(3).keys()].map(col => {
                        const cellPosition = 3 * row + col;
                        return (
                            <ActivationSquare
                                key={cellPosition}
                                value={activations[cellPosition]}
                            />
                        );
                    })}
                </div>
            )
            })}
            </div>
        </>
    )
}