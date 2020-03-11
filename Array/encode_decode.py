def encode(msg,key):
    res = ""
    if len(msg)>=len(key):
        pass
    else:
        key = key[0:len(msg)]
    for i,ch in enumerate(key):
            digit = int(ch)
            for j in range(digit):
                res  = res+msg[i]
    return res+msg[i+1:]

def decode(msg,key):
    res = ""
    index = 0
    for ch in key:
        digit = int(ch)
        for i in range(digit):
            index+=1
        if index <=len(msg):
            res = res+msg[index-1]
    
    res = res+msg[index:]
    return res
    

def main():
    msg = "open"
    key = "1234"
    key2 = "1234"
    msg2 = "oppeeennnn"
    print(encode(msg,key))
    print(decode(msg2,key2))
if __name__ == '__main__':
    main()
    