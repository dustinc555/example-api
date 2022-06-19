import useSWR from "swr";

const fetcher = (...args) => fetch(...args).then((res) => res.json());

const BaseUrl = "http://localhost:8080/api/physicians";

function usePhysicians() {
  const { data, error } = useSWR(`${BaseUrl}`, fetcher, {
    refreshInterval: 5000,
  });

  return {
    physicians: data,
    isLoading: !error && !data,
    isError: error,
  };
}

async function addAppointments(physician_id, appointments = []) {
  console.log(`posting to ${physician_id}`);
  console.log(appointments);

  await fetch(`${BaseUrl}/${physician_id}/appointments/add`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(appointments),
  })
    .then((response) => {
      if (response.status >= 400 && response.status < 600) {
        throw new Error("Bad response from server");
      }
      return response;
    })
    .catch((error) => {
      console.log(error);
    });
}

export { BaseUrl, usePhysicians, addAppointments };
