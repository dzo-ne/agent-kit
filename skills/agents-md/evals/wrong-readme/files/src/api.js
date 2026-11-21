// Board API client. Reads the base URL from VITE_BOARD_API_URL (Vite only exposes VITE_* vars).
export const API_URL = import.meta.env.VITE_BOARD_API_URL;

export async function paint(x, y, color) {
  await fetch(`${API_URL}/paint`, { method: "POST", body: JSON.stringify({ x, y, color }) });
}
