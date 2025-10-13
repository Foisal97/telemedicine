import { Alert } from "@mui/material"

interface AlertMessageProps{
    message: string;
    severity?: "error" | "success" | "info" | "warning"
}

export default function AlertMessage({message, severity = "info"}: AlertMessageProps){
    if (!message) return null;
    return <Alert security={severity} sx={{mt:2}}>{message}</Alert>
}