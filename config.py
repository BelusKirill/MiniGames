from dataclasses import dataclass
from typing import List


@dataclass
class TgBot:
    token: str
    admin_ids: List[int]


@dataclass
class Config:
    tg_bot: TgBot


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
        )
    )