import React, { useState } from "react";
import Stack from "@mui/material/Stack";
import Paper from "@mui/material/Paper";
import { styled } from "@mui/material/styles";

const DetailArea = () => {
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
  
  return (
    <>
      
      {stateG && (
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', height: '50vh'  }}>
            <MultiAxisLineChart data={stateG} />
          </div>
        )}
    </>
  );
};

export default DetailArea;
