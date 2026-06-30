import { useState } from "react";
import api from "../services/api";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function ResumeOptimizer({ jobDescription }) {
    const [loading, setLoading] = useState(false);
    const [optimizedResume, setOptimizedResume] = useState("");

    const optimizeResume = async () => {
        if (!jobDescription.trim()) {
            alert("Please paste a Job Description first.");
            return;
        }

        try {
            setLoading(true);

            const response = await api.post("/optimize-resume", {
                job_description: jobDescription,
            });

            setOptimizedResume(response.data.optimized_resume);
        } catch (err) {
            console.error(err);
            alert("Something went wrong.");
        } finally {
            setLoading(false);
        }
    };

    // Copy Resume
    const copyResume = async () => {
        try {
            await navigator.clipboard.writeText(optimizedResume);
            alert("Resume copied successfully!");
        } catch (err) {
            console.error(err);
        }
    };

    // Download Resume
    const downloadResume = () => {
        const element = document.createElement("a");

        const file = new Blob([optimizedResume], {
            type: "text/plain",
        });

        element.href = URL.createObjectURL(file);
        element.download = "Optimized_Resume.md";

        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    };

    return (
        <div className="mt-12 bg-white rounded-xl shadow p-8">

            <h2 className="text-2xl font-bold mb-6">
                AI Resume Optimizer
            </h2>

            <button
                onClick={optimizeResume}
                disabled={loading}
                className="mt-2 bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700 disabled:bg-gray-400"
            >
                {loading ? "Optimizing..." : "Optimize Resume"}
            </button>

            {optimizedResume && (
                <div className="mt-8">

                    {/* Action Buttons */}

                    <div className="flex gap-3 mb-5">

                        <button
                            onClick={copyResume}
                            className="bg-green-600 text-white px-5 py-2 rounded-lg hover:bg-green-700"
                        >
                            📋 Copy
                        </button>

                        <button
                            onClick={downloadResume}
                            className="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700"
                        >
                            ⬇ Download
                        </button>

                    </div>

                    {/* Resume */}

                    <div className="bg-gray-50 border rounded-xl p-6">

                        <div className="prose max-w-none">

                            <ReactMarkdown remarkPlugins={[remarkGfm]}>
                                {optimizedResume}
                            </ReactMarkdown>

                        </div>

                    </div>

                </div>
            )}
        </div>
    );
}

export default ResumeOptimizer;