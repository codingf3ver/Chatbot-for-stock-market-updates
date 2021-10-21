# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

from rasa_sdk.interfaces import Action
import requests
from rasa_sdk.executor import CollectingDispatcher
#

url = "https://nse-data1.p.rapidapi.com/market_status"

class NseStockInfo(Action):
    
    def name(self) :
         return "action_nse_stock_price"

    def run(self, dispatcher, tracker, domain) :
        headers = {
        'x-rapidapi-host': "nse-data1.p.rapidapi.com",
        'x-rapidapi-key': "YOUR_API_KEY"
        }   

        response = requests.request("GET", url, headers=headers)
        response_json = response.json()
        share_info = response_json['body'][ 'marketState']

        for i in range(len(share_info)):
            market = share_info[i]['market']
            market_status = share_info[i]['marketStatus'].strip()
            trade_date = share_info[i]['tradeDate']
            last_closed = share_info[i]['last']
            changes = share_info[i]['variation']
            
        
            output = f'Market: {market} , Status : {market_status} ,Trade Date: {trade_date}, Last Closed : {last_closed},Variation: {changes}\n'

            dispatcher.utter_message(text = output)

        return []
