from abc import ABCMeta, abstractmethod
from .target import Target


class OsOpenable(Target, metaclass=ABCMeta):  # pragma: no cover
    """ Anything that can be sent to open/xdg-open. """

    @property
    @abstractmethod
    def file_or_url(self) -> str:
        ...
