def findRotations(str):
    tmp = str + str
    n = len(str)
 
    for i in range(1, n + 1):
         
        substring = tmp[i: i+n]
 
        if (str == substring):
            return i
    return n

if __name__ == '__main__':
 
    str = "abc"
    print(findRotations(str))
 