import React, { useEffect, useState } from "react";
import AreaCard from "../components/Card";
import axios from "axios";
import Graph from "../components/Graph";
import MultiAxisLineChart from "../components/Graph";

const Area = () => {
  const [state, setState] = useState([]); // Correct usage of useState

  const list = [
    { name: "AREA : X", temp: "20", colors: "red" },
    { name: "Area : Y", temp: "22", colors: "green" },
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      getCount(); // Call it initially to fetch the count
    }, 1000);

    return () => clearInterval(interval); // Clear the interval on component unmount
  }, []); // Empty dependency array ensures this effect runs only once

  const getCount = async () => {
    try {
      const response = await axios.get("http://localhost:5000/latest_counter");
      console.log(response.data);
      setState(response.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  return (
    <div style={{ display: "inline-flex", justifyContent: 'center', alignItems: 'center' }}>
      <AreaCard
        name={"All (X+Y)"}
        colors={"grey"}
        count={state[0]?.count + state[1]?.count}
      />
      {state?.map((data, id) => (
        <>
          <div key={id} style={{ display: "inline-flex" }}>
            <AreaCard name={data.area} colors={"grey"} count={data.count} />
          </div>
        </>
      ))}
      <br></br>
    </div>
  );
};

export default Area;
