"use client";

import { useState } from "react";

export default function Home() {
  const [url, setUrl] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const researchCompany = async () => {
    if (!url) return;

    setLoading(true);

    try {
      const API_URL = process.env.NEXT_PUBLIC_API_URL;

      const res = await fetch(
         `${API_URL}/research?url=${encodeURIComponent(query)}`
      );

      const data = await res.json();

      setResult(data.analysis);
    } catch (err) {
      setResult("Failed to connect to backend.");
    }

    setLoading(false);
  };

   const downloadReport = () => {
    window.open(
      `${API_URL}/download-report?url=${encodeURIComponent(query)}`
    );
  };

  return (
    <main style={{ padding: "40px", fontFamily: "Arial" }}>
      <h1>🚀 Geko AI Company Research</h1>

      <input
        type="text"
        placeholder="https://python.org"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        style={{
          width: "500px",
          padding: "10px",
          fontSize: "16px",
        }}
      />

      <button
        onClick={researchCompany}
        style={{
          marginLeft: "10px",
          padding: "10px 20px",
        }}
      >
        Research
      </button>

      <button
        onClick={downloadReport}
        style={{
          marginLeft: "10px",
          padding: "10px 20px",
          background: "green",
          color: "white",
          cursor: "pointer",
        }}
      >
        Download PDF
      </button>

      {loading && <p>Analyzing company...</p>}

      <pre
        style={{
          whiteSpace: "pre-wrap",
          marginTop: "30px",
          background: "#f5f5f5",
          padding: "20px",
          borderRadius: "10px",
        }}
      >
        {result}
      </pre>
    </main>
  );
}