# -*- coding=utf-8 -*-


import pandas as pd
from factors import Factor
from dataclasses import dataclass


@dataclass
class ARRONDOWNFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        ArronDown 为考虑的时间段内最低价出现时间与当前时间的距离占时间段长度的百分比
        """
        n = para[0]

        data["low-len"] = (
            data["low"].rolling(n).apply(lambda z: n - (z.idxmin() + 1) % 10)
        )
        data[self.name] = 100 * (n - data["low-len"]) / n

        data = data.drop(columns=["low-len"])

        return data
