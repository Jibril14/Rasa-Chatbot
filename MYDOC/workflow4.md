# Rasa form
Rasa form is use to collect pieces of information from users, 
Collection of information from users also know as slot filling, Rasa form makes it easy

user: I want to buy a pizza ------rule
                                     |
                          -          --------------|
                                                pizza-form: active 
                                                [] pizza-type slot
                                                [] pizza-size slot

Think about this like an html form that need to validate data collected, on the frontend before sending to the server.
In this case the pizza-form must collect values for the two slot before activating a particular custom action. if not it will keep asking the user for all the information until all the slots are filled in (we dont have to write story for this, rather ask for a missing value from entity or text etc)

bot: What kind of pizza?
user: maloni
bot: What size
user: big

- Until now all the slot are now completed, it become inactive and a custom action can be call


## To configure a form in rasa we need to set two rules, one rule to
# activate the form and another rule to deactivate it 

## Wrong slot specify by use
user: I want to buy pizza
bot: What kind of pizza?
user: fruit----------------------------invalid entity
bot: What kind of pizza?
- If input from user is invalid, we want to prevent the slot from been set. we typical write a custom action to validate forms, to prevent some kind of validation, we can for example provide the types of pizza available upfront
