# states=['kerala','goa','tamilndu']
# capital=['tvm','panaji','chennai']
# states_capital={}
# states_capital= {'kerala':"tvm"}
#  print(states_capital)
# {'kerala': 'tvm'}

states=['kerala','goa','tamilndu']
capital=['tvm','panaji','chennai']
states_capital={}

size = len(states)
for i in range(size):
    key = states[i]
    value = capital[i]
    states_capital[key] = value

print(states_capital)