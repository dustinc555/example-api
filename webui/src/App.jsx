import Box from "@mui/material/Box";

import { ThemeProvider, createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#337FDD",
    },
  },
});

import { useState } from "react";
import { usePhysicians } from "./services/physicians";

import PhysiciansList from "./components/PhysiciansList";
import Calendar from "./components/Calendar";

export default function App() {
  const { physicians, isLoading } = usePhysicians();
  const [selectedIndex, setSelectedIndex] = useState(null);

  if (!isLoading) {
    return (
      <ThemeProvider theme={theme}>
        <Box sx={{ display: "flex", flexDirection: "row", p: 1, m: 1 }}>
          <PhysiciansList
            physicians={physicians}
            selectedIndex={selectedIndex}
            setSelectedIndex={setSelectedIndex}
          />
          <Calendar {...physicians[selectedIndex]} />
        </Box>
      </ThemeProvider>
    );
  } else return <h1>Loading...</h1>;
}
