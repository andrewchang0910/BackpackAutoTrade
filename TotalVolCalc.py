#coding=utf-8

from pprint import pprint

from bpx.bpx import *
from bpx.bpx_pub import *
import time
from dotenv import load_dotenv
import os

load_dotenv()
run_pair = 'SOL'
pair_name = 'SOL_USDC'
pair_accuracy = 2  # 交易對價格精度
# 讀取環境變數
api_secret = os.getenv('API_SECRET')
api_key = os.getenv('API_KEY')
wish_vol = int(os.getenv('WISH_VOLUME'))
bpx = BpxClient()
bpx.init(
    api_key=api_key,
    api_secret=api_secret,
)
wish_vol = wish_vol  # 期望刷的量，單位 USDC


volSum = 0
feeSum = 0
hisOrder = bpx.fillHistoryQuery(pair_name, 100, 0)
index = 100
while len(hisOrder) == 100:
    for order in hisOrder:
        # print(order)
        if order['feeSymbol'] == "USDC":
            feeSum += float(order['fee'])
        else:
            feeSum += float(order['fee']) * float(order['price'])
        volSum += float(order['price']) * float(order['quantity'])
    hisOrder = bpx.fillHistoryQuery(pair_name, 100, index)
    print(f"截取第{index}筆資料")
    index += 100
print(f"當前幣種累計成交量: {volSum} USDC")
print(f"當前幣種累計手續費: {feeSum} USDC")