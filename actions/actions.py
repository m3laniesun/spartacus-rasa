import logging
import json
import requests
import geocoder
from datetime import datetime
from typing import Any, Dict, List, Text, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    SlotSet,
    UserUtteranceReverted,
    ConversationPaused,
    EventType,
)


USER_INTENT_OUT_OF_SCOPE = "out_of_scope"

logger = logging.getLogger(__name__)


#weather stuff
weather_dict = {'freezing_rain_heavy': 'Heavy rain and snow', 'freezing_rain': 'Rain and snow outside the house', 'freezing_rain_light': 'Light rain and snow', 'freezing_drizzle': 'Light drizzle and snow', 'ice_pellets_heavy': 'Heavy ice pellets falling form the sky.', 'ice_pellets': 'Ice pellets falling from the sky.', 'ice_pellets_light': 'Light pellets falling from the sky.', 'snow_heavy': 'Heavy snow around the area.', 'snow': 'It is snowing outside.', 'snow_light': 'Light snow around the area.', 'flurries': 'Flurries', 'tstorm': 'Thunder storm around the area.', 'rain_heavy': 'Heavy rain around the area.', 'rain': 'It is raining outside.', 'rain_light': 'Light rain around the area.', 'drizzle': 'It is drizzling outside.', 'fog_light': 'Light fog around the area.', 'fog': 'Presence of fog around the area.', 'cloudy': 'It is cloudly outside.', 'mostly_cloudy': 'The sky is covered with clouds.', 'partly_cloudy': 'It is partly cloudly outside', 'mostly_clear': 'Sunny with presence of small clouds.', 'clear': 'It is clear and sunny outside.'}
url = "https://api.tomorrow.io/v4/timelines"
"""g = geocoder.ip('me')"""
querystring = {"lat":"38.8462","lon":"77.3064","unit_system":"si","fields":"temperature","apikey":"JVOO3lMW7kkGnGTg1hRR7iD4a5IDT77e"}

"""
g.lat
g.lon
"""

class ActionAskWeather(Action):
    def name(self) -> Text:
        return "action_ask_weather"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.request("GET", url, params=querystring)
        result = ""

        json_data = response.json()

        result = 'The average temperature is %s%s.' % (json_data['temperature']['value'], json_data['temperature']['units'])

        dispatcher.utter_message(text=result)

        return []