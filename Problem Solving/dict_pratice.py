state_capital = {
    "telangana": "hyderabad",
    "andhra":"amaravathi",
    "madhya pradesh":"bhopal",
    "bihar": "patna"
}
state_capital["maharastra"] = "mumbai"
print("after adding \n", state_capital)
print(state_capital.values())
print(state_capital.keys())

print("iterating dictionary")
for state, capital in state_capital.items():
    print(state , ":", capital)

print("after removing one value , printing removed values")
capital = state_capital.pop("andhra")
print(capital)
print(state_capital)

state_capital.clear()
print(state_capital)
print("re-creating dict")
state_capital = {
    "telangana": "hyderabad",
    "andhra":"amaravathi",
    "madhya pradesh":"bhopal",
    "bihar": "patna"
}
print(state_capital.get("telangana"))
print(state_capital.get("bihar"))

new_capitals = {"goa":"panaji", "up": "lucknow"}
state_capital.update(new_capitals)
print(state_capital)

print("key value pairs: ",  list(state_capital.items()))


"""
after adding 
 {'telangana': 'hyderabad', 'andhra': 'amaravathi', 'madhya pradesh': 'bhopal', 'bihar': 'patna', 'maharastra': 'mumbai'}
dict_values(['hyderabad', 'amaravathi', 'bhopal', 'patna', 'mumbai'])
dict_keys(['telangana', 'andhra', 'madhya pradesh', 'bihar', 'maharastra'])
iterating dictionary
telangana : hyderabad
andhra : amaravathi
madhya pradesh : bhopal
bihar : patna
maharastra : mumbai
after removing one value , printing removed values
amaravathi
{'telangana': 'hyderabad', 'madhya pradesh': 'bhopal', 'bihar': 'patna', 'maharastra': 'mumbai'}
{}
re-creating dict
hyderabad
patna
{'telangana': 'hyderabad', 'andhra': 'amaravathi', 'madhya pradesh': 'bhopal', 'bihar': 'patna', 'goa': 'panaji', 'up': 'lucknow'}
key value pairs:  [('telangana', 'hyderabad'), ('andhra', 'amaravathi'), ('madhya pradesh', 'bhopal'), ('bihar', 'patna'), ('goa', 'panaji'), ('up', 'lucknow')]
"""