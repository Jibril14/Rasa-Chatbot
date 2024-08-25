# response_text = "I'll recommend a few options for work### gaming within $300 budget."

# txt = response_text.replace("###", ",")

# print(txt)

# import re
# pattern = r'(\w+)###'
# match = re.search(pattern, response_text)
# if match:
#     print(match.group(1))
#     lst = response_text.split(match.group(1))
#     print(lst)

specify_slots = ["work", "gaming"]
if specify_slots != None:
    specify_slot = " ".join(specify_slots)
    if len(specify_slots) > 1:
        specify_slot = " and ".join(specify_slots)

print("specify_slots:", specify_slot)