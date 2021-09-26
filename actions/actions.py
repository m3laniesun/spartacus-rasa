import logging
import json
import requests
import datetime
from rasa_sdk.events import ReminderScheduled

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
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

USER_INTENT_OUT_OF_SCOPE = "out_of_scope"

logger = logging.getLogger(__name__)

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


class ActionFirstName(Action):

    def name(self) -> Text:
        #unique identifier of the form 

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template=utter_last_name)

        return [SlotSet('firstN',tracker.latest_message['text'])]
    

class ActionReceiveName(Action):

    def name(self) -> Text:
        return "action_receive_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
    
        text = tracker.latest_message['text']
        dispatcher.utter_message(text=f"I'll remember your name, {text}!")
        return [SlotSet("name", text)]
    
class ActionSayName(Action):

    def name(self) -> Text:
        return "action_say_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List [Dict[Text, Any]]:

        name = tracker.get_slot("name")
        if not name:
            dispatcher.utter_message(text="I don't know your name.")
        else:
            dispatcher.utter_message(text=f"your name is {name}.")
        return []

class Validate_Quiz(Action):


    def validate_quiz_11(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        if slot_value.lower() == 'b':
            print("{slot_value} is correct!")
            return {"get_point": 1}
            
        else:
            print("{slot_value} is incorrect")
            return {"get_point": 0}

class UtterMessage(Action):
    """Schedules a reminder, supplied with the last message's entities."""

    def name(self) -> Text:
        return "action_set_reminder"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dispatcher.utter_message("First message")

        date = datetime.datetime.now() + datetime.timedelta(seconds=5)
        entities = tracker.latest_message.get("entities")

       
