from key_config import api_key, api_secret
from binance.client import Client
import time
from tradingview_ta import TA_Handler, Interval, Exchange

SYMBOL = "BTCUSDT"
INTERVAL = Interval.INTERVAL_5_MINUTES
QNTY = 0.001

client = Client(api_key, api_secret)

def get_data():
    output = TA_Handler(symbol=SYMBOL,
                    screener='Crypto',
                    exchange='Binance',
                    interval=INTERVAL)

    activity = output.get_analysis().summary
    return activity


def place_order(order_type):
    if(order_type == 'BUY'):
        order = client.create_order(symbol=SYMBOL, side=order_type, type='MARKET', quantity=QNTY)
        print(order)
    if (order_type == 'SELL'):
        order = client.create_order(symbol=SYMBOL, side=order_type, type='MARKET', quantity=QNTY)
        print(order)



def main():
    buy = False
    sell = True
    print('script running')
    while True:
        data = get_data()
        print(data)
        if(data['RECOMMENDATION'] == 'STRONG BUY' and not buy):
            print('---BUY---')
            place_order('BUY')
            buy = not buy
            sell = not sell

        if(data['RECOMMENDATION'] == 'STRONG_SELL' and not sell):
            print('---SELL---')
            place_order('SELL')
            buy = not buy
            sell = not sell


        time.sleep(1)


if __name__ == '__main__':
    main()




