import { BrowserRouter, Routes, Route } from "react-router-dom"
import AuthPage from "./pages/AuthPage"
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<AuthPage/>}></Route>
        <Route path="*" element={<AuthPage/>}></Route>
      </Routes>
    </BrowserRouter>
  )
}

export default App
