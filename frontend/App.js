import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [caption, setCaption] = useState("");
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;
    setLoading(true);
    const formData = new FormData();
    formData.append("file", file);
    const res = await fetch("http://localhost:8000/caption", {
      method: "POST",
      body: formData,
    });
    const data = await res.json();
    setCaption(data.caption);
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 400, margin: "2rem auto", textAlign: "center" }}>
      <h2>AI Image Caption Generator</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" accept="image/*" onChange={handleFileChange} />
        <br />
        <button type="submit" disabled={loading} style={{ marginTop: 10 }}>
          {loading ? "Generating..." : "Generate Caption"}
        </button>
      </form>
      {caption && (
        <div style={{ marginTop: 20 }}>
          <strong>Caption:</strong>
          <div>{caption}</div>
        </div>
      )}
    </div>
  );
}

export default App;
