# -*- coding=utf-8 -*-

from quant_ff.factors.factor import Factor
from quant_ff.factors.adosc import ADOSCFactor
from quant_ff.factors.adtm import ADTMFactor
from quant_ff.factors.adx import ADXFactor
from quant_ff.factors.adxr import ADXRFactor
from quant_ff.factors.amv import AMVFactor
from quant_ff.factors.apz import APZFactor
from quant_ff.factors.ar import ARFactor
from quant_ff.factors.arrondown import ARRONDOWNFactor
from quant_ff.factors.arronup import ARRONUPFactor
from quant_ff.factors.asi import ASIFactor
from quant_ff.factors.atr import ATRFactor
from quant_ff.factors.aws import AWSFactor

from quant_ff.factors.bbi import BBIFactor
from quant_ff.factors.bias import BIASFactor
from quant_ff.factors.bias36 import BIAS36Factor
from quant_ff.factors.biasvol import BIASVOLFactor
from quant_ff.factors.bop import BOPFactor
from quant_ff.factors.br import BRFactor

from quant_ff.factors.cci import CCIFactor
from quant_ff.factors.clv import CLVFactor
from quant_ff.factors.cmf import CMFFactor
from quant_ff.factors.cmo import CMOFactor
from quant_ff.factors.copp import COPPFactor
from quant_ff.factors.cr import CRFactor
from quant_ff.factors.cv import CVFactor

from quant_ff.factors.dbcd import DBCDFactor
from quant_ff.factors.dc import DCFactor
from quant_ff.factors.ddi import DDIFactor
from quant_ff.factors.dema import DEMAFactor
from quant_ff.factors.demakder import DemakderFactor
from quant_ff.factors.dma import DMAFactor
from quant_ff.factors.do import DOFactor
from quant_ff.factors.dpo import DPOFactor
from quant_ff.factors.dzcci import DZCCIFactor
from quant_ff.factors.dzrsi import DZRSIFactor

all = ["Factor"]


def get_factor(name: str) -> Factor:
    match name.upper():
        case "ADOSC":
            return ADOSCFactor(name=name.upper())
        case "ADTM":
            return ADTMFactor(name=name.upper())
        case "ADX":
            return ADXFactor(name=name.upper())
        case "ADXR":
            return ADXRFactor(name=name.upper())
        case "AMV":
            return AMVFactor(name=name.upper())
        case "APZ":
            return APZFactor(name=name.upper())
        case "AR":
            return ARFactor(name=name.upper())
        case "ARRONDOWN":
            return ARRONDOWNFactor(name=name.upper())
        case "ARRONUP":
            return ARRONUPFactor(name=name.upper())
        case "ASI":
            return ASIFactor(name=name.upper())
        case "ATR":
            return ATRFactor(name=name.upper())
        case "AWS":
            return AWSFactor(name=name.upper())
        case "BBI":
            return BBIFactor(name=name.upper())
        case "BIAS":
            return BIASFactor(name=name.upper())
        case "BIAS36":
            return BIAS36Factor(name=name.upper())
        case "BIASVOL":
            return BIASVOLFactor(name=name.upper())
        case "BOP":
            return BOPFactor(name=name.upper())
        case "BR":
            return BRFactor(name=name.upper())
        case "CCI":
            return CCIFactor(name=name.upper())
        case "CLV":
            return CLVFactor(name=name.upper())
        case "CMF":
            return CMFFactor(name=name.upper())
        case "CMO":
            return CMOFactor(name=name.upper())
        case "COPP":
            return COPPFactor(name=name.upper())
        case "CR":
            return CRFactor(name=name.upper())
        case "CV":
            return CVFactor(name=name.upper())
        case "DBCD":
            return DBCDFactor(name=name.upper())
        case "DC":
            return DCFactor(name=name.upper())
        case "DDI":
            return DDIFactor(name=name.upper())
        case "DEMA":
            return DEMAFactor(name=name.upper())
        case "DEMAKDER":
            return DemakderFactor(name=name.upper())
        case "DMA":
            return DMAFactor(name=name.upper())
        case "DO":
            return DOFactor(name=name.upper())
        case "DPO":
            return DPOFactor(name=name.upper())
        case "DZCCI":
            return DZCCIFactor(name=name.upper())
        case "DZRSI":
            return DZRSIFactor(name=name.upper())
        case _:
            return Factor(name=name.upper())
