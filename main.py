import os
import time
import telebot
import yfinance as yf
import MetaTrader5 as mt5
from dotenv import load_dotenv
load_dotenv()

API_KEY=os.getenv("MY_SECRET_KEY")
if not mt5.initialize():
     print("initialize() failed, error code =",mt5.last_error())
     quit()
print("Hit")
bot=telebot.TeleBot(API_KEY)
print("Hit")


def BuyRequest(message):
     request=message=message.text.split()
     print(str(request))
     if request[0]=='Buy' or request[0]=='Sell':
         print(request[0])
         print("Checked out ")
         return True
         
     else:
         print("Dint check out")
         return False
 
def BuyOrder(symbol,lots):
     print("Buy Order Hit")
     lot = float(lots)
     point = mt5.symbol_info(symbol).point
     price = mt5.symbol_info_tick(symbol).ask
     print(price)
     deviation = 20
     request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "tp":price+270.24,
        "sl":price-270.24,
        "deviation": deviation,
        "magic": 234000,
        "comment": "python script open",
        "type_time": mt5.ORDER_TIME_GTC,}
        
     result=mt5.order_send(request) 
     print(result)
     return True
 
@bot.message_handler(func=BuyRequest)
def ExecuteBuy(message):
     symbol=message.text.split()[2]
     ordertype=message.text.split()[0]
     lots=message.text.split()[1]
     index=0
     
     for x in message.text:
         if x==symbol[0]:
             index=message.text.find(x)
             symbol=message.text
             symbol=symbol[index:]
             
             print(index)
     print(str(ordertype))
     print("Hit Order processing")
     print(symbol)
     symbol_info = mt5.symbol_info(symbol)
     time.sleep(10)
     print(symbol_info)
     if mt5.symbol_select(symbol):
         if ordertype=='Buy':
             if(BuyOrder(symbol,lots)):
                 print("Hit Buy succeed")
                 bot.send_message(message.chat.id,"Order executed")
         elif ordertype=='Sell':
             if(SellOrder(symbol,lots)):
                 print("Hit Sell succeed")
                 bot.send_message(message.chat.id,"Order executed")
                   
         else:
             bot.send_message(message.chat.id,"Symbol not found")
     else:
         bot.send_message(message.chat.id,"Symbol not found")
         print("Hit Buy failed")
        


bot.polling()

