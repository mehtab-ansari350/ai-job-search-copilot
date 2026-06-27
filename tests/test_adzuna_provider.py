from providers.adzuna_provider import AdzunaProvider


provider = AdzunaProvider()

jobs = provider.get_jobs()

print()

print(f"Found {len(jobs)} jobs")

print()

for job in jobs[:5]:
    print(job)