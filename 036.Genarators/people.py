import memory_profiler as mem_profile
import random
import time
mem_profile.memory_usage_resource = mem_profile.memory_usage

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'ComSci', 'Arts', 'Business']

print('Memory (Before): {}Mb'.format(mem_profile.memory_usage_resource()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
            }
        result.append(person)
    return result

def people_genarator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
            }
        yield person

t1 = time.perf_counter()
people = people_list(1_000_000)
t2 = time.perf_counter()

print('Memory (After) : {}Mb'.format(mem_profile.memory_usage_resource()))
print('Took {} Seconds'.format(t2-t1))