import { DataGrid } from "@mui/x-data-grid";
import Box from "@mui/material/Box";

import Typography from "@mui/material/Typography";

export default function Calendar({ appointments = [], name = "", email = "" }) {
  const columns = [
    { field: "id", headerName: "#", width: 50 },
    { field: "name", headerName: "Name", width: 130 },
    {
      field: "time",
      headerName: "Time",
      width: 130,
      type: "dateTime",
    },
    { field: "kind", headerName: "Kind", width: 130 },
  ];

  const rowsprop = appointments.map((r) => ({
    ...r,
    id: r._id,
  }));

  return (
    <Box sx={{ pl: 2, width: "100%" }}>
      <Typography variant="h4">{name}</Typography>
      <Typography variant="h6">{email}</Typography>
      <DataGrid
        paging={true}
        pageSize={6}
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
    </Box>
  );
}
