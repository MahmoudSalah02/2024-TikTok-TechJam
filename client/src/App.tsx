import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import IdeaList from "./components/IdeaList";

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/ideas" element={<IdeaList />} />
        {/* Add other routes here */}
      </Routes>
    </Router>
  );
};

export default App;
