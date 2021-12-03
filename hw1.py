import requests

TOKEN = "2619421814940190"

super_three = ['Hulk', 'Captain America', 'Thanos']
super_three_dict = {}

for each in super_three:
    response = requests.get(f'https://superheroapi.com/api/{TOKEN}'
                            f'/search/{each}')
    intelligence = response.json()['results'][0]['powerstats']['intelligence']
    super_three_dict[each] = int(intelligence)

max_intelligence = max(super_three_dict, key=super_three_dict.get)
print(f'Самый умный из супергероев {max_intelligence}')
