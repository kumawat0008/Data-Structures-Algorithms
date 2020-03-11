import sys

def min_steps(source, destination, steps, cache,count):

    count[0]+=1

    if abs(source)>abs(destination):
        return sys.maxsize
    if source==destination:
        return steps
    if steps in cache:
        return cache[steps]
    cache[steps] = min(min_steps(source+steps+1,destination,steps+1,cache,count),min_steps(source-steps-1,destination,steps+1,cache,count))
    return cache[steps]

cache = dict()
count = [0]
print(min_steps(0,90,0,cache,count),count[0])