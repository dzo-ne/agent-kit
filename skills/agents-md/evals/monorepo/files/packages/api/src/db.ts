// The only module that talks to Postgres. Routes call these functions;
// never import `pg` anywhere else, so pooling and transactions stay in one place.
import pg from "pg";

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });

export async function listTasks() {
  return (await pool.query("SELECT id, title FROM tasks ORDER BY id")).rows;
}
