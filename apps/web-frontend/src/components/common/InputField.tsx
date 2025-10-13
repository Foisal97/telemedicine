import { TextField } from "@mui/material";


interface InputFieldProps{
    label: string;
    type?: string;
    value: string;
    onChange: (val: string) => void
}

export default function InputField({ label, type = "text", value, onChange}: InputFieldProps) {
    return (
        <TextField
        fullWidth
        label={label}
        type={type}
        margin="normal"
        value={value}
        onChange={(e)=> onChange(e.target.value)}
        />
    );
}