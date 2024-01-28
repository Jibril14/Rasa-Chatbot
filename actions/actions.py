# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ExtractIphoneEntity(Action):

    def name(self) -> Text:
        return "action_extract_iphone_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        iphone_entity = next(tracker.get_latest_entity_values("phone"), None)

        if iphone_entity:
            dispatcher.utter_message(text=f"You have selected {iphone_entity} variant")
        else:
            dispatcher.utter_message(text="Sorry, I could not detect the phone variant. Can you be more specific")
        return []


class ExtractSamsungEntity(Action):

    def name(self) -> Text:
        return "action_extract_samsung_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        samsung_entity = next(tracker.get_latest_entity_values("phone"), None)

        if samsung_entity:
            dispatcher.utter_message(text=f"We have different models of {samsung_entity}. which do you like to order")
        else:
            dispatcher.utter_message(text="Sorry, I could not detect the phone variant. Can you be more specific")
        return []