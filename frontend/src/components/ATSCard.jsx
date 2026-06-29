import { FaAward } from "react-icons/fa";

function ATSCard({ score }) {
  return (
    <div className="bg-white shadow-lg rounded-xl p-6 border hover:shadow-xl transition">

      <div className="flex justify-between items-center">

        <h3 className="text-gray-500">
          ATS Score
        </h3>

        <FaAward className="text-blue-600 text-2xl" />

      </div>

      <p className="text-5xl font-bold text-blue-600 mt-5">
        {score}%
      </p>

    </div>
  );
}

export default ATSCard;