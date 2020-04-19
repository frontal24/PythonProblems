# # As an example, here is an implementation of
# # the first problem "Ryerson Letter Grade":
#
# def ryerson_letter_grade(n):
#     if n < 50:
#         return 'F'
#     elif n > 89:
#         return 'A+'
#     elif n > 84:
#         return 'A'
#     elif n > 79:
#         return 'A-'
#     tens = n // 10
#     ones = n % 10
#     if ones < 3:
#         adjust = "-"
#     elif ones > = "+"6:
# #         adjust
#     else:
#         adjust = ""
#     return "DCB"[tens - 5] + adjust
#

# #Ascending list
# def is_ascending(items):
#     if len(items) == 0:
#         return True
#     cur = items[0]
#     for item in items[1:]:
#         if cur > item:
#             return False
#         cur = item
#     return True
#
# # Riffle
# def riffle(items, out = True):
#     result=[]
#     items = items[:]
#     if len(items) == 0:
#         return []
#     #print(items)
#     a = int(len(items)/2)
#     list1 = items[:a]
#     list2 = items[a:]
#     for i in range(a):
#         if out:
#             result.extend([list1[i],list2[i]])
#         else:
#             result.extend([list2[i],list1[i]])
#     return result
#
#
# # Only odd digits
# def only_odd_digits(n):
#     while(n>10):
#         digit = n%10
#         n = n//10
#         if (digit%2==0):
#             return False
#     if (n%2==1):
#         return True
#     return False
#
# # Blocks in pyramid
# def pyramid_blocks(n, m, h):
#     result = 0
#     for i in range(h):
#         result += (n+i)*(m+i)
#     return result
#
# #Cyclops numbers
# def is_cyclops(n):
#     if n==0: return True
#     n_as_str = str(n)
#     if (len(n_as_str) % 2) == 0:
#         return False
#     mid = int(len(n_as_str)/2)
#     if n_as_str[mid] == str(0):
#         rest = n_as_str[:mid] + n_as_str[mid+1:]
#         if ("0" not in rest):
#             return True
#     return False
#
# #Domino cycle
# def domino_cycle(tiles):
#     if len(tiles)==0: return True
#     # if len(tiles) ==1:
#     #     if tiles[0][0] ==tiles[0][1]:return True
#     #     else: return False
#     first_item = tiles[0][0]
#     last_item = tiles[0][1]
#     for (f,l) in tiles[1:]:
#         if (last_item != f):
#             return False
#         last_item = l
#     if (last_item != first_item):
#         return False
#     return True
#
# # Count dominators
# def count_dominators(items):
#     if len(items) == 0: return 0
#     if len(items) == 1: return 1
#     num_dominators = 1#this should be 1
#     cur_max = items[-1]
#     for index in range(len(items)-2,-1,-1):
#         if items[index] > cur_max:
#             num_dominators += 1
#             cur_max = items[index]
#     return num_dominators
#
# #Extract increasing integers from digit string
# def extract_increasing(digits):
#     if len(digits) == 0: return []
#     leftover = ""
#     result = [int(digits[0])]
#     for d in digits[1:]:
#         lastIdx = (len(result) - 1)
#         leftover = leftover + d
#         if int(leftover) > result[lastIdx]:
#             result.append(int(leftover))
#             leftover = ""
#     return result
#
#
# # Words that contain given letter sequence
# def words_with_letters(words, letters):
#     result = []
#     for word in words:
#         pos = 0
#         for c in word:
#             if c == letters[pos]:
#                 pos += 1
#                 if pos == len(letters):
#                     break
#
#         if pos == len(letters):
#             result.append(word)
#     return result
#
#
# # Taxi zum zum
# def taxi_zum_zum(moves):
#     pos = (0,0)
#     directions = ['N','E','S','W']
#     cur_dir = 'N'
#     cur_dir_pos = 0
#     for m in moves:
#         if (m == 'L'):
#             cur_dir_pos = cur_dir_pos - 1
#         elif (m == 'R'):
#             cur_dir_pos = cur_dir_pos + 1
#         elif (m == 'F'):
#             moving_dir = directions[abs(cur_dir_pos % 4)]
#             if (moving_dir == 'N'):
#                 pos = (pos[0], pos[1]+1)
#             elif (moving_dir == 'S'):
#                 pos = (pos[0], pos[1] - 1)
#             elif (moving_dir == 'E'):
#                 pos = (pos[0]+1, pos[1])
#             elif (moving_dir == 'W'):
#                 pos = (pos[0]-1, pos[1])
#     return pos
#
# # Arithmetic progression
# def arithmetic_progression(elems):
#     aplist = []
#     if (len(elems) == 0): return []
#     if (len(elems) == 1): return [elems[0],0,1]
#     max_n = 0
#     max_idx = 0
#     for start_idx in range(len(elems)):
#         start = elems[start_idx]
#         for elem in elems[start_idx+1:]:
#             stride = elem - start
#             n = 2
#             while(True):
#                 next = start + stride * n
#                 if next in elems:
#                     n += 1
#                 else:
#                     break
#             if n > max_n:
#                 max_idx = len(aplist)
#                 max_n = n
#             aplist.append((start, stride, n))
#     return aplist[max_idx]
#
# # Tukey's ninther
# def get_median_of_three(ks):
#     ks = sorted(ks)
#     return ks[1]
#
# def tukeys_ninthers(items):
#     if (len(items) == 0): return None
#     if (len(items) == 1): return items[0]
#
#     tempList = items
#     med = tempList[0]
#     while(len(tempList) >= 3):
#         sublist = tempList[:3]
#         del tempList[:3]
#         med = get_median_of_three(sublist)
#         tempList.append(med)
#     return med
#
# # Suppressed digit sum
# def suppressed_digit_sum(n):
#     if (n < 10): return 0
#     unique_nums = set()
#     # generate unique numbers
#     strn = str(n)
#     for skip_idx in range(len(strn)):
#         unique_nums.add(int(strn[:skip_idx] + strn[skip_idx+1:]))
#     return sum(unique_nums)
#
# # duplicated from PythonExamples reference
# def two_summers(items, goal, i = None, j = None):
#     i = i if i else 0
#     j = j if j else len(items) - 1
#     while i < j:
#         x = items[i] + items[j]
#         if x == goal:
#             return True
#         elif x < goal:
#             i += 1
#         else:
#             j -= 1
#     return False
#
# #Three summers ago
# def three_summers(items, goal):
#     for idx in range(len(items)):
#         temp = items[:idx] + items[idx+1:]
#         g = goal - items[idx]
#         if (two_summers(temp, g)):
#             return True
#     return False
#
#
# # Count all sums and products
# def count_distinct_sums_and_products(items):
#     sum_prodect_set = set()
#     if (len(items) < 1): return 0
#     if (len(items) == 1): return 2
#     for i in range(0, len(items)):
#         for j in range(i, len(items)):
#             sum_prodect_set.add(items[i]+items[j])
#             sum_prodect_set.add(items[i]*items[j])
#     return len(sum_prodect_set)
#
# #Try a spatula
# def pancake_scramble(text):
#     order = len(text)
#     # with the magic of string reverse
#     for i in range(2,order+1):
#         text = text[:i][::-1]+text[i:]
#     return text
#
# #Carry on Pythonista
# def count_carries(a, b):
#     nloops = max(len(str(a)),len(str(b)))
#     i = 0
#     num_carry = 0
#     carry = 0
#     while i < nloops:
#         la = a%10
#         lb = b%10
#         carry = (la + lb + carry)//10
#         if carry > 0: num_carry += 1
#         a = a // 10
#         b = b // 10
#         i = i+1
#     if carry: num_carry += 1
#     return num_carry
#
# #First missing positive integer
#
# def first_missing_positive(items):
#     largest = max(items)
#     smallest = min(items)
#     if smallest > 1: return 1
#     uniques = set(items)
#     if (largest + 1) == len(uniques):
#         return (largest + 1)
#     s = sorted(uniques)
#     retval = 1
#     for i in s:
#         if retval == i:
#             retval += 1
#         elif (retval < i):
#             break
#     return retval
#
#
# # Check your permutation
# def is_permutation(items, n):
#     if (n == 0): return False
#     if (len(items) < n): return False
#     expected = set()
#     expected.update(range(1,n+1))
#     for item in items:
#         if item < 1 or item > n:
#             # is outside the range
#             return False
#         if (item not in expected):
#             # is duplicate
#             return False
#         expected.remove(item)
#     return True
#
#
# # Tribonacci
# def tribonacci(n, start = (1, 1, 1)):
#     if n == 0: return start[0]
#     if n == 1: return start[1]
#     if n == 2: return start[2]
#     triplet = (start[0], start[1],start[2])
#     for i in range(3, n+1):
#         next = sum(triplet)
#         triplet = (triplet[1],triplet[2],next)
#     return triplet[2]
#
#
# # Forbidden substrings
# def next_char(word, letters, n, tabu, result):
#     for t in tabu:
#         if len(word) < len(t): continue
#         if t in word:
#             return ""
#     if len(word) == n:
#         result.append(word)
#         return ""
#     for c in letters:
#         next_char(word+c, letters, n, tabu, result)
#
# def forbidden_substrings(letters, n, tabu):
#     word_list = []
#     sorted_letters = "".join(sorted(letters))
#     for c in sorted_letters:
#         next_char(c, sorted_letters, n, tabu, word_list)
#
#     return word_list
#
#
#
# # Keep doubling
# def double_until_all_digits(n, giveup = 1000):
#     iters = 0
#     while iters < giveup:
#         s = set()
#         for a in str(n):
#             s.add(a)
#         # if dict is empty we have seen all digits
#         if len(s) == 10:
#             return iters
#         n = n * 2
#         iters += 1
#
#     return -1
#
# # Remove each item after its k :th occurrence
# def remove_after_kth(items, k = 1):
#     if k == 0: return []
#     seen_items = dict()
#     resultList = list()
#     for item in items:
#         if item not in seen_items:
#             seen_items[item] = 0
#         seen_items[item] += 1
#         if seen_items[item] <= k:
#             resultList.append(item)
#     return resultList
#
#
# def safe_squares_rooks(n, rooks):
#     rows_covered = [rook[0] for rook in rooks]
#     cols_covered = [rook[1] for rook in rooks]
#     rows_covered = list(set(rows_covered))
#     cols_covered = list(set(cols_covered))
#     num_rows_free = n - len(rows_covered)
#     num_cols_free = n - len(cols_covered)
#     if num_cols_free and num_rows_free:
#         return num_rows_free * num_cols_free
#     return 0
#
# # First item that is preceded by k smaller items
# def first_preceded_by_smaller(items, k = 1):
#     if items == None: return None
#     if len(items) == 0: return None
#     if k > len(items): return None
#
#     sorted_list = []
#     for item in items:
#         if len(sorted_list) >= k:
#             # check if item is preceded by k smaller items
#             counter = 0
#             for j in range(len(sorted_list)):
#                 if (sorted_list[j] < item):
#                     counter += 1
#                     if counter == k:
#                         return item
#                 else:
#                     break
#         sorted_list.append(item)
#         sorted_list = sorted(sorted_list)
#
#     return None
#
# # Maximum difference sublist
# def maximum_difference_sublist(items, k = 2):
#     if len(items) == 0: return None
#     if (k == 1): return [items[0]]
#     largest = 0
#     largest_index = None
#     for i in range(len(items)):
#         if (i + k > len(items)):
#             break
#         diff = max(items[i:i+k]) - min(items[i:i+k])
#         if (diff > largest):
#             largest = diff
#             largest_index = i
#
#     return items[largest_index:largest_index+k]
#
# #What do you hear, what do you say?
# def count_and_say(digits):
#     if len(digits) == 0: return ''
#     digitList = []
#     countList = []
#     d = digits[0]
#     c = 1
#     for digit in digits[1:]:
#         if (d == digit):
#             c += 1
#         else:
#             digitList.append(d)
#             countList.append(c)
#             d = digit
#             c = 1
#     digitList.append(d)
#     countList.append(c)
#     result = ""
#     for i in range(len(digitList)):
#         result += str(countList[i]) + digitList[i]
#     return result
#
#
# # Reversing the reversed
# def reverse_reversed(items):
#     result = list()
#     for item in items:
#         revItem = item
#         if type(item) == list:
#             revItem = reverse_reversed(item)
#         result.insert(0, revItem)
#
#     return result

