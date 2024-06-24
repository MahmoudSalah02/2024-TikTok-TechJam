import axios from "./axios";

export const register = async (username: string, password: string) => {
  try {
    const response = await axios.post("/register", { username, password });
    return response.data;
  } catch (error) {
    console.error("Error registering user:", error);
    throw error;
  }
};

export const login = async (username: string, password: string) => {
  try {
    const response = await axios.post("/login", { username, password });
    return response.data;
  } catch (error) {
    console.error("Error logging in user:", error);
    throw error;
  }
};
