import Box from "@mui/material/Box";

import { useState, useEffect } from "react";

import PhysiciansList from "./components/PhysiciansList";
import Calendar from "./components/Calendar";

export default function App() {
  const [physicians, setPhysicians] = useState([]);
  const [selectedIndex, setSelectedIndex] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8080/api/physicians")
      .then((response) => response.json())
      .then((data) => setPhysicians(data));
  }, []);

  console.log(selectedIndex);

  if (physicians.length > 0) {
    return (
      <Box sx={{ display: "flex", flexDirection: "row", p: 1, m: 1 }}>
        <PhysiciansList
          physicians={physicians}
          selectedIndex={selectedIndex}
          setSelectedIndex={setSelectedIndex}
        />
        <Calendar physician={physicians[selectedIndex] ?? {}} />
      </Box>
    );
  } else return <h1>No Data</h1>;
}
