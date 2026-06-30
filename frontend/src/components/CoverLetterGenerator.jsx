import { useState } from "react";
import api from "../services/api";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

function CoverLetterGenerator({ jobDescription }) {

    const [loading, setLoading] = useState(false);
    const [coverLetter, setCoverLetter] = useState("");

    const generateCoverLetter = async () => {

        if (!jobDescription.trim()) {
            alert("Please paste a Job Description first.");
            return;
        }

        try {

            setLoading(true);

            const response = await api.post(
                "/generate-cover-letter",
                {
                    job_description: jobDescription
                }
            );

            setCoverLetter(response.data.cover_letter);

        }

        catch (err) {

            console.log(err);

            alert("Failed to generate cover letter.");

        }

        finally {

            setLoading(false);

        }

    };

    const copyToClipboard = () => {

        navigator.clipboard.writeText(coverLetter);

        alert("Cover Letter copied!");

    };

    const downloadCoverLetter = () => {

        const blob = new Blob(
            [coverLetter],
            {
                type: "text/plain"
            }
        );

        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = "Cover_Letter.txt";

        link.click();

        window.URL.revokeObjectURL(url);

    };

    return (

        <div className="mt-12 bg-white rounded-xl shadow p-8">

            <h2 className="text-2xl font-bold mb-6">
                AI Cover Letter Generator
            </h2>

            <button
                onClick={generateCoverLetter}
                className="bg-purple-600 text-white px-6 py-3 rounded-lg hover:bg-purple-700"
            >
                Generate Cover Letter
            </button>

            {loading && (

                <p className="mt-6 text-purple-600">
                    Generating Cover Letter...
                </p>

            )}

            {coverLetter && (

                <div className="mt-8">

                    <div className="flex gap-3 mb-5">

                        <button
                            onClick={copyToClipboard}
                            className="bg-green-600 text-white px-5 py-2 rounded-lg hover:bg-green-700"
                        >
                            Copy
                        </button>

                        <button
                            onClick={downloadCoverLetter}
                            className="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700"
                        >
                            Download
                        </button>

                    </div>

                    <div className="bg-gray-50 rounded-xl p-6 border">

                        <div className="prose prose-indigo max-w-none">

                            <ReactMarkdown
                                remarkPlugins={[remarkGfm]}
                            >
                                {coverLetter}
                            </ReactMarkdown>

                        </div>

                    </div>

                </div>

            )}

        </div>

    );

}

export default CoverLetterGenerator;