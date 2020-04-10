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
#     elif ones > 6:
#         adjust = "+"
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
# # def is_cyclops(n):
# #     if n==0: return True
# #     n_as_str = str(n)
# #     print("{},{},{}".format(n_as_str, type(n_as_str), len(n_as_str)))
# #     if (len(n_as_str) % 2) == 0:
# #         return False
# #     mid = int(len(n_as_str)/2)
# #     if n_as_str[mid] == str(0):
# #         return True
# #     return False
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
# #Count dominators
# # def count_dominators(items):
# #     if len(items) == 0: return 0
# #     if len(items) == 1: return 1
# #     num_dominators = 1#this should be 1
# #     cur_max = items[-1]
# #     for index in range(len(items)-2,-1,-1):
# #         if items[index] > cur_max:
# #             num_dominators += 1
# #             cur_max = items[index]
# #     return num_dominators
#
# #Extract increasing integers from digit string
#
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
# #Words that contain given letter sequence
# # def words_with_letters(words, letters):
# #     result = []
# #     for word in words:
# #         pos = 0
# #         for c in word:
# #             if c == letters[pos]:
# #                 pos += 1
# #                 if pos == len(letters):
# #                     break
# #
# #         if pos == len(letters):
# #             result.append(word)
# #     return result
#
# #Sum of two squares
# # import math
# # def sum_of_two_squares(n):
# #     if n <= 1: return None
# #     results = []
# #     final_result_idx = 0
# #     biggest = 0
# #     # factors of n are always less than sqrt(n)
# #     n_sqrt = int(math.sqrt(n))
# #     for i in range(1,n_sqrt+1):
# #         for j in range(i, n_sqrt+1):
# #             if (i**2 + j**2) == n:
# #                 if (i > biggest) or (j > biggest):
# #                     final_result_idx = len(results)
# #                     biggest = max(i,j)
# #                 results.append((i,j))
# #     if len(results) > 0:
# #         retval = results[final_result_idx]
# #         if retval[0] < retval[1]:
# #             return (retval[1],retval[0])
# #         else:
# #             return retval
# #     return None
#
# #Try a spatula
#
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
# # # Factoring factorials
# # # this program has a high runtime cost
# # cached_max = 1
# # cached_primes = []
# # def get_prime_numbers(n):
# #     global cached_max
# #     global cached_primes
# #     if (n < cached_max):
# #         return [p for p in cached_primes if p < n]
# #     result = []
# #     if (n > 1):
# #         start = 1
# #         if (cached_max > start):
# #             start = cached_max
# #             result.extend(cached_primes)
# #         for i in range(1+start, n+1):
# #             isPrime = True
# #             for a in range(2, i):
# #                 if (i % a == 0):
# #                     isPrime = False
# #                     break
# #             if isPrime: result.append(i)
# #     cached_primes = result
# #     cached_max = n
# #     return result
# #
# # def get_num_divisible(n, divisor):
# #     start = 1
# #     count = 0
# #     for i in range(start+1, n+1):
# #         if (i % divisor == 0):
# #             count += 1
# #     return count
# #
# # def factoring_factorial(n):
# #     if (n == 1):
# #         return []
# #     primes = get_prime_numbers(n)
# #     result = []
# #     # based on Legendre's Theorem
# #     for prime in primes:
# #         divisor = prime
# #         loop = 1
# #         count = 0
# #         while True:
# #             c = get_num_divisible(n, divisor)
# #             if (c > 0):
# #                 count += c
# #                 loop += 1
# #                 divisor = prime ** (loop)
# #             else:
# #                 break
# #         if (count == 0): result.append((prime,1))
# #         else: result.append((prime,count))
# #     return result
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

# First item that is preceded by k smaller items
def first_preceded_by_smaller(items, k = 1):
    if len(items) == 0: return None
    if k > len(items): return None
    return None

# Maximum difference sublist
def maximum_difference_sublist(items, k = 2):
    if len(items) == 0: return None
    if (k == 1): return [items[0]]
    largest = 0
    largest_index = None
    for i in range(len(items)):
        if (i + k > len(items)):
            break
        diff = max(items[i:i+k]) - min(items[i:i+k])
        if (diff > largest):
            largest = diff
            largest_index = i

    return items[largest_index:largest_index+k]

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

