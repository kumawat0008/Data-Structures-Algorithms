def max_profit_from_houses(houses, house_no,cache):

    if house_no<0:
        return 0
    if house_no == 0:
        return houses[0]

    if cache[house_no]!=0:
        return cache[house_no]

    profit = max(houses[house_no]+max_profit_from_houses(houses,house_no-2,cache),max_profit_from_houses(houses,house_no-1,cache))
    cache[house_no] = profit
    return profit



def main():

    houses = [10,20, 15, 35, 30]
    cache = [0]*len(houses)
    max_profit = max_profit_from_houses(houses,len(houses)-1,cache)
    print(max_profit)


if __name__ == '__main__':
    main()
    