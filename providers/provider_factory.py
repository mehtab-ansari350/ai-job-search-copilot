"""
Provider Factory
"""

import os

from providers.static_provider import StaticJobProvider
from providers.adzuna_provider import AdzunaProvider


def get_provider():

    provider = os.getenv("JOB_PROVIDER", "static")

    if provider == "adzuna":
        return AdzunaProvider()

    return StaticJobProvider()