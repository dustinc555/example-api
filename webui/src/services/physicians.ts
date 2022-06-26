import useSWR, { Fetcher, SWRConfiguration } from "swr";

export interface Appointment {
  _id: string;
  time: string;
  name: string;
  kind: string;
}

export interface Physician {
  _id: string;
  name: string;
  email: string;
  appointments: Appointment[];
}

export interface PhysiciansState {
  physicians: Physician[];
  isLoading: boolean;
  isError?: Error;
}

export const BaseUrl = "http://localhost:8080/api/physicians";

const fetcher: Fetcher<Physician[], string> = async (query) => {
  const res = await fetch(query, {
    method: "GET",
  });
  if (!res.ok) throw new Error("An error occurred while fetching the data.");

  const json = (await res.json()) as Physician[];
  return json;
};

export function usePhysicians(): PhysiciansState {
  const config: SWRConfiguration = {
    refreshInterval: 5000,
  };

  const { data, error } = useSWR<Physician[], Error>(BaseUrl, fetcher, config);

  return {
    physicians: data ?? [],
    isLoading: !error && !data,
    isError: error,
  };
}

type NewAppointment = Omit<Appointment, "_id">;

export async function addAppointments(
  physician_id: string,
  appointments: NewAppointment[] = []
) {
  const res = await fetch(`${BaseUrl}/${physician_id}/appointments/add`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(appointments),
  });

  if (!res.ok) {
    throw Error("An error occurred while fetching the data.");
  }
}
