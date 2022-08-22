import itertools
user1_list = []
user2_list = []
total_list = []
patterns = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
game = 0

while game<9:

    user1 = int(input("User1: "))
    while user1 in total_list:
        user1 = int(input("Already number entered choose another number: "))
    total_list.append(user1)
    user1_list.append(user1)
    for i in range(1,10):
        if i in user1_list:
           print(f"|x|",end=" ")
        elif i in user2_list:
            print(f"|o|", end=" ")
        else:
            print(f"| |", end=" ")
        if i%3==0:
               print()
   
    comb = list(itertools.combinations(user1_list,3))#from itertools module finding combinations
    if len(user1_list)>=3:
        for item in patterns:
            perm = list(itertools.permutations(item))
            for iters in perm:
               if iters in comb:
                   print("user1 win")
                   game = 10
    game = game+1
    if game < 9:
        user2 = int(input("User2: "))
        while user2 in total_list:
            user2 = int(input("Already number entered choose another number: "))
        total_list.append(user2)
        user2_list.append(user2)
        for i in range(1,10):
            if i in user2_list:
               print(f"|o|",end=" ")
            elif i in user1_list:
                print(f"|x|", end=" ")
            else:
                print(f"| |", end=" ")
            if i%3==0:
                   print()
       
        comb = list(itertools.combinations(user2_list,3))#from itertools module finding combinations
        if len(user2_list)>=3:
            for item in patterns:
                perm = list(itertools.permutations(item))
                for iters in perm:
                   if iters in comb:
                       print("user2 win")
                       game = 10
    game = game+1                
print("Game over")
