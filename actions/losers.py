import json
from typing import Any, Text, Dict, List
from rasa_sdk.interfaces import Action
import requests
from rasa_sdk.executor import CollectingDispatcher
#

url = "https://nse-data1.p.rapidapi.com/market_status"

class NseTopLosers(Action):
    
    def name(self) :
         return "action_nse_top_losers"

    def run(self, dispatcher, tracker, domain) :
        url = "https://nse-data1.p.rapidapi.com/top_loosers"

        headers = {
            'x-rapidapi-host': "nse-data1.p.rapidapi.com",
            'x-rapidapi-key': "YOUR_API_KEY"
            }

        response = requests.request("GET", url, headers=headers)
        losers = response.json()
        nifty_top_losers = losers['body']['FOSec']['data']
        for i in range(len(nifty_top_losers)):
            ntl = nifty_top_losers 
            entity_name = ntl[i]['symbol']
            open_price = ntl[i]['open_price']
            low_price = ntl[i]['low_price']
            high_price = ntl[i]['high_price']
            change_percent = ntl[i]['perChange']
            output = f'Entity = {entity_name}, Opening = {open_price}, lowest = {low_price}, Highest = {high_price}, percentChange = {change_percent}\n'
            dispatcher.utter_message(text = output)

        return []