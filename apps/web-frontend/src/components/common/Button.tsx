import { Button as MuiButton } from "@mui/material";

interface ButtonProps {
  text: string;
  onClick?: () => void;
  type?: "button" | "submit";
}

export default function Button({ text, onClick, type = "button" }: ButtonProps) {
  return (
    <MuiButton type={type} fullWidth variant="contained" onClick={onClick}>
      {text}
    </MuiButton>
  );
}
