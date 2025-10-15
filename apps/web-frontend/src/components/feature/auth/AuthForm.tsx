import { useState } from "react";
import InputField from "../../common/InputField";
import AlertMessage from "../../common/AlertMessage";
import { login, signup } from "../../../services/auth";
import Button from "../../common/Button";

interface AuthFormProps {
    mode: "login" | "signup"
}

export default function AuthForm({mode}: AuthFormProps){
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")
    const [message, setMessage] = useState("")

    const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setMessage("");
    try {
      if (mode === "login") {
        const res = await login(email, password);
        localStorage.setItem("token", res.data.access_token);
        setMessage("Login successful!");
      } else {
        await signup(email, password);
        setMessage("Signup successful! You can now login.");
      }
    } catch (err: any) {
      setMessage(err.response?.data?.detail || "Something went wrong");
    }
}

return(
    <form onSubmit={handleSubmit}>
        <InputField label="Email" value={email} onChange={setEmail} />
        <InputField label="Password" type="password" value={password} onChange={setPassword} />
        <Button text={mode === "login" ? "Login" : "Sign Up"} type="submit" />
        <AlertMessage
        message={message}
        severity={message.toLowerCase().includes("wrong") ? "error" : "success"}
      />
        
    </form>
);
}