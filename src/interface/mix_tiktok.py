from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

from src.interface.template import APITikTok
from src.testers import Params

if TYPE_CHECKING:
    from src.config import Parameter


class MixTikTok(APITikTok):
    def __init__(self,
                 params: Union["Parameter", Params],
                 cookie: str = None,
                 proxy: str = None,
                 mix_title: str = ...,
                 mix_id: str = ...,
                 # detail_id: str = None,
                 cursor=0,
                 count=30,
                 *args,
                 **kwargs,
                 ):
        super().__init__(params, cookie, proxy, *args, **kwargs, )
        self.mix_title = mix_title
        self.mix_id = mix_id
        # self.detail_id = detail_id  # 未使用
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}api/mix/item_list/"
        self.text = "合辑作品数据"

    def generate_params(self, ) -> dict:
        return self.params | {
            "count": self.count,
            "cursor": self.cursor,
            "mixId": self.mix_id,
        }

    async def run(self,
                  referer: str = None,
                  single_page=False,
                  data_key: str = "itemList",
                  error_text="",
                  cursor="cursor",
                  has_more="hasMore",
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
            error_text or f"获取{self.text}失败",
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )


class MixListTikTok(APITikTok):
    def __init__(self,
                 params: Union["Parameter", Params],
                 cookie: str = None,
                 proxy: str = None,
                 sec_user_id: str = "",
                 cursor=0,
                 count=20,
                 *args,
                 **kwargs,
                 ):
        super().__init__(params, cookie, proxy, *args, **kwargs, )
        self.sec_user_id = sec_user_id
        self.cursor = cursor
        self.count = count
        self.api = f"{self.domain}api/user/playlist/"
        self.text = "账号合辑数据"

    def generate_params(self, ) -> dict:
        return self.params | {
            "count": self.count,
            "cursor": self.cursor,
            "secUid": self.sec_user_id,
        }

    async def run(self,
                  referer: str = None,
                  single_page=False,
                  data_key: str = "playList",
                  error_text="",
                  cursor="cursor",
                  has_more="hasMore",
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
            error_text or f"获取{self.text}失败",
            cursor,
            has_more,
            params,
            data,
            method,
            headers,
            *args,
            **kwargs,
        )
