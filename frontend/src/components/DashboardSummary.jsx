import { FaAward, FaBuilding, FaBullseye } from "react-icons/fa";

function DashboardSummary({ result }) {
    return (
        <div className="mt-10">

            <h2 className="text-2xl font-bold mb-6">
                Resume Analysis
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

                {/* ATS */}

                <div className="bg-white shadow-lg rounded-xl p-6 border hover:shadow-xl transition">

                    <div className="flex justify-between items-center">

                        <h3 className="text-gray-500">
                            ATS Score
                        </h3>

                        <FaAward className="text-blue-600 text-2xl" />

                    </div>

                    <p className="text-5xl font-bold text-blue-600 mt-5">
                        {result.ats_report.ats_score}%
                    </p>

                </div>

                {/* Match */}

                <div className="bg-white shadow-lg rounded-xl p-6 border hover:shadow-xl transition">

                    <div className="flex justify-between items-center">

                        <h3 className="text-gray-500">
                            Best Match
                        </h3>

                        <FaBullseye className="text-green-600 text-2xl" />

                    </div>

                    <p className="text-5xl font-bold text-green-600 mt-5">
                        {result.ranked_jobs[0].match_score}%
                    </p>

                </div>

                {/* Company */}

                <div className="bg-white shadow-lg rounded-xl p-6 border hover:shadow-xl transition">

                    <div className="flex justify-between items-center">

                        <h3 className="text-gray-500">
                            Top Company
                        </h3>

                        <FaBuilding className="text-purple-600 text-2xl" />

                    </div>

                    <p className="text-xl font-bold mt-5">
                        {result.ranked_jobs[0].company}
                    </p>

                    <p className="text-gray-500">
                        {result.ranked_jobs[0].title}
                    </p>

                </div>

            </div>

        </div>
    );
}

export default DashboardSummary;