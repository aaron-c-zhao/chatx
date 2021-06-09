# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, FollowupAction

import re

# class MyCustomAction(Action):
    
#     def name(self) -> Text:
#         pass
    
#     def run(self, dispatcher:CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#             pass
    
#     def __parseContent(message):
#         regex = re.compile('^@bot(.*)', re.IGNORECASE)
#         match = regex.match(message)
#         if not match:
#             return False, message
#         else:
#             return True, match.group(1)
        
        
    



class ActionConfirmFoodPreference(Action):

    def name(self) -> Text:
        return "action_confirm_food_preference"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        if tracker.slots['food']:
            dispatcher.utter_message(
                json_message={
                    "text": "So, you are looking for a restaurant at {loc} and serves {food}" \
                        .format(loc=tracker.slots['location'], food=tracker.slots['food']),
                    "type": "confirm"
                }
            )

        return []


class ActionSendQuery(Action): 
    
    def name(self) -> Text:
        return "action_send_query"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
        if tracker.slots['food']:
            dispatcher.utter_message(
                json_message={
                    "text": " \"{food}\" AND \"{loc}\"" \
                        .format(loc=tracker.slots['location'], food=tracker.slots['food']),
                    "type": "result"
                }
            )

        return [AllSlotsReset()]
    

class ActionMonitorGroupChat(Action):
    def name(self) -> Text:
        return "action_monitor_groupchat"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            if not tracker.slots['food'] and not tracker.slots['location']:
                return [FollowupAction(name= 'utter_ignore')] 
            else:
                return []