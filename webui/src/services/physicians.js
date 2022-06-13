import useSWR from "swr";

const fetcher = (...args) => fetch(...args).then((res) => res.json());

export function usePhysicians() {
  const { data, error } = useSWR(
    `http://localhost:8080/api/physicians`,
    fetcher
  );

  return {
    physicians: data,
    isLoading: !error && !data,
    isError: error,
  };
}
