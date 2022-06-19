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
}));

const StyledTableRow = styled(TableRow)(({ theme }) => ({
  "&:nth-of-type(even)": {
    backgroundColor: theme.palette.action.hover,
  },
  "& .MuiTableCell-root": {
    borderLeft: "1px solid rgba(224, 224, 224, 1)",
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
    (a, b) => new Date(a.time) - new Date(b.time)
  );

  return (
    <Stack spacing={2} sx={{ pl: 2, width: "100%" }}>
      <Typography variant="h4">{name}</Typography>
      <Typography variant="h6">{email}</Typography>
      <TableContainer sx={{ maxHeight: 440 }} component={Paper}>
        <Table stickyHeader>
          <TableHead>
            <TableRow>
              <StyledTableCell align="left">#</StyledTableCell>
              <StyledTableCell align="left">Name</StyledTableCell>
              <StyledTableCell align="left">Time</StyledTableCell>
              <StyledTableCell align="left">Kind</StyledTableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rowsprop.map((row) => (
              <StyledTableRow key={row._id}>
                <TableCell align="left">{row._id}</TableCell>
                <TableCell align="left">{row.name}</TableCell>
                <TableCell align="left">{row.time}</TableCell>
                <TableCell align="left">{row.kind}</TableCell>
              </StyledTableRow>
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
