function ATSReportCard({ report }) {
    return (
        <div className="bg-white rounded-xl shadow-lg p-8 mt-10">

            <h2 className="text-2xl font-bold mb-6">
                ATS Report
            </h2>

            {/* Score */}

            <div className="mb-8">

                <h3 className="font-semibold text-lg">
                    ATS Score
                </h3>

                <div className="w-full bg-gray-200 rounded-full h-5 mt-3">

                    <div
                        className="bg-green-500 h-5 rounded-full"
                        style={{ width: `${report.ats_score}%` }}
                    ></div>

                </div>

                <p className="mt-2 font-bold text-green-600">
                    {report.ats_score}%
                </p>

            </div>

            {/* Strengths */}

            <div className="mb-8">

                <h3 className="font-semibold text-lg mb-3">
                    Strengths
                </h3>

                <ul className="list-disc ml-6">

                    {report.strengths.map((item, index) => (

                        <li key={index}>
                            {item}
                        </li>

                    ))}

                </ul>

            </div>

            {/* Weaknesses */}

            <div className="mb-8">

                <h3 className="font-semibold text-lg mb-3">
                    Weaknesses
                </h3>

                <ul className="list-disc ml-6">

                    {report.weaknesses.map((item, index) => (

                        <li key={index}>
                            {item}
                        </li>

                    ))}

                </ul>

            </div>

            {/* Suggestions */}

            <div>

                <h3 className="font-semibold text-lg mb-3">
                    Suggestions
                </h3>

                <ul className="list-disc ml-6">

                    {report.suggestions.map((item, index) => (

                        <li key={index}>
                            {item}
                        </li>

                    ))}

                </ul>

            </div>

        </div>
    );
}

export default ATSReportCard;