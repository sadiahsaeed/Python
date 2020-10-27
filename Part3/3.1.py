import random

a_rand = random.sample(range(1, 100), 10)
print a_rand
b_rand = random.sample(range(1, 100), 10)
print b_rand

c_rand_set = set(a_rand) & set(b_rand)
print c_rand_set
input()