## draft problems


# Count word dominators
def is_word_dominator(a, b):
    yes, no = 0, 0
    for i in range(len(a)):
        if (a[i] > b[i]):
            yes += 1
        else:
            no += 1
    return yes > no

# Count word dominators
def count_word_dominators(words):
    if len(words) == 0: return 0
    if len(words) == 1: return 1
    num_dominators = 1#this should be 1
    cur_max = words[-1]
    for index in range(len(words)-2,-1,-1):
        if is_word_dominator(words[index],cur_max):
            num_dominators += 1
            cur_max = words[index]
    return num_dominators

# # also very slow: about 65 secs
# # Pull down your neighbour
# def eliminate_neighbours(items):
#     if (len(items) == 0): return 0
#     tempItems = items
#     iters = 0
#     sortedItems = sorted(items)
#     while (len(tempItems) != 0):
#         min_idx = tempItems.index(sortedItems[0])
#         left_neigh,right_neigh = -1,-1
#         if (len(tempItems) == 1):
#             # exit when the list has only a single item
#             iters += 1
#             break
#         if (min_idx != 0): left_neigh = tempItems[min_idx-1]
#         if (min_idx != len(tempItems)-1): right_neigh = tempItems[min_idx + 1]
#         neigh = max(left_neigh,right_neigh)
#         iters += 1
#         if (neigh == sortedItems[-1]):
#             # exit when we remove the largest item
#             break
#         tempItems.remove(sortedItems[0])
#         tempItems.remove(neigh)
#         sortedItems.remove(sortedItems[0])
#         sortedItems.remove(neigh)
#     return iters

