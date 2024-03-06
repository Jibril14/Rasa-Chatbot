# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

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

'''
  - laptop_os
  - laptop_brand
  - laptop_processor
'''

AVAILABLE_LAPTOP_BRANDS = ["hp", "dell", "lenovo", "apple", "alienware", "asus"]
AVAILABLE_LAPTOP_PROCESSORS = ["intel celeron", "intel core i3", "intel core i5", "intel core i7", "intel core i9"]
AVAILABLE_OS_TYPES = ["windows", "macbook", "mac", "linux"]


# class ValidateFirstLaptopForm(FormValidationAction): # inheriting from a validation action
#     def name(self) -> Text:
#         return "validate_first_laptop_form" # must be name validate_<name of the form>
    
#     def validate_laptop_os(
#         self,
#         slot_value: Any, 
#         dispatcher: CollectingDispatcher, 
#         tracker: Tracker,
#         domain: DomainDict
#         ) -> Dict[Text, Any]:
#         """Validate `laptop os` value."""
#         if slot_value.lower() not in AVAILABLE_OS_TYPES:
#             dispatcher.utter_message(text="We dont have your specify OS")
#             return {"laptop_os": None}
#         dispatcher.utter_message(text=f"Ok! You choose a laptop with {slot_value} OS")
#         return {"laptop_os": slot_value}

#     def validate_laptop_brand(
#         self,
#         slot_value: Any, 
#         dispatcher: CollectingDispatcher, 
#         tracker: Tracker,
#         domain: DomainDict
#         ) -> Dict[Text, Any]:
#         """Validate `laptop brand` value."""
#         if slot_value.lower() not in AVAILABLE_LAPTOP_BRANDS:
#             dispatcher.utter_message(text=f"We dont have your specify Brand right now. Choose {'/'.join(AVAILABLE_LAPTOP_BRANDS)}")
#             return {"laptop_brand": None}
#         dispatcher.utter_message(text=f"Ok! You choose a {slot_value} laptop")
#         return {"laptop_brand": slot_value}

#     def validate_laptop_processor(
#         self,
#         slot_value: Any, 
#         dispatcher: CollectingDispatcher, 
#         tracker: Tracker,
#         domain: DomainDict
#         ) -> Dict[Text, Any]:
#         """Validate `laptop processor` value."""
#         if slot_value.lower() not in AVAILABLE_LAPTOP_PROCESSORS:
#             dispatcher.utter_message(text="We dont have your specify processor")
#             return {"laptop_processor": None}
#         dispatcher.utter_message(text=f"Good! You choose a laptop with {slot_value} processor")
#         return {"laptop_processor": slot_value}

# this generate a button, so user can set a boolean value which in turn is used in validate_laptop_touch_screen function
# You can call this class with a botton from frontend. 
# intead of of using button to triger intent, from frontend we can us botton to enter a slot
# or just message and use the triggered intent to do as below
class AskForLaptopToachScreen(Action):
    """Ask weather laptop be touch screen. In Second laptop form"""
    """Programmatically generate a button that a user can press"""
    """Button in rasa interactive """

    def name(self) -> Text:
        return "action_ask_laptop_touch_screen"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Would you like to order a touch screen laptop?",
            buttons=[
                {"title": "yes", "payload": "/affirm"}, # triggers /affirm intent if a person press yes, set val to True
                {"title": "no", "payload": "/deny"}, # corresponding to slot mapping
            ],
            
            )
        return []


# This class is added to show that is possible to write a validation not for the entire form,
# But for a single slot in the form e.g AskForLaptopToachScreen above.
# class EXTRAVALIDATIONFORLAPTOOSSLOT(Action):

#     def name(self) -> Text:
#         return "action_ask_laptop_os"

#     def run(self, 
#             dispatcher: CollectingDispatcher,
#             slot_value: Any,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         if tracker.get_slot("laptop_touch_screen"):
#             dispatcher.utter_message(text=f"I will remember touch screen laptop")
#         else:
#              dispatcher.utter_message(text=f"No value for touch screen laptop")
#         return []



# When a form is triggered, it want to collect slot. this validation class will run
# and validate each slot according to which come first in the domain.yml file or which is entered by the user first
# not according to which validation is written 1st here

# Also this Validation class will run any class above if the name of the class above is action_ask_<slot name>
# where slot name = any slot it validating e.g before def validate_laptop_touch_screen run it 1st run action_ask_laptop_touch_screen
# we still need to put both inside domain.yml under actions: ie action_ask_laptop_touch_screen & validate_laptop_touch_screen


class ValidateSecondLaptopForm(FormValidationAction): # inheriting from a validation action
    def name(self) -> Text:
        return "validate_second_laptop_form" # must be name validate_<name of the form>

    def validate_laptop_os(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker,
        domain: DomainDict
        ) -> Dict[Text, Any]:
        """Validate `laptop os` value."""
        if slot_value.lower() not in AVAILABLE_OS_TYPES:
            dispatcher.utter_message(text="We dont have your specify OS")
            return {"laptop_os": None}
        dispatcher.utter_message(text=f"Ok! You choose a laptop with {slot_value} OS")
        return {"laptop_os": slot_value}

    def validate_laptop_touch_screen( # validate_ <name of slot>
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker,
        domain: DomainDict
        ) -> Dict[Text, Any]:
        """Validate `laptop screen` value."""

        if tracker.get_intent_of_latest_message() == "affirm":
            dispatcher.utter_message(text="I will remember you prefer a touch screen laptop")
            return {"laptop_touch_screen": True}

        if tracker.get_intent_of_latest_message() == "deny":
            dispatcher.utter_message(text="I will remember that you dont want a touch screen laptop")
            return {"laptop_touch_screen": False}

        dispatcher.utter_message(text="I did not get that")
        return {"laptop_touch_screen": None}

    def validate_laptop_brand(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker,
        domain: DomainDict
        ) -> Dict[Text, Any]:
        """Validate `laptop brand` value."""
        if slot_value.lower() not in AVAILABLE_LAPTOP_BRANDS:
            dispatcher.utter_message(text=f"We dont have your specify Brand right now. Choose {'/'.join(AVAILABLE_LAPTOP_BRANDS)}")
            return {"laptop_brand": None}
        dispatcher.utter_message(text=f"Ok! You choose a {slot_value} laptop")
        return {"laptop_brand": slot_value}

    def validate_laptop_processor(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker,
        domain: DomainDict
        ) -> Dict[Text, Any]:
        """Validate `laptop processor` value."""
        if slot_value.lower() not in AVAILABLE_LAPTOP_PROCESSORS:
            dispatcher.utter_message(text="We dont have your specify processor")
            return {"laptop_processor": None}
        dispatcher.utter_message(text=f"Good! You choose a laptop with {slot_value} processor")
        return {"laptop_processor": slot_value}