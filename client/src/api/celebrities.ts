import axios from "./axios";

export const getIdeas = async (celebrityId: string) => {
  try {
    const response = await axios.get(`/celebrities/${celebrityId}/ideas`);
    return response.data;
  } catch (error) {
    console.error("Error fetching ideas:", error);
    throw error;
  }
};

export const createIdea = async (
  celebrityId: string,
  title: string,
  description: string
) => {
  try {
    const response = await axios.post(`/celebrities/${celebrityId}/ideas`, {
      title,
      description,
    });
    return response.data;
  } catch (error) {
    console.error("Error creating idea:", error);
    throw error;
  }
};

export const voteIdea = async (
  celebrityId: string,
  ideaId: string,
  upvote: boolean
) => {
  try {
    const response = await axios.post(
      `/celebrities/${celebrityId}/ideas/${ideaId}/vote`,
      { upvote }
    );
    return response.data;
  } catch (error) {
    console.error("Error voting idea:", error);
    throw error;
  }
};
