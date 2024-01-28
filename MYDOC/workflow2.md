Adding custom actions (In the Domain.yml response without the utter_ prefix are action)

- The rules.yml file may not be use for every chatbot cases
thour similar to stories.yml some of it use cases are: 
Explicit control of conversational flow
More customizations
Fallback and clarification handling
Overriding default behaviour
simplifying complex dialogue management



- Entities: importants info the charbot extract from users to understand user requests
- Entities extraction: To give bot capability to extract entities, we need to define them in our label data e.g 
I want to order a [pizza](food) # this the format for entity anotation
- Synonyms: The are use to improve the NLU of the chatbot, by allowing it to recognize diffrent variation of the same entity values.
e.g same city differet names
[Abuja](Nigeria)
[ABJ](Nigeria)

- Regex Patterns: use in nlu.yml, is a powerful tool use for defining rules that can match and extract entities from user input base on specifict patterns.
E.g Utterances that contain certain words
- regex: hours
  examples: |
    - \bopen\b


# Intent Recognition & Entity Extraction
- Intent Recognition & Entity Extraction
Book a flight for three people in Abuja at the Emirate airline on Monday
Intent: "flight_reservation"
number_of_people: "Abuja"
location: "Abuja"
date: "Monday

- We already have some entities define in our training label
- The action.py file is use to define custom actions, action are use to implement logic and perform actions base on user input(input, intent & entities)

we enable actions in the endpoints.yml
and run: rasa run actions