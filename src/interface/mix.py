from typing import Callable
from typing import TYPE_CHECKING
from typing import Union

from src.extract import Extractor
from src.interface.detail import Detail
from src.interface.template import API
from src.testers import Params

if TYPE_CHECKING:
    from src.config import Parameter


class Mix(API):
    def __init__(self,
                 params: Union["Parameter", Params],
                 cookie: str = None,
                 proxy: str = None,
                 mix_id: str = None,
                 detail_id: str = None,
                 cursor=0,
                 count=12,
                 *args,
                 **kwargs,
                 ):
        super().__init__(params, cookie, proxy, *args, **kwargs, )
        self.mix_title = None
        self.mix_id = mix_id
        self.detail_id = detail_id
        self.count = count
        self.cursor = cursor
        self.api = f"{self.domain}aweme/v1/web/mix/aweme/"
        self.text = "合集作品数据"
        self.detail = Detail(params, cookie, proxy, self.detail_id, )

    def generate_params(self, ) -> dict:
        return self.params | {
            "mix_id": self.mix_id,
            "cursor": self.cursor,
            "count": self.count,
            "version_code": "170400",
            "version_name": "17.4.0",
        }

    async def run(self,
                  referer: str = None,
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
        await self.__get_mix_id()
        if not self.mix_id:
            self.log.warning("获取合集 ID 失败")
            return self.response
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

    async def __get_mix_id(self):
        if not self.mix_id:
            self.mix_id = Extractor.extract_mix_id(await self.detail.run())
