# -*- coding=utf-8 -*-

import common as cm
import pandas as pd

from factors import Factor
from dataclasses import dataclass


@dataclass
class BIAS36Factor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        用来衡量不同的移动平均价间的差距
        """
        n = para[0]

        data["36"] = cm.ma(data, N=3) - cm.ma(data, N=6)
        data[self.name] = cm.ma(data, "36", n)

        data = data.drop(columns=["36"])

        return data
