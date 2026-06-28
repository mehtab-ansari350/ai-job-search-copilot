import JobCard from "./JobCard";

function JobList({ jobs }) {
  return (
    <div className="mt-12">

      <h2 className="text-3xl font-bold mb-6">
        Top Matching Jobs
      </h2>

      <div className="space-y-4">

        {jobs.slice(0, 5).map((job, index) => (
          <JobCard
            key={index}
            job={job}
          />
        ))}

      </div>

    </div>
  );
}

export default JobList;