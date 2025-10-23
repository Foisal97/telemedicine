import { Button, Stack, Typography } from "@mui/material";
import { Google, Microsoft } from "@mui/icons-material";

export default function SSOButtons() {
  const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

  const handleSSO = (provider: "google" | "microsoft") => {
    window.location.href = `${API_URL}/auth/${provider}`;
  };

  return (
    <Stack spacing={2} sx={{ mt: 3 }}>
      <Typography
        variant="body1"
        align="center"
        sx={{ color: "text.secondary", mb: 1 }}
      >
        Or sign in with
      </Typography>

      <Button
        variant="outlined"
        fullWidth
        startIcon={<Google sx={{ fontSize: 24 }} />}
        onClick={() => handleSSO("google")}
        sx={{
          borderRadius: 2,
          py: 1.2,
          textTransform: "none",
          fontWeight: 500,
          color: "#4285F4",
          borderColor: "#4285F4",
          transition: "0.3s",
          "&:hover": {
            backgroundColor: "#4285F4",
            color: "white",
            boxShadow: "0 4px 12px rgba(66,133,244,0.4)",
          },
        }}
      >
        Continue with Google
      </Button>

      <Button
        variant="outlined"
        fullWidth
        startIcon={<Microsoft sx={{ fontSize: 24 }} />}
        onClick={() => handleSSO("microsoft")}
        sx={{
          borderRadius: 2,
          py: 1.2,
          textTransform: "none",
          fontWeight: 500,
          color: "#2F2F2F",
          borderColor: "#2F2F2F",
          transition: "0.3s",
          "&:hover": {
            backgroundColor: "#2F2F2F",
            color: "white",
            boxShadow: "0 4px 12px rgba(47,47,47,0.4)",
          },
        }}
      >
        Continue with Microsoft
      </Button>
    </Stack>
  );
}
