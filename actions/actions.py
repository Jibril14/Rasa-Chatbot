from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


import random

def shuffle_response_template(templates):
    return random.choice(templates)
    

class  ActionValidateSlot(Action): 

    def name(self) -> Text:
        return "action_laptop_uses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        specify_slots = tracker.get_slot("laptop_use")

        if specify_slots != None:
            specify_slot = " ".join(specify_slots)

            response = domain["responses"]["utter_laptop_use"][0]
            response_text = response["text"].format(laptop_use=specify_slot)
            dispatcher.utter_message(text=response_text)
        else:
            dispatcher.utter_message(text=f"We have some good products checkout: <DB data latest product>")
        return []


class  ActionValidateLaptopUseAndBudget(Action): 

    def name(self) -> Text:
        return "action_laptop_recommend"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        specify_slots = tracker.get_slot("laptop_use")
        specify_budget = tracker.get_slot("laptop_budget")
        # specify_slot = " ".join(specify_slots)
       
            # samsung_entity = next(tracker.get_latest_entity_values("phone"), None)
        
        
        if specify_slots != None:
            response = domain["responses"]["utter_recommend_laptop_if_user_give_use"][0]
            response_text = response["text"].format(laptop_use=type(specify_slots))
        if specify_budget != None:
            response = domain["responses"]["utter_recommend_laptop_if_user_give_budget"][0]
            if int(specify_budget) < 200:
                specify_budget = "small budget < $400"
            response_text = response["text"].format(budget=specify_budget)
        if specify_budget and specify_slots != None:
            for slot in specify_slots:
                specify_slot = slot + " "
            response = domain["responses"]["utter_recommend_laptop_if_user_give_use_and_budget"][0]
            response_text = response["text"].format(laptop_use=specify_slot, budget=specify_budget)
       
        
        dispatcher.utter_message(text=response_text)
        return []


class  ActionGetQueryBrand(Action): 
    """Get user query for a particullar brand"""
    def name(self) -> Text:
        return "action_get_available_brand"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        response = [
            domain["responses"]["utter_brand_availability_and_stock"][0],
            domain["responses"]["utter_brand_availability_and_stock"][1]
        ]
        response = shuffle_response_template(response)
        specify_brand = tracker.get_slot("query_brand")
        response_text = response["text"].format(query_brand="")
        if specify_brand != None:
            response_text = response["text"].format(query_brand=specify_brand)
        dispatcher.utter_message(text=response_text)
        return []




from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        response = [ 
            domain["responses"]["utter_default_one"][0],
            domain["responses"]["utter_default_one"][1]
        ]
        response = shuffle_response_template(response)
        dispatcher.utter_message(text=response)
        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]