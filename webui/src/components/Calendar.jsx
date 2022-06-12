import { DataGrid } from "@mui/x-data-grid";
import Box from "@mui/material/Box";

export default function Calendar(props) {
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

  console.log("i got");
  console.log(props);

  let rows = props.physician.appointments ?? [];
  let name = props.physician.name ?? "";
  let email = props.physician.email ?? "";

  rows = rows.map((r) => {
    return {
      ...r,
      id: r._id,
    };
  });

  return (
    <Box sx={{ p: 2, width: "100%" }}>
      <h1>{name}</h1>
      <h4>{email}</h4>
      <DataGrid
        paging={true}
        pageSize={6}
        emptyRowsWhenPaging={false}
        pageSizeOptions={[6, 12, 20, 50]}
        rows={rows}
        columns={columns}
      />
    </Box>
  );
}
