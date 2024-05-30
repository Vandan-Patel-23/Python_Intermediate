raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(320291, "No Prize"))
print(raffle)

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81],"Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78],
"Dina":[64, 60, 75]}
for score_list in test_scores.values():
    print(score_list)

# Classwork
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries",
"Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini",
"Libra", "Aquarius"]}
print(zodiac_elements['earth'])
print(zodiac_elements['fire'])

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam":
123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id=user_ids.get('teraCoder',100000)
print(tc_id)
stack_id=user_ids.get('superStackSmashcm',100000)
print(stack_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir":
20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
available_items.pop('power stew', "No Prize")
available_items.pop('stamina grains', 100000)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22,"lists": 19, "classes": 18, "dictionaries": 18}
for i in num_exercises.values():
    print(i)
lessons=list(num_exercises)
print(lessons)

women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for i, j in women_in_occupation.items():
    print('Women make up',j ,'percent of',i,'s.')