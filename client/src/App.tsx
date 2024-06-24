import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import IdeaList from "./components/IdeaList";
import Signup from "./components/Signup";
import Login from "./components/Login";

const App: React.FC = () => {
  return (
    <AuthProvider>
      <Router>
        <Routes>
          <Route path="/ideas" element={<IdeaList />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/login" element={<Login />} />
          {/* Add other routes here */}
        </Routes>
      </Router>
    </AuthProvider>
  );
};

export default App;
