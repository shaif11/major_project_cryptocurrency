import tkinter as tk
import logging

from connectors.binance_futures import BinanceFuturesClient


logger = logging.getLogger()


logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)
file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
if __name__ == '__main__':

   binance = BinanceFuturesClient(True)
   print(binance.get_balances())
   print(binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", 2000, "GTC"))
   print(binance.get_order_status("BTCUSDT", 2612334776))

   root = tk.Tk()
   root.mainloop()

    # jcjdjcvnhfjvfj
