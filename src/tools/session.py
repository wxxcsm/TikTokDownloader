from typing import TYPE_CHECKING
from typing import Union

from httpx import AsyncClient
from httpx import Client
from httpx import Limits

from src.custom import MAX_WORKERS
from src.custom import TIMEOUT
from src.custom import USERAGENT
from src.tools import TikTokDownloaderError
from .capture import capture_error_params
from .retry import PrivateRetry

if TYPE_CHECKING:
    from src.record import BaseLogger
    from src.record import LoggerManager
    from src.testers import Logger

__all__ = ["request_params", "create_client"]


def create_client(
        user_agent=USERAGENT,
        timeout=TIMEOUT,
        headers: dict = None,
        max_connections=MAX_WORKERS,
        *args,
        **kwargs,
) -> AsyncClient:
    return AsyncClient(
        headers=headers or {"User-Agent": user_agent, },
        timeout=timeout,
        follow_redirects=True,
        verify=False,
        limits=Limits(max_connections=max_connections),
        *args,
        **kwargs,
    )


async def request_params(
        logger: Union["BaseLogger", "LoggerManager", "Logger",],
        url: str,
        method: str = "POST",
        params: dict | str = None,
        data: dict | str = None,
        useragent=USERAGENT,
        timeout=TIMEOUT,
        headers: dict = None,
        resp="headers",
        proxy: str = None,
        proxies: dict = None,
        **kwargs,
):
    with Client(
            headers=headers or {
                "User-Agent": useragent,
                "Content-Type": "application/json; charset=utf-8",
                # "Referer": "https://www.douyin.com/"
            },
            follow_redirects=True,
            timeout=timeout,
            verify=False,
            proxy=proxy,
            proxies=proxies,
    ) as client:
        return await request(
            logger,
            client,
            method,
            url,
            resp,
            params=params,
            data=data,
            **kwargs,
        )


@PrivateRetry.retry_lite
@capture_error_params
async def request(logger: Union["BaseLogger", "LoggerManager", "Logger",],
                  client: Client,
                  method: str,
                  url: str,
                  resp="json",
                  **kwargs,
                  ):
    response = client.request(method, url, **kwargs)
    response.raise_for_status()
    match resp:
        case "headers":
            return response.headers
        case "text":
            return response.text
        case "content":
            return response.content
        case "json":
            return response.json()
        case "url":
            return str(response.url)
        case "response":
            return response
        case _:
            raise TikTokDownloaderError
