import React from "react";
import { AppBar, Toolbar, Typography, Button, Box } from "@mui/material";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
    const navigate = useNavigate();
  return (
    <AppBar
      position="sticky"
      sx={{
        backgroundColor: "#ffffff",
        boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
        padding: 0,
        margin: 0,
      }}
    >
      <Toolbar
        disableGutters // removes default Toolbar padding
        sx={{
          display: "flex",
          justifyContent: "space-between",
          minHeight: "64px",
        }}
      >
        {/* Logo / Brand */}
        <Typography
          variant="h6"
          sx={{
            fontWeight: "bold",
            fontSize: "1.8rem",
            fontFamily: "'Montserrat', sans-serif",
            color: "#1976d2",
            marginLeft: 2, // optional small spacing from edge
          }}
          onClick={()=> navigate("/")}>
          Total Med
        </Typography>

        {/* Navigation Buttons */}
        <Box sx={{ display: "flex", gap: 2, marginRight: 2 }}>
          {/* Regular links */}

          {/* Sign Up - just text */}
          <Button
            sx={{
              color: "#1976d2",
              fontWeight: "bold",
              textTransform: "none",
              minWidth: "auto",
              "&:hover": { backgroundColor: "rgba(25, 118, 210, 0.1)" },
            }}
          onClick={()=> navigate("/auth")}>
            Sign In
          </Button>
          <Button
            href="#features"
            sx={{
              color: "black",
              fontWeight: "medium",
              textTransform: "none",
              minWidth: "auto",
              "&:hover": { backgroundColor: "rgba(0,0,0,0.05)" },
            }}
            
          >
            Appointments
          </Button>
          <Button
            sx={{
              color: "black",
              fontWeight: "medium",
              textTransform: "none",
              minWidth: "auto",
              "&:hover": { backgroundColor: "rgba(0,0,0,0.05)" },
            }}
          >
            Check Ups
          </Button>
          <Button
            sx={{
              color: "black",
              fontWeight: "medium",
              textTransform: "none",
              minWidth: "auto",
              "&:hover": { backgroundColor: "rgba(0,0,0,0.05)" },
            }}
          >
            Medicine
          </Button>

          {/* Become a Doctor - filled background */}
          <Button
            sx={{
              backgroundColor: "#1976d2",
              color: "white",
              fontWeight: "medium",
              textTransform: "none",
              borderRadius: 1,
              minWidth: "auto",
              "&:hover": { backgroundColor: "#115293" },
            }}
          >
            Become a Doctor
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
