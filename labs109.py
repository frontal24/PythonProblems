# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust

#Ascending list
def is_ascending(items):
    if len(items) == 0:
        return True
    cur = items[0]
    for item in items[1:]:
        if cur > item:
            return False
        cur = item
    return True

# Riffle
def riffle(items, out = True):
    result=[]
    items = items[:]
    if len(items) == 0:
        return []
    #print(items)
    a = int(len(items)/2)
    list1 = items[:a]
    list2 = items[a:]
    for i in range(a):
        if out:
            result.extend([list1[i],list2[i]])
        else:
            result.extend([list2[i],list1[i]])
    return result


# Only odd digits
def only_odd_digits(n):
    while(n>10):
        digit = n%10
        n = n//10
        if (digit%2==0):
            return False
    if (n%2==1):
        return True
    return False

# Blocks in pyramid
def pyramid_blocks(n, m, h):
    result = 0
    for i in range(h):
        result += (n+i)*(m+i)
    return result