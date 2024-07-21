export type SquareState = '' | 'X' | 'O';

export type GridCell = {
    value: SquareState,
    color: string,
};