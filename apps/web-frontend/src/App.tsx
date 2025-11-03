import {Routes, Route } from "react-router-dom"
import AuthPage from "./pages/AuthPage"
import LandingPage from "./pages/LandingPage"
import AppLayout from "./layout/AppLayout"
function App() {
  return (
    <>
      <Routes>
        <Route element={<AppLayout/>}>
        <Route path="/" element={<LandingPage />} />
        <Route path="/auth" element={<AuthPage/>}></Route>
        </Route>
      </Routes>
    </>
  )
}

export default App
