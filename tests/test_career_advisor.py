from agents.career_advisor_agent import (
    generate_career_plan
)

result = generate_career_plan(
    [
        "AWS",
        "Kubernetes"
    ]
)

print(result)