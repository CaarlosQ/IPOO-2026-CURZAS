from abc import ABC, abstractmethod


class ConfirmableInterface(ABC):

    @abstractmethod
    def confirmar_lectura(self):
        pass