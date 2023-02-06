import random

RANDOM_SCHEDULER = "random"

def schedule_func_from(input):
    if input == RANDOM_SCHEDULER:
        return random_scheduler
    else:
        return Exception("Unknown scheduler: " + input)

def random_scheduler(socks):
    return random.choice(socks)
