import logo from "./logo.svg";
import "./App.css";
import Area from "./pages/Area.page";
import MultiAxisLineChart from "./components/Graph";
import { useEffect, useState } from "react";
import axios from "axios";
import DetailArea from "./pages/DetailArea";

function App() {
  
  console.log(stateG);
  return (
    <div className="App">
      <div style={{ display: "grid" }}>
        <Area /> {/* Area takes 50% width */}
        <DetailArea/>
      </div>
    </div>
  );
}

export default App;
