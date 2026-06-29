import { FaAward, FaBuilding, FaBullseye } from "react-icons/fa";
import ATSCard from "./ATSCard";
import BestMatchCard from "./BestMatchCard";
import TopCompanyCard from "./TopCompanyCard";

function DashboardSummary({ result }) {
    return (
        <div className="mt-10">

            <h2 className="text-2xl font-bold mb-6">
                Resume Analysis
            </h2>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-6">

                {/* ATS */}

                <ATSCard score={result.ats_report.ats_score} />

                {/* Match */}

                <BestMatchCard
                    score={result.ranked_jobs[0].match_score}
                />

                {/* Company */}

                <TopCompanyCard
                    company={result.ranked_jobs[0].company}
                    title={result.ranked_jobs[0].title}
                />
            </div>

        </div>
    );
}

export default DashboardSummary;