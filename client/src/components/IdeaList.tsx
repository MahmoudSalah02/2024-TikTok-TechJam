import React, { useEffect, useState } from "react";
import { getIdeas, createIdea, voteIdea } from "../api/ideas";

interface Idea {
  id: string;
  title: string;
  description: string;
  votes: number;
}

const IdeaList: React.FC = () => {
  const [ideas, setIdeas] = useState<Idea[]>([]);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    const fetchIdeas = async () => {
      try {
        const data = await getIdeas();
        setIdeas(data);
      } catch (error) {
        console.error("Failed to fetch ideas", error);
      }
    };

    fetchIdeas();
  }, []);

  const handleCreateIdea = async () => {
    try {
      const newIdea = await createIdea(title, description);
      setIdeas([...ideas, newIdea]);
      setTitle("");
      setDescription("");
    } catch (error) {
      console.error("Failed to create idea", error);
    }
  };

  const handleVote = async (id: string, upvote: boolean) => {
    try {
      const updatedIdea = await voteIdea(id, upvote);
      setIdeas(ideas.map((idea) => (idea.id === id ? updatedIdea : idea)));
    } catch (error) {
      console.error("Failed to vote on idea", error);
    }
  };

  return (
    <div>
      <h1>Idea List</h1>
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button onClick={handleCreateIdea}>Create Idea</button>
      <ul>
        {ideas.map((idea) => (
          <li key={idea.id}>
            <h2>{idea.title}</h2>
            <p>{idea.description}</p>
            <p>Votes: {idea.votes}</p>
            <button onClick={() => handleVote(idea.id, true)}>Upvote</button>
            <button onClick={() => handleVote(idea.id, false)}>Downvote</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default IdeaList;
