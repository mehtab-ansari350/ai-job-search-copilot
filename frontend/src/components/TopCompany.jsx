import { FaBuilding } from "react-icons/fa";

function TopCompanyCard({ company, title }) {
    return (
        <div className="bg-white shadow-lg rounded-xl p-6 border hover:shadow-xl transition">

            <div className="flex justify-between items-center">

                <h3 className="text-gray-500">
                    Top Company
                </h3>

                <FaBuilding className="text-purple-600 text-2xl" />

            </div>

            <p className="text-xl font-bold mt-5">
                {company}
            </p>

            <p className="text-gray-500">
                {title}
            </p>

        </div>
    );
}

export default TopCompanyCard;