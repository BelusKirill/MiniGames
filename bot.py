import logging

from datetime import datetime
from aiogram.types import BotCommand

logger = logging.getLogger(__name__)


def register_all_filters(dispatcher):
    """
    Функция регистрации фильтров телеграм бота
    Возвращает: None
    """


def register_all_handlers(dp):
    """
    Функция регистрации обработчиков телеграм бота
    Возвращает: None
    """
    from tgbot.handlers.user import register_user

    register_user(dp)


async def on_startup(dispatcher):
    """
    Функция выполняемая перед запуском бота. Настройка логов,
    регистрация обработчиков и фильтров
    Возвращает: None
    """ 
    logging.basicConfig(
        level=logging.DEBUG,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info(f"Starting bot {datetime.now()}")
    from loader import db
    if await db.create_pool():
        await db.create_users_table()
        register_all_filters(dispatcher)
        register_all_handlers(dispatcher)
        await dispatcher.bot.set_my_commands([
            BotCommand('start', 'Перезапустить 🔄'),
            BotCommand('rsp', 'Камень, ножницы, бумага 🪨✂️📄')
        ])
        logger.info(f'Вeрсия postgrest: {await db.get_vdb()}')


async def on_shutdown(dispatcher):
    """
    Функция завершения бота
    Возвращает: None
    """
    from loader import db
    logging.warning('Shutting down..')
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

    logging.warning('Bye!')
    await dispatcher.bot.close()
    await db.close()


if __name__ == '__main__':
    from aiogram.utils import executor
    from loader import dp

    executor.start_polling(dp, skip_updates=True,
                        on_startup=on_startup, on_shutdown=on_shutdown)    