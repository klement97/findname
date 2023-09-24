import abc


class UseCasePort(abc.ABC):

    @abc.abstractmethod
    async def execute(self, *args, **kwargs): ...
