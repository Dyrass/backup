import os
import random
p = '/home/arvind/Pictures'
os.chdir(p)


file = random.choice(os.listdir())
print(os.listdir())
try:
    os.system(f'xdg-open "{os.path.realpath(file)}"')
except Exception as e:
    print(e)