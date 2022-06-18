import requests
import xmltodict


class Transformer:
    """Класс для подготовки данных к загрузке в БД"""
    DOLLAR_RATE = 0

    def __init__(self, data: list, currency_position: int):
        self.data = data
        self.currency_position = currency_position

    @staticmethod
    def __get_currency_rate() -> dict:
        """Получение курса валют с сайта ЦБ"""
        result = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?VAL_NM_RQ=R01235')
        result_dict = xmltodict.parse(result.content).get('ValCurs')
        return result_dict.get('Valute')

    @classmethod
    def __get_dollar_rate(cls) -> float:
        """Получение курса доллара из списка курса всех валют"""
        for currency in cls.__get_currency_rate():
            if currency.get('CharCode') == 'USD':
                cls.DOLLAR_RATE = float(currency.get('Value').replace(',', '.'))
                break

    def transform_data(self):
        """Добавление в данные стоимости в рублях"""
        self.__get_dollar_rate()

        for row in self.data:
            row.append(
                round(
                    float(row[self.currency_position]) * Transformer.DOLLAR_RATE,
                    2)
            )
