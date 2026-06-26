from graph.builder import graph

initial_state = {
    "job_description": (
        "AI Engineer with Python, FastAPI, Docker, "
        "AWS, Kubernetes and LangChain"
    )
}

result = graph.invoke(initial_state)

print("\nFINAL RESULT\n")
print(result)