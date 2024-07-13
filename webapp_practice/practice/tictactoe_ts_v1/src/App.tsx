import React from 'react';
import {useState} from "react";
import logo from './logo.svg';
import './App.css';

interface SquareProps {
  value: string | null;
  onSquareClick: () => any;
};
function Square({ value, onSquareClick }: SquareProps): JSX.Element {
  //named arguments only for HTML / CSS.
  return (
    <button
      className="square"
      onClick={onSquareClick}
    >
      {value}
    </button>
  );
}
interface BoardProps {
  turn_number: number;
  squares: Array<string>;
  onPlay: (given_squares:Array<string>) => void;
}

function Board({ turn_number, squares, onPlay }: BoardProps) {
  const player = turn_number % 2 === 0 ? "X" : "O";
  function handleClick(pos: number): void {
    if (squares[pos] || calculateWinner(squares) ) {
      //pass
    } else {
      const new_squares = squares.slice();
      /*slice creates a shallow copy - non-primitive values are shared.
         since our array only contains primitive strs, this is sufficient.
         For deep copying, another library will be needed.*/

      new_squares[pos] = player;
      onPlay(new_squares);
    }
  }
  let winner = calculateWinner(squares);
  const status = winner ? "Winner: " + winner
                 : turn_number >= 9 ? "Draw"
                 : "Next player: " + player;

  function makeRow(row: number) {
    return (
      <div className="board-row">
        {Array(3)
          .fill(3 * row)
          .map((base: number, index: number) => base + index)
          .map(pos => 
            <Square
              value={squares[pos]}
              onSquareClick={() => handleClick(pos)}
            />)
        }
      </div>
    );
  }
  return (
    <>
      <div className="status">{status}</div>
      {[0, 1, 2].map(row_num => makeRow(row_num))}
    </>
  );
}

function Game() {
  const [history, setHistory] = useState([Array(9).fill(null)]);
  const [currentMove, setCurrentMove] = useState(0);
  const currentSquares = history[currentMove];

  function handlePlay(new_squares: any) {
    setHistory([...history.slice(0, currentMove + 1), new_squares]);
    setCurrentMove(currentMove + 1);
  }

  function jumpTo(nextMove: any) {
    setCurrentMove(nextMove);
  }

  const moves = history.map((squares, move) => {
    const description = 'Go to ' + (move > 0 ? 'move #' + move : 'game start');
    //unique keys here is not strictly required, but is good coding practice.
    return (
      <li key={move}> 
        <button onClick={() => jumpTo(move)}>{description}</button>
      </li>
    );
  });

  return (
    <div className="game">
      <div className="game-board">
        <Board turn_number={currentMove} squares={currentSquares} onPlay={handlePlay}/>
      </div>
      <div className="game-info">
        <ol>{moves}</ol>
      </div>
    </div>
  );
}


function calculateWinner(squares: any): (string | null) {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}

export default Game;
