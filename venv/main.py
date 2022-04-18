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

   binance = BinanceFuturesClient("42da1a468b48c41f7974333ed77b22b898d81b914d2bfcc09d1f520da376a6d6cb7f9c30475b5410730640836205e3dca232f9f5115409870bd6fe30dd3add53", True)


   root = tk.Tk()
   root.mainloop()

    # jcjdjcvnhfjvfj
