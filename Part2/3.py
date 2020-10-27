import itertools      
data ={'1':['a','b'], '2':['c','d']}
for array in itertools.product(*[data[i] for i in sorted(data.keys())]):
    print(''.join(array))
