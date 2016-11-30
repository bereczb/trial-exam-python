pirates = [
  {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
  {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
  {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
  {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
  {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that has wooden leg and
# more than 15 gold

def count_woden_leg_and_gold(list_of_pirates):

    result_list = []

    for i in range(len(list_of_pirates)):
        if list_of_pirates[i]['has_wooden_leg'] and list_of_pirates[i]['gold'] > 15:
            result_list.append(list_of_pirates[i]['Name'])

    return result_list

print(count_woden_leg_and_gold(pirates))
