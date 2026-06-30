import { useState } from "react";
import api from "../services/api";

function CareerAdvisor({ missingSkills }) {
    const [loading, setLoading] = useState(false);
    const [plan, setPlan] = useState(null);

    const generatePlan = async () => {
        try {
            setLoading(true);

            const res = await api.post("/career-advisor", {
                missing_skills: missingSkills,
            });
            
            console.log(res.data);
            setPlan(res.data);

        } catch (err) {
            console.log(err);
            alert("Failed to generate roadmap.");
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="mt-10 bg-white rounded-xl shadow p-8">

            <h2 className="text-2xl font-bold mb-6">
                AI Career Advisor
            </h2>

            <button
                onClick={generatePlan}
                className="bg-indigo-600 text-white px-6 py-3 rounded-lg hover:bg-indigo-700"
            >
                Generate Career Roadmap
            </button>

            {loading && (
                <p className="mt-5 text-indigo-600">
                    Creating roadmap...
                </p>
            )}

            {plan && (
                <div className="mt-8">

                    <h3 className="font-bold text-lg">
                        Estimated Duration
                    </h3>

                    <p className="mb-5">
                        {plan.estimated_duration}
                    </p>

                    <h3 className="font-bold text-lg">
                        Learning Roadmap
                    </h3>

                    <ul className="space-y-5">
                        {plan.roadmap.map((item, index) => (
                            <li
                                key={index}
                                className="border rounded-lg p-4 bg-gray-50"
                            >
                                <p className="font-bold">
                                    Step {item.step}: {item.topic}
                                </p>

                                <p className="mt-2">
                                    <strong>Skills:</strong>{" "}
                                    {item.skills.join(", ")}
                                </p>

                                <p className="mt-2">
                                    <strong>Resources:</strong>{" "}
                                    {item.resources.join(", ")}
                                </p>

                                <p className="mt-2 text-indigo-600">
                                    Duration: {item.duration}
                                </p>
                            </li>
                        ))}
                    </ul>

                    <h3 className="font-bold text-lg">
                        Interview Focus
                    </h3>

                    <ul className="list-disc ml-6">
                        {plan.interview_focus.map((item, index) => (
                            <li key={index}>{item}</li>
                        ))}
                    </ul>

                </div>
            )}

        </div>
    );
}

export default CareerAdvisor;