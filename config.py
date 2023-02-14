from dataclasses import dataclass
from typing import List


@dataclass
class DbConfig:
    host: str
    port: str
    password: str
    user: str
    database: str

@dataclass
class TgBot:
    token: str
    admin_ids: List[int]


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig


def load_config() -> Config:
    """
    Функция загрузки config, параметры для подключения к телеграмм
    Возвращает: Config
    """
    import configparser

    from os import getenv
    from dotenv import load_dotenv, find_dotenv

    load_dotenv(find_dotenv())
    return Config(
        tg_bot=TgBot(
            token=getenv("BOT_TOKEN"),
            admin_ids=list(map(int, getenv("ADMIN").split(",")))
        ),
        db=DbConfig(
            host=getenv('DB_HOST'),
            password=getenv('DB_PASS'),
            port=getenv('DB_PORT'),
            user=getenv('DB_USER'),
            database=getenv('DB_NAME')            
        )
    )