# # Too slow considering the number of test cases
# # It took about 695 secs to run all the tests
# # Sum of two squares
# import math
# def sum_of_two_squares(n):
#     if n <= 1: return None
#     results = []
#     final_result_idx = 0
#     biggest = 0
#     # factors of n are always less than sqrt(n)
#     n_sqrt = int(math.sqrt(n))
#     print("closest sqrt for {} : {}".format(n, n_sqrt))
#     for i in range(1,n_sqrt+1):
#         for j in range(i, n_sqrt+1):
#             if (i**2 + j**2) == n:
#                 if (i > biggest) or (j > biggest):
#                     final_result_idx = len(results)
#                     biggest = max(i,j)
#                 results.append((i,j))
#     if len(results) > 0:
#         retval = results[final_result_idx]
#         if retval[0] < retval[1]:
#             return (retval[1],retval[0])
#         else:
#             return retval
#     return None

# ### Failed attempts
#
# # Nearest smaller element
# def nearest_smaller(items):
#     resultItems = list()
#     if (len(items) <= 1): return items
#     if (items[0] > items[1]):
#         resultItems.append(items[1])
#     else:
#         resultItems.append(items[0])
#
#     for i in range(1, len(items)-1):
#         smaller = min(items[i-1],items[i],items[i+1])
#         resultItems.append(smaller)
#
#     if (items[-1] > items[-2]):
#         resultItems.append(items[-2])
#     else:
#         resultItems.append(items[-1])
#
#     return resultItems

