import logo from "./logo.svg";
import "./App.css";
import Area from "./pages/Area.page";
import MultiAxisLineChart from "./components/Graph";
import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [stateG, setStateG] = useState([]); // Correct usage of useState

  useEffect(() => {
  
    const getCount_graph = async () => {
      try {
        const response = await axios.get("http://localhost:5000/counter");
        console.log(response.data);
        setStateG(response.data);
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    };
    const interval = setInterval(() => {
    getCount_graph()},5000)

    return () => clearInterval(interval);
  }, []
)
  
  console.log(stateG);
  return (
    <div className="App">
      <div style={{ display: "grid" }}>
        <Area /> {/* Area takes 50% width */}
        {stateG && (
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh'  }}>
            <MultiAxisLineChart data={stateG} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
