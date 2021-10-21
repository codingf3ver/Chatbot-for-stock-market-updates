import json
from typing import Any, Text, Dict, List
from rasa_sdk.interfaces import Action
import requests
from rasa_sdk.executor import CollectingDispatcher
#

url = "https://nse-data1.p.rapidapi.com/market_status"

class NseTopGainers(Action):
    
    def name(self) :
         return "action_nse_top_gainers"

    def run(self, dispatcher, tracker, domain) :
        url = "https://nse-data1.p.rapidapi.com/top_gainers"

        headers = {
        'x-rapidapi-host': "nse-data1.p.rapidapi.com",
        'x-rapidapi-key': "YOUR_API_KEY"
        }

        response = requests.request("GET", url, headers=headers)
        gainers = response.json()
        nifty_top_gainers = gainers['body']['BANKNIFTY']['data']
        for i in range(len(nifty_top_gainers)):
            ntg = nifty_top_gainers 
            entity_name = ntg[i]['symbol']
            open_price = ntg[i]['open_price']
            low_price = ntg[i]['low_price']
            high_price = ntg[i]['high_price']
            change_percent = ntg[i]['perChange']
            output = f'Entity = {entity_name}, Opening = {open_price}, lowest = {low_price}, Highest = {high_price}, percentChange = {change_percent}\n'
            dispatcher.utter_message(text = output)

        return []