# # Sum of distinct cubes
# def get_distinct(cubes, n, trialNum):
#     rem = n - (trialNum**3)
#     if (rem <= 0):
#         return rem
#     a = get_distinct(cubes, rem, trialNum)
#
# def sum_of_distinct_cubes(n):
#     # prep a dict of all cubes possible for n
#     cubeDict = dict()
#     num = 1
#     while(True):
#         cubeDict[num] = num ** 3
#         if cubeDict[num] >= n:
#             break
#         num += 1
#
#     results = list()
#     for i in range(num, 0, -1):
#         res = get_distinct(cubeDict, i)
#         sum_of_cubes = 0
#         for r in res:
#             sum_of_cubes += r ** 3
#         if (sum_of_cubes == n):
#             results.append(res)
#
# # Count growlers
# # Question and sample answer is not clear to me
# # does not give correct answer
# def count_growlers(animals):
#     RList, LList = [],[]
#     ld,rd,lc,rc=0,0,0,0
#     growlers = 0
#     for animal in animals[::-1]:
#         if animal is "dog" or animal is "cat":
#             if (ld > lc): growlers += 1
#             if (animal is "dog"): ld += 1
#             if (animal is "cat"): lc += 1
#         elif animal is "god" or animal is "tac":
#             if (rd > rc): growlers += 1
#             if (animal is "god"): rd += 1
#             if (animal is "tac"): rc += 1
#     return growlers
