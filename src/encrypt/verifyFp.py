from random import random
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits
from time import time

from rich import print

__all__ = ["VerifyFp", ]


class VerifyFp:
    """代码参考: https://github.com/Johnserf-Seed/f2/blob/main/f2/apps/douyin/utils.py"""

    @staticmethod
    def get_verify_fp(timestamp: int = None):
        base_str = digits + ascii_uppercase + ascii_lowercase
        t = len(base_str)
        milliseconds = timestamp or int(round(time() * 1000))
        base36 = ""

        # 转换为 base36
        while milliseconds > 0:
            milliseconds, remainder = divmod(milliseconds, 36)
            if remainder < 10:
                base36 = str(remainder) + base36
            else:
                base36 = chr(ord("a") + remainder - 10) + base36

        # 设置固定字符
        o = [""] * 36
        o[8] = o[13] = o[18] = o[23] = "_"
        o[14] = "4"

        # 随机填充缺失的字符
        for i in range(36):
            if not o[i]:
                n = int(random() * t)  # 优化随机数生成方式
                if i == 19:
                    n = 3 & n | 8
                o[i] = base_str[n]

        # 组合最终字符串
        return "verify_" + base36 + "_" + "".join(o)


if __name__ == "__main__":
    params = 1710413848097
    print(VerifyFp.get_verify_fp(params))
