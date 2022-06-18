from datetime import datetime
from os import environ

import telebot
import psycopg2

from dotenv import load_dotenv


load_dotenv()
dsn = {
    'dbname': environ.get('DB_NAME'),
    'user': environ.get('DB_USER'),
    'password': environ.get('DB_PASSWORD'),
    'host': environ.get('DB_HOST', 'localhost'),
    'port': environ.get('DB_PORT', 5432),
}

TELEGRAM_TOKEN = environ.get('TELEGRAMBOT_TOKEN')
CHAT_ID = environ.get('TELEGRAM_CHAT_ID')

QUERY = """
SELECT order_num FROM google_sheet_order
WHERE delivery_time < '{term}';
""".format(term=datetime.now().strftime('%Y-%m-%d'))


def get_order_num():
    with psycopg2.connect(**dsn) as conn:
        with conn.cursor() as cur:
            cur.execute(QUERY)
            return '\n'.join([row[0] for row in cur.fetchall()])


def send_message():
    order_numbers = get_order_num()
    if order_numbers:
        message = f'У следующих заказов срок доставки истек:\n{order_numbers}'
        telegram_bot = telebot.TeleBot(TELEGRAM_TOKEN)
        telegram_bot.send_message(CHAT_ID, message)
