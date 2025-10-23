import { useState } from "react";
import { Container, Box, Typography, Link, Tabs, Tab } from "@mui/material";
import AuthForm from "../components/feature/auth/AuthForm";
import SSOButtons from "../components/feature/auth/SSOButton";

export default function AuthPage() {
  const [mode, setMode] = useState<"login" | "signup">("login");

  const handleTabChange = (_: React.SyntheticEvent, newValue: "login" | "signup") => {
    setMode(newValue);
  };

  return (
    <Container maxWidth="sm">
      <Box
        sx={{
          mt: 8,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          p: 3,
          border: "1px solid #ddd",
          borderRadius: 2,
        }}
      >
        <Tabs
          value={mode}
          onChange={handleTabChange}
          centered
          sx={{ mb: 3, width: "100%" }}
        >
          <Tab label="Login" value="login" />
          <Tab label="Sign Up" value="signup" />
        </Tabs>

        <Typography variant="h4" sx={{ mb: 2 }}>
          {mode === "login" ? "Login to your account" : "Create an account"}
        </Typography>

        <AuthForm mode={mode} />

        <SSOButtons/>

        <Typography variant="body2" sx={{ mt: 2 }}>
          {mode === "login" ? (
            <>
              Don’t have an account?{" "}
              <Link onClick={() => setMode("signup")} sx={{ cursor: "pointer" }}>
                Sign up
              </Link>
            </>
          ) : (
            <>
              Already have an account?{" "}
              <Link onClick={() => setMode("login")} sx={{ cursor: "pointer" }}>
                Login
              </Link>
            </>
          )}
        </Typography>
      </Box>
    </Container>
  );
}
