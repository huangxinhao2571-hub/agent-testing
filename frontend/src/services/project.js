import { postJson } from "./http";

export function createProject(payload) {
  return postJson("/api/v1/project/create", payload, { auth: true });
}
