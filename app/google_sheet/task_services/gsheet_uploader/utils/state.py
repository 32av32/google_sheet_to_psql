import abc
import json
from typing import Any, Optional


class BaseStorage:
    @abc.abstractmethod
    def save_state(self, state: dict) -> None:
        """Сохранить состояние в постоянное хранилище"""
        pass

    @abc.abstractmethod
    def retrieve_state(self) -> dict:
        """Загрузить состояние локально из постоянного хранилища"""
        pass


class JsonFileStorage(BaseStorage):
    """
    Класс для хранения состояния в формате JSON
    """
    def __init__(self, file_path: Optional[str] = None):
        self.file_path = file_path

    def save_state(self, state: dict) -> None:
        """Сохранить состояние в постоянное хранилище"""
        with open(self.file_path, 'w') as file_object:
            json.dump(state, file_object)

    def retrieve_state(self) -> dict:
        """Загрузить состояние локально из постоянного хранилища"""
        try:
            with open(self.file_path, 'r') as file_object:
                return json.load(file_object)
        except FileNotFoundError:
            return {}


class State:
    """
    Класс для хранения состояния при работе с данными, чтобы постоянно не перечитывать данные с начала.
    """

    def __init__(self, storage: BaseStorage):
        self.__storage = storage
        self.__state = self.__storage.retrieve_state()

    def set_state(self, key: str, value: Any) -> None:
        """Установить состояние для определённого ключа"""
        self.__state[key] = value
        self.__storage.save_state(self.__state)

    def get_state(self, key: str) -> Any:
        """Получить состояние по определённому ключу"""
        return self.__state.get(key)
