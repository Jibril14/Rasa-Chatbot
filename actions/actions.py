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


class ValidateFirstLaptopForm(FormValidationAction): # inheriting from a validation action
    def name(self) -> Text:
        return "validate_first_laptop_form" # must be name validate_<name of the form>
    
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


