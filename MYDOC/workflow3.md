# Rasa Slot

Slots are like the assistant memory
They alow the chatbot to store important details and later use them in a specific context e.g:
I would like to book a flight to Lagos.
slot: destination
value: Lagos
The chatbot now have the knowlegh that we are booking a flight to Lagos


# Configuration (1 Using NLU file)
## here we extract our slot from the tags in our training
entities:
- destination

slots:
    destination:
        type: test
        influence_conversation: false # should it influence the conversation?
        mappings:
        - type: custom

## Configuration ( Using custom actions)
- In some cases get data from data base or API call. these details can be use as slot and use in a specific context

# Influencing the conversation
## Slot can be configure to influence the flow of a conversation
- influence_conversation: false
This means the slot will influence the dialogue management model to make prediction for the next actions. a slot value if present/absent can influence the flow of a conversation. e.g

user: I would like to book a flight to New York
chatbot: Sure! Looking for the options.

user: I would like to book a flight ticket.
chatbot: What is your destination
- They way slot influence conversation highly depend on the type of slot

# Configuring the stories for slot
## If slot is configure to influence the flow of conversation,
## we have to include them in the training stories
## ie: after intent book_a_ticket is call do this or this
# or slot value allow us to diferenciate slot value or increase the length of story file. if you find your self use them alot, you might need to look into your domain file intead

stories:
- story: booking a flight ticket
    steps:
    - intent: book_a_ticket
    - or:
        - slot_was_set:
            - destination: Ontario
        - slot_was_set:
            - destination: Abuja


# Slot Mappings
## Slot mappings are applied after each user message
## the define how each slot should get their value

e.g
in domain.yml
entities:
- entity_name
slots:
    amount_of_money:
        type: any
        mappings:
        - type: from_entity # slot will be fill in with value from this entity
          entity: number # the actual entity name that ill fill the slot is number
          intent: make_transaction # slot will be applied to only this intent
          not_intent: check_transaction # if this intent pedicted, then slot will not be applied

e.g
- Send N5000 to John    -make_transaction -this will use slot
- I didn't receive any N20000 from Lia   -check_transaction -this will not use slot


# Types of Slot Mapping
# 1: from_entity (fills in the slot base on the entities extracted)

entities:
- entity_name
slots:
    slot_name:
        type: any
        mappings:
        - type: from_entity # slot will be fill in with value from entity
          entity: entity_name
          role: role_name
          group: group_name
          intent: intent_name
          not_intent: excluded_intent name
i.e
- role: only applies the mapping if the extracted entity has this role.
- group: only applies the mapping if the extracted entity belongs to this group.
- intent: Only applies the mapping when this intent is predicted.
- not_intent: does not apply the mapping when this intent is predicted

# 2: from_text (fills in the slot base on the text of the last message user entered)

slots:
    slot_name:
        type: text
        mappings:
        - type: from_text # slot will be fill in with value from text
          intent: intent_name
          not_intent: excluded_intent name

# 3: from_intent (fills in the slot base on the predicted intent )
slots:
    slot_name:
        type: any
        mappings:
        - type: from_intent # slot will be fill in with value from intent
          value: my_value
          intent: intent_name
          not_intent: excluded_intent name

# 4: from_trigger_intent (fills in the slot with a specific defined value if 
# a form is activated by a user message with a specific intent)
slots:
    slot_name:
        type: any
        mappings:
        - type: from_trigger_intent
          value: my_value
          intent: intent_name
          not_intent: excluded_intent name


# 5: custom (if non of the predefined slot mapping suit my need)
## I can create custom slot mapping using slot validation actions(a special types of action)

slots:
    day_of_week:
        type: text
        mappings:
        - type: custom
          action: action_calculate_day_of_week



-  Again they way slot influence conversation highly depend on the type of slot
- All the slot types can have -influence_conversation: false/true if you want them to influence the convrsation. the present or absent of this slot can now drive the conversation

# 6: Boolean slot (Can be use to store information that can get the values True of False)

slots:
    authenticated:
        type: boolean
        influence_conversation: true # I added
        mappings:
        - type: custom
          action: show_last_month_order_info

e.g a chatbot can check in the background if a user is authenticated to access specific information or perform specific action:
user: My user Id is 12345
chatbot: user id is valid user ID


# 7: Categorical slot (this is perfect to store values that can get one of the possible N values) may be 1 item from a list
# this can also influnce how the conversation goes e.g (medium is a slut here)
# user: I would like to book a table at the restaurant within medium price range
# bot: Sure! here are the options withing a medium price range

slots:
    price_range:
        type: categorical
        values: # some may get value from entity
            - low
            - medium
            - high
        mappings:
        - type: custom
          

# 8) Float Slot (can be use to store numerical values)
slots:
    radius:
        type: float
        min_value: 0
        max_value: 100
        mappings:
        - type: custom
e.g (make the conversation to a more specific search)
user: Looking for a restaurant within 10 mile radius
chatbot: sure, here is the result

# 9) List Slot (similar to text slot. can be use to store
lists of values values)
# the presence of this slot, when specified can influence the conversation flow
entities:
- shopping_item
- order_list
slots:
    cart:
        type: list
        mappings:
        - type: from_entity
        entity: shopping_item # the entity name

e.g a bot that help make order
user: I'd like to order some cookies, chocolate and milk
chatbot: Items are added to the shopping list

# 10) Any slot type (can be use to store any arbitrary values.)
# slots of this type dont have any influence on the conversation
# flow which means that the value and the prensence of the slot
# doesnot have any influence on how the conversation goes

slots:
    shopping_items:
        type: any
        mappings:
        - type: custom


_________________________________________________________________________________
I want to check if the presence of flag -influence_conversation: true/false
is what enforce the influence of slot on conversation or just the type of slot
whats the default behaviour ie without the flag influence_conversation: true
also note some slot define their values ie not getting it fro entities



# The initial_value parameter (To set a default initial value to slot)
## The value will be assign to the slot from the begginning of conversation
## and be reset later by the NLU or custom actions

slots:
    current_account:
        type: float
        initial_value: 200
        mappings:
        - type: custom

