import { Button } from "@mui/material";
import { GridCell } from "./GridTypes";


export type SquareProps = {
    gridCell: GridCell,
    toDisable: boolean,
    updateGrid?: () => void,
};

export const GridSquare = ({ 
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