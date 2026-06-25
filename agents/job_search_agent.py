"""
Job Search Agent
"""

jobs_database = [
    {
        "title": "AI Engineer",
        "company": "Infosys",
        "location": "Bangalore",
        "skills": [
            "Python",
            "FastAPI",
            "Docker",
            "AWS",
            "LLMs"
        ]
    },
    {
        "title": "Generative AI Engineer",
        "company": "TCS",
        "location": "Hyderabad",
        "skills": [
            "Python",
            "LangChain",
            "RAG",
            "LLMs"
        ]
    },
    {
        "title": "Machine Learning Engineer",
        "company": "Wipro",
        "location": "Pune",
        "skills": [
            "Python",
            "TensorFlow",
            "Docker"
        ]
    }
]


def search_jobs():
    return jobs_database