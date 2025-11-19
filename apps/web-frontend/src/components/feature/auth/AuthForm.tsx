import { useState, useCallback } from "react";
import InputField from "../../common/InputField";
import AlertMessage from "../../common/AlertMessage";
import { login, signup } from "../../../services/auth";
import Button from "../../common/Button";

interface AuthFormProps {
  mode: "login" | "signup";
}

const AuthForm: React.FC<AuthFormProps> = ({ mode }) => {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [message, setMessage] = useState<string>("");

  const handleSubmit = useCallback(
    async (e: React.FormEvent<HTMLFormElement>) => {
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
    },
    [email, password, mode]
  );

  return (
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
};

export default AuthForm;
