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


 # In general there are two mechanisms inside of Rasa that drive the Conversational AI.

 - NLU stands for natural language understanding
 This can be rule based, in which case we may be using a Regex or it can be based on a neural network.
Rasa comes with a neural network architecture, called DIET, that sorts texts into intents 
and entities based on examples it's been provided.
Rule based approach tend to be more lightweight and require more domain knowledge to get right.
Neural approaches tend to require more training data and compute power but they're very good 
at handling thigns they haven't seen before.


- Dialogue Policies

When we talk about Dialogue Policies we're referring to the part of the system that predicts the next
action to take. The next action isn't just determined based on the current intent, we typically need
to know about the entire conversation so far
Policies can again be based on rules or on neural methods. Rasa allows you to define your own
lightweight rules to define what needs to happen. But in order to allow for generalization Rasa
also provides a neural network called TED that picks the next best turn based on the conversation
so far and all the conversations that it trained on.
Rasa recommend using both rule-based approaches and neural methods in tandem

# How to make Conversations Work
The Rasa approach is flexible, but it works better the more high-quality data you have.
That means that you'll want to manually review and annotate conversations
as you're building your assistant
In order to improve the performance of an assistant, it's helpful to practice CDD and add new
training examples based on how your users have talked to your assistant. You can use rasa train 
co--finetune to initialize the pipeline with an already trained model and further finetune
# Dependencies (Not sure yet)
Rasa uses Spacy model. Small models require less memory to run, but will likely reduce
 intent classification performance.