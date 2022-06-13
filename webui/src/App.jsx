import Box from "@mui/material/Box";

import { useState } from "react";
import { usePhysicians } from "./services/physicians";

import PhysiciansList from "./components/PhysiciansList";
import Calendar from "./components/Calendar";

export default function App() {
  const { physicians, isLoading } = usePhysicians();
  const [selectedIndex, setSelectedIndex] = useState(null);

  console.log(selectedIndex);

  if (!isLoading) {
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