import random
import time
from django.http import HttpResponse

def randomInt():
    time.sleep(5)
    b = random.randint(1, 10000)
    return b
    
while True:
    a = randomInt()
    print(a)