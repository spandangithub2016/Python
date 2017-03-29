def sumprimes(l):
    pr_Num = []
    for item in l:
        is_prime = True
        if(item >= 2):
            maxnum= int(item ** 0.5) + 1
            for i in range(2, maxnum):
                if(item % i == 0):
                    is_prime = False
                    break
            if(is_prime):
                pr_Num.append(item)
    return(sum(pr_Num))
l = [eval(x) for x in input().split()]
print(sumprimes(l))

