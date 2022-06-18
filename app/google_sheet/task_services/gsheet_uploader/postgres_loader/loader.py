from psycopg2.extensions import connection, cursor
from psycopg2.extras import execute_batch


class PostgresLoader:
    """Класс для загрузки и обновления данных из списка в Postgresql"""
    PAGE_SIZE = 100
    QUERY_INSERT = """INSERT INTO google_sheet_order (num, order_num, price, delivery_time, price_rouble)
             VALUES (%s, %s, %s, TO_DATE(%s, 'DD.MM.YYYY'), %s)
            ON CONFLICT (order_num) DO UPDATE SET order_num = EXCLUDED.order_num,
            num = EXCLUDED.num,
            price = EXCLUDED.price,
            delivery_time = EXCLUDED.delivery_time,
            price_rouble = EXCLUDED.price_rouble;"""

    QUERY_DELETE = """DELETE FROM google_sheet_order WHERE order_num NOT IN
                      {values_tuple}"""

    def __init__(self, conn: connection, data: list):
        self.conn = conn
        self.data = data

    def upload_data(self, unique_column_pos: int):
        """Обновление данных в БД"""
        with self.conn.cursor() as cur:
            self.update_data(cur)
            self.delete_missing_data(cur, unique_column_pos)

    def update_data(self, cur: cursor):
        """Добавление данных из БД на основе списка"""
        execute_batch(cur, PostgresLoader.QUERY_INSERT, self.data, PostgresLoader.PAGE_SIZE)

    def delete_missing_data(self, cur: cursor, unique_column_pos: int):
        """Удаление данных из БД на основе списка"""
        unique_values = tuple([row[unique_column_pos] for row in self.data])
        cur.execute(PostgresLoader.QUERY_DELETE.format(values_tuple=unique_values))

