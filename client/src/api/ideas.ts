import axios from "./axios";

export const getIdeas = async () => {
  try {
    const response = await axios.get("/ideas");
    return response.data;
  } catch (error) {
    console.error("Error fetching ideas:", error);
    throw error;
  }
};

export const createIdea = async (title: string, description: string) => {
  try {
    const response = await axios.post("/ideas", { title, description });
    return response.data;
  } catch (error) {
    console.error("Error creating idea:", error);
    throw error;
  }
};

export const voteIdea = async (id: string, upvote: boolean) => {
  try {
    const response = await axios.post(`/ideas/${id}/vote`, { upvote });
    return response.data;
  } catch (error) {
    console.error("Error voting idea:", error);
    throw error;
  }
};
