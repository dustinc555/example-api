import { DataGrid } from "@mui/x-data-grid";
import { Typography, Stack, Box } from "@mui/material";

import AddComponentForm from "./AddAppointmentForm";

export default function Calendar({
  appointments = [],
  name = "",
  email = "",
  _id = "",
}) {
  const columns = [
    { field: "id", headerName: "#", width: 50 },
    { field: "name", headerName: "Name", width: 130 },
    {
      field: "time",
      headerName: "Time",
      width: 160,
      type: "dateTime",
    },
    { field: "kind", headerName: "Kind", width: 130 },
  ];

  const rowsprop = appointments.map((r) => ({
    ...r,
    id: r._id,
  }));

  return (
    <Stack spacing={2} sx={{ pl: 2, width: "100%" }}>
      <Typography variant="h4">{name}</Typography>
      <Typography variant="h6">{email}</Typography>
      <DataGrid
        paging={true}
        sx={{ minHeight: 300 }}
        emptyRowsWhenPaging={false}
        pageSizeOptions={[6, 12, 20, 50]}
        rows={rowsprop}
        columns={columns}
        initialState={{
          sorting: {
            sortModel: [{ field: "time", sort: "asc" }],
          },
        }}
      />
      {_id !== "" ? (
        <Box sx={{ display: "flex", flexDirection: "row" }}>
          <AddComponentForm physician_id={_id} />
        </Box>
      ) : null}
    </Stack>
  );
}
