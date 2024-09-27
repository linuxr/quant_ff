# -*- coding=utf-8 -*-

import quant_ff.common as cm
import pandas as pd

from quant_ff.factors import Factor
from dataclasses import dataclass


@dataclass
class MAAMTFactor(Factor):
    def signal(self, data: pd.DataFrame, para: list):
        """
        成交额的移动平均线
        """
        n = para[0]

        data[self.name] = cm.ma(data, "quote_volume", n)

        return data
