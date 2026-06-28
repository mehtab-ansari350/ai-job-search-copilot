function JobCard({ job }) {
    return (
        <div className="border rounded-xl p-6 flex justify-between items-center shadow-sm hover:shadow-md transition">

            <div>

                <h3 className="text-xl font-semibold">
                    {job.title}
                </h3>

                <p className="text-gray-600">
                    {job.company}
                </p>

                <p className="text-gray-500">
                    {job.location}
                </p>

            </div>

            <div className="text-right">

                <p className="text-2xl font-bold text-green-600">
                    {job.match_score}%
                </p>

                <p className="text-sm text-gray-500">
                    Match
                </p>

            </div>

        </div>
    );
}

export default JobCard;