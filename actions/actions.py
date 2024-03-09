from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


AVAILABLE_LAPTOP_BRANDS = ["hp", "dell", "lenovo", "apple", "alienware", "asus"]
AVAILABLE_LAPTOP_PROCESSORS = ["intel celeron", "intel core i3", "intel core i5", "intel core i7", "intel core i9"]
AVAILABLE_OS_TYPES = ["windows", "macbook", "mac", "linux"]


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
                {"title": "yes", "payload": "/affirm"},
                {"title": "no", "payload": "/deny"},
            ],
            
            )
        return []


class ValidateSecondLaptopForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_second_laptop_form"

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

    def validate_laptop_touch_screen(
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