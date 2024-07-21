import { Button } from "@mui/material";

type ActivationSquareProps = {
    value: number
}

const dark = '#444444';
const light = 'gray';
const none = 'white';
export const ActivationSquare = ({ 
    value,
}: ActivationSquareProps) => {
    const logValue = isNaN(Number(value)) ? -100 : Math.round(Math.log2(value));
    const color = 
        logValue > -5 ? dark
        : logValue > -10 ? light
        : none;

    return (
        <Button
            variant='contained'
            sx={{ height: 80, width: 80, fontSize: '2em', backgroundColor: color}}
        >
            <text style={{ color: color === none ? 'black' : 'white' }}>
                {logValue}
            </text>
        </Button>
    )
}