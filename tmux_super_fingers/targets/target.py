from abc import ABCMeta, abstractmethod


class Target(metaclass=ABCMeta):  # pragma: no cover
    @abstractmethod
    def perform_primary_action(self) -> None:
        ...
