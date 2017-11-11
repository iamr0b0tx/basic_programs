keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

table = {x:str(x) for x in range(10)}
table_rev = {str(x):x for x in range(10)}

table.update({x+10:keys[x] for x in range(len(keys))})
table_rev.update({keys[x]:x+10 for x in range(len(keys))})

def convert(a, b, c=False):
    if c == False:
        c = 10
    if b != c:
        if b != 10:
            if type(a) == str:
                ab10 = [table_rev[x] for x in list(a)]
            else:
                ab10 = [int(x) for x in list(str(a))]
            ab10 = sum([(ab10[i]*(b**(len(ab10) - i - 1))) for i in range(len(ab10))])
        else:
            ab10 = a

        abc = []
        print(ab10)
        while ab10 != 0:
            x = int(ab10)
            v = ab10%c
            if v in table:
                v = table[v]
            abc.append(str(v))
            ab10 //= c
            print(str(a)[:10], c, v, ab10)
        abc.reverse() 
        val = "".join(abc)
    
    return val

if __name__ == '__main__':
    print(convert(65535, 10, 36))
    print(convert('1ekf', 36))
    print(convert('christian', 36))
    print(convert('christian300chriscom1002980180firstbank', 36))
