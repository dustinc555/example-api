import * as React from "react";
import Box from "@mui/material/Box";
import List from "@mui/material/List";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import Button from "@mui/material/Button";

import { Typography } from "@mui/material";

import { Physician } from "@/services/physicians";

interface Props {
  selectedIndex: number;
  setSelectedIndex: React.Dispatch<React.SetStateAction<number>>;
  physicians: Physician[];
}

export default function PhysiciansList({
  selectedIndex,
  setSelectedIndex,
  physicians = [],
}: Props) {
  const handleListItemClick = (index: number) => {
    setSelectedIndex(index);
  };

  return (
    <Box sx={{ p: 2, width: "100%", maxWidth: 360, bgcolor: "#F4F4F6" }}>
      <Box>
        <Typography
          style={{ fontFamily: "sans-serif", fontWeight: "bold" }}
          variant="h4"
          color="primary"
        >
          Example
        </Typography>
      </Box>

      <Box mt={4}>
        <Typography variant="h6">PHYSICIANS</Typography>
      </Box>
      <List component="nav" aria-label="secondary mailbox folder">
        {physicians.map((p, index) => (
          <ListItemButton
            key={index}
            selected={selectedIndex === index}
            onClick={(event) => handleListItemClick(index)}
          >
            <ListItemText primary={p.name} />
          </ListItemButton>
        ))}
      </List>
      <Box
        sx={{ pt: 8, pb: 8 }}
        display="flex"
        justifyContent="center"
        alignItems="center"
      >
        <Button variant="contained">Logout</Button>
      </Box>
    </Box>
  );
}
