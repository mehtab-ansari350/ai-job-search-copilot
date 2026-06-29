import { FaBullseye } from "react-icons/fa";

function BestMatchCard({ score }) {
    return (
        <div className="bg-white shadow-lg rounded-xl p-6 border hover:shadow-xl transition">

            <div className="flex justify-between items-center">

                <h3 className="text-gray-500">
                    Best Match
                </h3>

                <FaBullseye className="text-green-600 text-2xl" />

            </div>

            <p className="text-5xl font-bold text-green-600 mt-5">
                {score}%
            </p>

        </div>
    );
}

export default BestMatchCard;