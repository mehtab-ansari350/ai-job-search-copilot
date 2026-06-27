"""
Static Job Provider
"""

from providers.base_provider import BaseJobProvider


class StaticJobProvider(BaseJobProvider):

    def get_jobs(self):

        return [
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