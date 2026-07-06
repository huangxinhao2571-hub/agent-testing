const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "";

export async function postJson(path, payload, options = {}) {
  const headers = {
    "Content-Type": "application/json"
  };

  if (options.auth) {
    const token = localStorage.getItem("teamhelper_token");
    if (token) {
      headers.Authorization = `Bearer ${token}`;
    }
  }

  const response = await fetch(`${API_BASE_URL}${path}`, {
    method: "POST",
    headers,
    body: JSON.stringify(payload)
  });

  const text = await response.text();
  let result = null;

  if (text) {
    try {
      result = JSON.parse(text);
    } catch (error) {
      throw new Error(`接口返回不是合法 JSON: ${text}`);
    }
  }

  if (!response.ok) {
    throw new Error(result?.msg || `接口请求失败: ${response.status} ${response.statusText}`);
  }

  return result;
}
