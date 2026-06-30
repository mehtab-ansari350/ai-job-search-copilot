import { useState } from "react";
import api from "../services/api";

function InterviewPreparation({ jobDescription }) {

    const [loading, setLoading] = useState(false);
    const [interview, setInterview] = useState(null);

    const generateInterview = async () => {

        if (!jobDescription.trim()) {
            alert("Please paste a Job Description first.");
            return;
        }

        try {

            setLoading(true);

            const response = await api.post(
                "/generate-interview",
                {
                    job_description: jobDescription
                }
            );

            setInterview(response.data);

        } catch (err) {

            console.log(err);

            alert("Failed to generate interview questions.");

        } finally {

            setLoading(false);

        }

    };

    const copyInterview = () => {

        navigator.clipboard.writeText(
            JSON.stringify(interview, null, 2)
        );

        alert("Interview Prep copied!");

    };

    const downloadInterview = () => {

        const blob = new Blob(
            [
                JSON.stringify(interview, null, 2)
            ],
            {
                type: "text/plain"
            }
        );

        const url = window.URL.createObjectURL(blob);

        const link = document.createElement("a");

        link.href = url;

        link.download = "Interview_Preparation.txt";

        link.click();

        window.URL.revokeObjectURL(url);

    };

    return (

        <div className="mt-12 bg-white rounded-xl shadow p-8">

            <h2 className="text-2xl font-bold mb-6">
                AI Interview Preparation
            </h2>

            <button
                onClick={generateInterview}
                className="bg-red-600 text-white px-6 py-3 rounded-lg hover:bg-red-700"
            >
                Generate Interview Questions
            </button>

            {loading && (

                <p className="mt-5 text-red-600">
                    Generating Interview Questions...
                </p>

            )}

            {interview && (

                <div className="mt-8">

                    <div className="flex gap-3 mb-6">

                        <button
                            onClick={copyInterview}
                            className="bg-green-600 text-white px-5 py-2 rounded-lg hover:bg-green-700"
                        >
                            Copy
                        </button>

                        <button
                            onClick={downloadInterview}
                            className="bg-blue-600 text-white px-5 py-2 rounded-lg hover:bg-blue-700"
                        >
                            Download
                        </button>

                    </div>

                    <h3 className="text-xl font-bold mb-4">
                        Technical Questions
                    </h3>

                    {interview.technical_questions.map((item, index) => (

                        <div
                            key={index}
                            className="mb-6 p-4 border rounded-lg bg-gray-50"
                        >

                            <p className="font-semibold">
                                Q{index + 1}. {item.question}
                            </p>

                            <p className="mt-2 text-gray-700">
                                <strong>Sample Answer:</strong>
                            </p>

                            <p>{item.sample_answer}</p>

                        </div>

                    ))}

                    <h3 className="text-xl font-bold mb-4">
                        Behavioral Questions
                    </h3>

                    {interview.behavioral_questions.map((item, index) => (

                        <div
                            key={index}
                            className="mb-6 p-4 border rounded-lg bg-gray-50"
                        >

                            <p className="font-semibold">
                                Q{index + 1}. {item.question}
                            </p>

                            <p className="mt-2 text-gray-700">
                                <strong>Sample Answer:</strong>
                            </p>

                            <p>{item.sample_answer}</p>

                        </div>

                    ))}

                    <h3 className="text-xl font-bold mb-4">
                        Interview Tips
                    </h3>

                    <ul className="list-disc ml-6">

                        {interview.tips.map((tip, index) => (

                            <li key={index}>
                                {tip}
                            </li>

                        ))}

                    </ul>

                </div>

            )}

        </div>

    );

}

export default InterviewPreparation;