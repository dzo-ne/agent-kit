// The web app reaches data only through the API's HTTP routes, never the database.
export async function fetchTasks() {
  return (await fetch("/api/tasks")).json();
}
