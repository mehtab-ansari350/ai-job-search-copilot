import { useState } from "react";
import api from "../services/api";

function Dashboard() {
    const [jobDescription, setJobDescription] = useState("");
    const [result, setResult] = useState(null);
    const [loading, setLoading] = useState(false);

    const analyzeResume = async () => {
    try {
        setLoading(true);

        const res = await api.post("/analyze-job", {
            job_description: jobDescription,
        });

        setResult(res.data);

    } catch (error) {
        console.log(error);
    } finally {
        setLoading(false);
    }
};

   

  return (
    <div className="min-h-screen bg-gray-100">

      <div className="max-w-6xl mx-auto p-10">

        <h1 className="text-4xl font-bold text-center mb-10">
          AI Job Search Copilot
        </h1>

        <div className="bg-white rounded-xl shadow p-8">

          <h2 className="text-xl font-semibold mb-4">
            Resume Upload
          </h2>

          <input
            type="file"
            className="mb-8"
          />

          <h2 className="text-xl font-semibold mb-4">
            Job Description
          </h2>

          <textarea
            className="w-full border rounded-lg p-4 h-60"
            placeholder="Paste Job Description..."
            value={jobDescription}
            onChange={(e) => setJobDescription(e.target.value)}
          />

          <button
            onClick={analyzeResume}
            className="mt-6 bg-blue-600 text-white px-8 py-3 rounded-lg hover:bg-blue-700"
           > 
            Analyze Resume
          </button>
          
          {/* Loading Message */}

          {loading && (
              <p className="mt-6 text-blue-600">
                  Analyzing Resume...
              </p>
          )}

          {/* Temporary JSON */}

          {result && (
              <pre className="mt-8 bg-gray-900 text-green-400 p-5 rounded-lg overflow-auto">
                  {JSON.stringify(result, null, 2)}
              </pre>
          )}
        </div>

      </div>

    </div>
  )
}

export default Dashboard;