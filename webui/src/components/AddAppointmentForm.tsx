import React from "react";
import { useFormik, FormikProps } from "formik";
import {
  TextField,
  FormControl,
  Button,
  MenuItem,
  Stack,
  Typography,
  Paper,
} from "@mui/material";

import { addAppointments } from "@/services/physicians";

interface FormValues {
  time: string;
  kind: string;
  name: string;
}

interface FormErrors {
  name?: string;
  time?: string;
}

const validate = (values: FormValues) => {
  const errors: FormErrors = {};
  if (!values.name) {
    errors.name = "Required";
  }

  if (!values.time) {
    errors.time = "Required";
  }

  return errors;
};

interface Props {
  physician_id: string;
}

export default function AddAppointmentForm({ physician_id }: Props) {
  const formik = useFormik({
    initialValues: {
      name: "",
      time: "",
      kind: "Follow-up",
    },
    validate,
    onSubmit: async (values) => {
      try {
        await addAppointments(physician_id, [values]);
        alert("success");
      } catch (error) {
        alert(`Failed to schedule appointment: ${error}`);
      }
    },
  });
  return (
    <Paper elevation={3} style={{ padding: 4 }}>
      <form onSubmit={formik.handleSubmit}>
        <Typography align="center" sx={{ mb: 2 }} variant="h6">
          Create New Appointment
        </Typography>
        <FormControl>
          <Stack spacing={4}>
            <TextField
              id="name"
              error={!!formik.errors.name}
              helperText={formik.errors.name}
              label="Name"
              onChange={formik.handleChange}
              value={formik.values.name}
            />
            <TextField
              id="kind"
              name="kind"
              value={formik.values.kind}
              label="Kind"
              onChange={formik.handleChange}
              select
            >
              <MenuItem value="New Patient">New Patient</MenuItem>
              <MenuItem value="Follow-up">Follow-up</MenuItem>
            </TextField>
            <TextField
              id="time"
              label="Date&Time"
              type="datetime-local"
              value={formik.values.time}
              error={!!formik.errors.time}
              helperText={formik.errors.time}
              onChange={formik.handleChange}
              InputLabelProps={{
                shrink: true,
              }}
            />
            <Button variant="contained" type="submit">
              Submit
            </Button>
          </Stack>
        </FormControl>
      </form>
    </Paper>
  );
}
