def max_profit(houses, house_no, cache):
    for i in range(2,len(cache)):
        cache[i] = max(houses[i-1]+cache[i-2],cache[i-1])


def main():

    houses = [10,20, 15, 35, 30]
    cache = [0]*(len(houses)+1)
    cache[1] = houses[0]
    max_profit(houses,len(houses)-1,cache)
    print(cache)


if __name__ == '__main__':
    main()
    