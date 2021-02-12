import requests
import datetime

req = requests.get('https://finnhub.io/api/v1/crypto/candle?symbol=BINANCE:BTCUSDT&resolution=D&from=1611967991&to=1612967991&token=c0htplv48v6qgpegtbk0')
req = req.json()
#print(req)

data_list = []
len = [len(v) for v in req.values()]
for i in range(len[0]):
       temp_list = []
       data_list.append(temp_list)
       for k, v in req.items():
              if k == 't':
                     temp_list.append(
                            datetime.datetime.fromtimestamp(
                                   v[i]).strftime('%Y-%m-%d %H:%M:%S')
                     )
              elif k == 'c':
                     temp_list.append('price ' + str(v[i]))
              elif k == 'v':
                     temp_list.append('volume ' + str(v[i]))

for item in data_list:
       print(item)
