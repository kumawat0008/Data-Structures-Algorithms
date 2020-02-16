test = int(input())

for i in range(test):
    n,q = input().split()
    n = int(n)
    q = int(q)
    persons = list(input().split())
    mu_frnds = dict()
    
    
    list_of_sets = list()
    for q in range(q):
        query, p1,p2 = input().split()
        
        if query == "addincircle":
            if p1 in mu_frnds and mu_frnds[p1]!=p2:
                mu_frnds[p2] = p1
            else:
                mu_frnds[p1] = p2
        
        elif query == "arewefriends":
            # print('++++++',mu_frnds)
            if p1 in mu_frnds and mu_frnds[p1]==p2 or p2 in mu_frnds and mu_frnds[p2]==p1:
                print("1")
            elif p1 in mu_frnds:
                # print('++++if')
                friend = mu_frnds[p1]
                while True:
                    # print('++++++friend',friend)
                    if friend == p2:
                        print("1")
                        break
                    try:
                        friend = mu_frnds[friend]
                    except:
                        print("0")
                        break
                    
            elif p2 in mu_frnds:
                # print('++++else')
                friend = mu_frnds[p2]
                while True:
                    if friend == p1:
                        print("1")
                        break
                    try:
                        friend = mu_frnds[friend]
                    except:
                        print("0")
                        break
            else:
                print("0")
        