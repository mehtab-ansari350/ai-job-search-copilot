"""
Job Search Agent
"""

from providers.provider_factory import get_provider


def search_jobs():

    provider = get_provider()

    return provider.get_jobs()