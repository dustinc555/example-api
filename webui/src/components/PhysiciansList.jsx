import * as React from "react";
import Box from "@mui/material/Box";
import List from "@mui/material/List";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemText from "@mui/material/ListItemText";
import Button from "@mui/material/Button";

export default function PhysiciansList({
  selectedIndex,
  setSelectedIndex,
  physicians = [],
}) {
  const handleListItemClick = (event, index) => {
    setSelectedIndex(index);
  };

  return (
    <Box sx={{ p: 2, width: "100%", maxWidth: 360, bgcolor: "#F4F4F6" }}>
      <h1 style={{ color: "#397ADD" }}>notable</h1>
      <h3>PHYSICIANS</h3>
      <List component="nav" aria-label="secondary mailbox folder">
        {physicians.map((p, index) => (
          <ListItemButton
            key={index}
            selected={selectedIndex === index}
            onClick={(event) => handleListItemClick(event, index)}
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
        <Button>Logout</Button>
      </Box>
    </Box>
  );
}
