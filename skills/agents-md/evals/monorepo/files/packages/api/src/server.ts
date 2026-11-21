import Fastify from "fastify";
import { listTasks } from "./db";

const app = Fastify();
app.get("/tasks", async () => listTasks());
app.listen({ port: 3001 });
