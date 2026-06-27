from graph.builder import graph

initial_state = {
    "job_description": (
        "AI Engineer with Python, FastAPI, Docker, "
        "AWS, Kubernetes and LangChain"
    )
}

result = graph.invoke(initial_state)

print("\nFINAL RESULT\n")
print("\n==============================")
print("ATS REPORT")
print("==============================")

print("ATS Score:", result["ats_report"]["ats_score"])

print("\nMatched Keywords")
print(result["ats_report"]["matched_keywords"])

print("\nMissing Keywords")
print(result["ats_report"]["missing_keywords"])

print("\nStrengths")
for item in result["ats_report"]["strengths"]:
    print("-", item)

print("\nWeaknesses")
for item in result["ats_report"]["weaknesses"]:
    print("-", item)

print("\nSuggestions")
for item in result["ats_report"]["suggestions"]:
    print("-", item)

print("\n")
print("=" * 30)
print("RESUME OPTIMIZER")
print("=" * 30)

print(result["resume_optimization"])

print()
print("=" * 30)
print("COVER LETTER")
print("=" * 30)
print(result["cover_letter"])