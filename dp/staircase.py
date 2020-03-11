def number_of_ways(n,options,dp):

    if n ==0:
        return 1
    if n<0:
        return 0
    if n not in dp:
        sum = 0
        for i in options:
            sum = sum + number_of_ways(n-i,options,dp)
        dp[n]=sum
    return dp[n]

def main():
    n = 50
    options = [1,3,5]
    dp = dict()
    print(number_of_ways(n,options,dp))

if __name__ == '__main__':
    main()
    