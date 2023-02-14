import asyncio
import logging
from typing import Union, Optional

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

logger = logging.getLogger(__name__)


class Database:
    """
    Класс для работы с db
    """
    def __init__(self, username: str, password: str, host: str, database: str, port: str,
                 loop: Optional[Union[asyncio.BaseEventLoop, asyncio.AbstractEventLoop]] = None):
        self._main_loop = loop
        self.pool: Union[Pool, None] = None
        self._pool: Union[Pool, None] = None
        self._username = username
        self._password = password
        self._host = host
        self._database = database
        self._port = port

    async def create_pool(self) -> Pool:
        """
        Функция создает pool
        Возвращает: Pool
        """
        self._pool = await asyncpg.create_pool(user=self._username,
                                               password=self._password,
                                               host=self._host,
                                               database=self._database,
                                               port=self._port,
                                               min_size=20,
                                               max_size=40
                                               )
        logger.info("Создан pool асинхронных подключений")
        return self._pool

    @property
    def loop(self) -> Optional[asyncio.AbstractEventLoop]:
        return self._main_loop

    async def get_pool(self) -> Pool:
        """
        Функция возвращает pool, создает pool если еще не создан 
        Возвращает: Pool
        """
        if self._pool is None: self._pool = await self.create_pool()
        if not self._pool._loop.is_running():
            logger.info("Pool не работает в цикле")
            await self._pool.close()
            self._pool = await self.create_pool()
        return self._pool

    async def close(self):
        """
        Функция закрывает соединение (pool)
        Возвращает: None
        """
        if self._pool: await self._pool.close() 

    async def execute(self, command, *args, fetch: bool = False, fetchval: bool = False, fetchrow: bool = False,
                      execute: bool = False):
        """
        Функция оаределяет параметры выполение запроса и вылняет его        
        Возвращает: Coroutine
        """
        if self._pool is None: await self.get_pool()
        async with self._pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
                return result 

    async def get_vdb(self):
        """
        Функция возвращает версию db
        Возвращает: Coroutine
        """
        sql = "SELECT version()"
        return await self.execute(sql, fetchval=True)  