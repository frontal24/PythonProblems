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

#Cyclops numbers
# def is_cyclops(n):
#     if n==0: return True
#     n_as_str = str(n)
#     print("{},{},{}".format(n_as_str, type(n_as_str), len(n_as_str)))
#     if (len(n_as_str) % 2) == 0:
#         return False
#     mid = int(len(n_as_str)/2)
#     if n_as_str[mid] == str(0):
#         return True
#     return False

#Domino cycle
def domino_cycle(tiles):
    if len(tiles)==0: return True
    # if len(tiles) ==1:
    #     if tiles[0][0] ==tiles[0][1]:return True
    #     else: return False
    first_item = tiles[0][0]
    last_item = tiles[0][1]
    for (f,l) in tiles[1:]:
        if (last_item != f):
            return False
        last_item = l
    if (last_item != first_item):
        return False
    return True

#Count dominators
def count_dominators(items):
    if len(items) == 0: return 0
    if len(items) == 1: return 1
    num_dominators = 1#this should be 1
    cur_max = items[-1]
    for index in range(len(items)-2,-1,-1):
        if items[index] > cur_max:
            num_dominators += 1
            cur_max = items[index]
    return num_dominators

#Extract increasing integers from digit string

def extract_increasing(digits):
    if len(digits) == 0: return []
    leftover = ""
    result = [int(digits[0])]
    for d in digits[1:]:
        lastIdx = (len(result) - 1)
        leftover = leftover + d
        if int(leftover) > result[lastIdx]:
            result.append(int(leftover))
            leftover = ""
    return result


#Words that contain given letter sequence
#def words_with_letters(words, letters):






