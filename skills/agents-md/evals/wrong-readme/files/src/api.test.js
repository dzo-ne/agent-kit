import { test, expect } from "vitest";
import { API_URL } from "./api.js";

test("api url is a string or undefined", () => {
  expect(["string", "undefined"]).toContain(typeof API_URL);
});
