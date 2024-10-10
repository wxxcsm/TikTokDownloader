from asyncio import run
from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

from src.interface.collection import Collection
from src.interface.template import API
from src.testers import Params

if TYPE_CHECKING:
    from src.config import Parameter


class Collects(API):
    def __init__(self,
                 params: Union["Parameter", Params],
                 cookie: str = None,
                 proxy: str = None,
                 cursor=0,
                 count=10,
                 *args,
                 **kwargs,
                 ):
        super().__init__(params, cookie, proxy, *args, **kwargs, )
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}aweme/v1/web/collects/list/"
        self.text = "收藏夹数据"

    def generate_params(self, ) -> dict:
        return self.params | {
            "cursor": self.cursor,
            "count": self.count,
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(self,
                  referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
                  single_page=False,
                  data_key: str = "collects_list",
                  error_text="当前账号无收藏夹",
                  cursor="cursor",
                  has_more="has_more",
                  params: Callable = lambda: {},
                  data: Callable = lambda: {},
                  method="GET",
                  headers: dict = None,
                  *args,
                  **kwargs,
                  ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )


class CollectsDetail(Collection, API):
    def __init__(self,
                 params: Union["Parameter", Params],
                 cookie: str = None,
                 proxy: str = None,
                 collects_id: str = ...,
                 sec_user_id: str = None,
                 pages: int = None,
                 cursor=0,
                 count=10,
                 *args,
                 **kwargs,
                 ):
        super().__init__(params, cookie, proxy, sec_user_id, *args, **kwargs, )
        self.collects_id = collects_id
        self.pages = pages or params.max_pages
        self.api = f"{self.domain}aweme/v1/web/collects/video/list/"
        self.cursor = cursor
        self.count = count
        self.text = "收藏夹作品数据"

    def generate_params(self, ) -> dict:
        return self.params | {
            "collects_id": self.collects_id,
            "cursor": self.cursor,
            "count": self.count,
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(self,
                  referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
                  single_page=False,
                  data_key: str = "aweme_list",
                  error_text="",
                  cursor="cursor",
                  has_more="has_more",
                  params: Callable = lambda: {},
                  data: Callable = lambda: {},
                  method="GET",
                  headers: dict = None,
                  *args,
                  **kwargs,
                  ):
        await super(Collection, self).run(
            referer,
            single_page,
            data_key,
            error_text or f"收藏夹 {self.collects_id} 为空",
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )
        if self.sec_user_id:
            await self.get_owner_data()
        return self.response


class CollectsMix(API):
    def __init__(self,
                 params: Union["Parameter", Params],
                 cookie: str = None,
                 proxy: str = None,
                 cursor=0,
                 count=12,
                 *args,
                 **kwargs,
                 ):
        super().__init__(params, cookie, proxy, *args, **kwargs, )
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}aweme/v1/web/mix/listcollection/"
        self.text = "收藏合集数据"

    def generate_params(self, ) -> dict:
        return self.params | {
            "cursor": self.cursor,
            "count": self.count,
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(self,
                  referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
                  single_page=False,
                  data_key: str = "mix_infos",
                  error_text="当前账号无收藏合集",
                  cursor="cursor",
                  has_more="has_more",
                  params: Callable = lambda: {},
                  data: Callable = lambda: {},
                  method="GET",
                  headers: dict = None,
                  proxy: str = None,
                  *args,
                  **kwargs,
                  ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            proxy,
            *args,
            **kwargs,
        )


class CollectsSeries(CollectsMix):
    def __init__(self,
                 params: Union["Parameter", Params],
                 cookie: str = None,
                 proxy: str = None,
                 cursor=0,
                 count=12,
                 *args,
                 **kwargs,
                 ):
        super().__init__(params, cookie, proxy, *args, **kwargs, )
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}aweme/v1/web/series/collections/"
        self.text = "收藏短剧数据"

    async def run(self,
                  referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
                  single_page=False,
                  data_key: str = "series_infos",
                  error_text="当前账号无收藏短剧",
                  cursor="cursor",
                  has_more="has_more",
                  params: Callable = lambda: {},
                  data: Callable = lambda: {},
                  method="GET",
                  headers: dict = None,
                  *args,
                  **kwargs,
                  ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )


class CollectsMusic(CollectsMix):
    def __init__(self,
                 params: Union["Parameter", Params],
                 cookie: str = None,
                 proxy: str = None,
                 cursor=0,
                 count=20,
                 *args,
                 **kwargs,
                 ):
        super().__init__(params, cookie, proxy, *args, **kwargs, )
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}aweme/v1/web/music/listcollection/"
        self.text = "收藏音乐数据"

    async def run(self,
                  referer: str = "https://www.douyin.com/user/self?showTab=favorite_collection",
                  single_page=False,
                  data_key: str = "mc_list",
                  error_text="当前账号无收藏音乐",
                  cursor="cursor",
                  has_more="has_more",
                  params: Callable = lambda: {},
                  data: Callable = lambda: {},
                  method="GET",
                  headers: dict = None,
                  *args,
                  **kwargs,
                  ):
        return await super().run(
            referer,
            single_page,
            data_key,
            error_text,
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )


async def main():
    async with Params() as params:
        c = Collects(params, )
        print(await c.run())
        c = CollectsDetail(params, collects_id="7357880138505361191")
        print(await c.run())
        c = CollectsMix(params, )
        print(await c.run())
        c = CollectsMusic(params, )
        print(await c.run())
        c = CollectsSeries(params, )
        print(await c.run())


if __name__ == "__main__":
    run(main())
