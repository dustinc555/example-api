import {
  Typography,
  Stack,
  Box,
  TableContainer,
  Table,
  TableHead,
  TableRow,
  TableCell,
  tableCellClasses,
  TableBody,
  Paper,
} from "@mui/material";

import { styled } from "@mui/material/styles";

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  [`&.${tableCellClasses.head}`]: {
    backgroundColor: theme.palette.primary.main,
    color: theme.palette.common.white,
  },
  [`&.${tableCellClasses.body}`]: {
    fontSize: 14,
  },
}));

import AddComponentForm from "./AddAppointmentForm";

export default function Calendar({
  appointments = [],
  name = "",
  email = "",
  _id = "",
}) {
  const rowsprop = appointments.sort(
    (a, b) => new Date(b.time) - new Date(a.time)
  );

  return (
    <Stack spacing={2} sx={{ pl: 2, width: "100%" }}>
      <Typography variant="h4">{name}</Typography>
      <Typography variant="h6">{email}</Typography>
      <TableContainer sx={{ maxHeight: 440 }} component={Paper}>
        <Table stickyHeader>
          <TableHead>
            <TableRow>
              <StyledTableCell align="right">#</StyledTableCell>
              <StyledTableCell align="right">Name</StyledTableCell>
              <StyledTableCell align="right">Time</StyledTableCell>
              <StyledTableCell align="right">Kind</StyledTableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rowsprop.map((row) => (
              <TableRow
                key={row._id}
                sx={{ "&:last-child td, &:last-child th": { border: 0 } }}
              >
                <TableCell align="right">{row._id}</TableCell>
                <TableCell align="right">{row.name}</TableCell>
                <TableCell align="right">{row.time}</TableCell>
                <TableCell align="right">{row.kind}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
      {_id !== "" ? (
        <Box sx={{ display: "flex", flexDirection: "row" }}>
          <AddComponentForm physician_id={_id} />
        </Box>
      ) : null}
    </Stack>
  );
}
