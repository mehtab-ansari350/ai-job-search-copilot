"""
Base Job Provider
"""

from abc import ABC, abstractmethod


class BaseJobProvider(ABC):

    @abstractmethod
    def get_jobs(self):
        """
        Return a list of jobs.
        """
        pass