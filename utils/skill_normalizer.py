"""
Skill Normalizer
"""

import re 

NORMALIZATION = {

    # -------- LLM --------
    "llm": "LLMs",
    "llms": "LLMs",
    "large language model": "LLMs",
    "large language models": "LLMs",
    "large language models (llms)": "LLMs",
    "large language models(llms)": "LLMs",

    # -------- RAG --------
    "rag": "RAG",
    "retrieval augmented generation": "RAG",
    "retrieval-augmented generation": "RAG",
    "retrieval augmented generation (rag)": "RAG",
    "retrieval-augmented generation (rag)": "RAG",

    # -------- Prompt Engineering --------
    "prompt engineering": "Prompt Engineering",
    "prompt engineer": "Prompt Engineering",

    # -------- NLP --------
    "nlp": "NLP",
    "natural language processing": "NLP",
    "naturallanguage processing (nlp)": "NLP",
    "natural language processing (nlp)": "NLP",

    # -------- GenAI --------
    "gen ai": "Generative AI",
    "genai": "Generative AI",
    "generative ai": "Generative AI",

    # -------- ML --------
    "machine learning": "Machine Learning",
    "ml": "Machine Learning",

    # -------- APIs --------
    "rest api": "REST APIs",
    "rest apis": "REST APIs",

    # -------- CV --------
    "computer vision": "Computer Vision",

    # -------- Azure --------
    "azure": "Microsoft Azure",

    # -------- LangChain --------
    "langchain": "LangChain",

    # -------- FastAPI --------
    "fastapi": "FastAPI",

    # -------- Docker --------
    "docker": "Docker",

    # -------- Python --------
    "python": "Python",
}


import re

def normalize(skills):

    normalized = []

    for skill in skills:

        s = skill.lower().strip()

        # remove duplicate spaces
        s = re.sub(r"\s+", " ", s)

        normalized.append(
            NORMALIZATION.get(s, skill.strip())
        )

    return list(set(normalized))