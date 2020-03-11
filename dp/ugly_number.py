def find_nth_ugly_number(n):
    ugly_numbers = [1]
    i2 = 0
    i3 = 0
    i5 = 0
    next_mult_2 = 2
    next_mult_3 = 3
    next_mult_5 = 5
    while n-1:
        minimum = min(next_mult_2,next_mult_3,next_mult_5)
        ugly_numbers.append(minimum)
        if minimum == next_mult_2:
            i2+=1
            next_mult_2 =2*ugly_numbers[i2]
        if minimum == next_mult_3:
            i3+=1
            next_mult_3 =3*ugly_numbers[i3]
        if minimum == next_mult_5:
            i5+=1
            next_mult_5 =5*ugly_numbers[i5]
        n-=1
    return ugly_numbers

def main():
    
    print(find_nth_ugly_number(50))


if __name__ == '__main__':
    main()
    