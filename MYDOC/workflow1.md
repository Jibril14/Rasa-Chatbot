# Rasa is a tool to help you build task oriented dialogue systems

# The core of building a Rasa assistant is providing examples that your system learns from. That way, Rasa can attempt to generalise patterns in your data. 


# Workflow

# nlu.yml

- We define an intent (eg thank) in nlu.yml, then we give examples(training data), this is a write up 
patterns we want our model to recognise eg thank you, appreciate, many thanks

# domain.yml
- Then here we bring a list of all intents as they are in nlu.yml. We also define a list of responses
 here too. The domain.yml is like where the bot stores text(response)
- other components in here are: actions, slots, forms, templates
# stories.yml
- stories.yml has two keys intent: greet & action: utter_greet (we call out intents as define in nlu.yml and
 responses has define in domain.yml). stories.yml is use to define the conversational flow of 
 chatbot(intent & values).  map the response to an intent and trigger it. here we call 
 values define inside domain.yml. stories.yml is like a selfcontain conversation, where we can call a series 
 of intents(patterns) and responses to match it e.g
 
 - story: A conversation about a day
  steps:
  - intent: greet
  - action: utter_greet
  - intent: mood_unhappy
  - action: utter_cheer_up

 # At this point, I did
 - rasa train 
 - rasa shell # seems to need internet connection the 1st time I chat