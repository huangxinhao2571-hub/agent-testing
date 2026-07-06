import { postJson } from "./http";

export function registerUser(payload) {
  return postJson("/api/v1/user/register", payload);
}

export function loginUser(payload) {
  return postJson("/api/v1/user/login", payload);
}
