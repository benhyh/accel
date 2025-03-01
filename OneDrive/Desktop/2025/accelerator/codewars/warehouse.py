def remove_exclaimation_marks(str):
    result = str

    for char in str:
        if char != '!':
            result += char
    
    return result

def reverse_seq(n):
    return list(range(n, 0, -1))

def multi_table(number):
    result = ""
    for i in range(1, 11):
        result += f"{i} * {number} = {i * number}\n"
    return result.rstrip()

def quarter_of(month):
    return (month - 1) // 3 + 1

# split the string into words and add the length of the word to the word
# "apple ban" --> ["apple 5", "ban 3"]
def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]

def reverse(st):
    words = st.split()
    words.reverse()

    return " ".join(words)

def pipe_fix(nums):
    result = []

    for i in range(nums[0], nums[-1] + 1):
        result.append(i)

    return result

def remove_every_other(my_list):
    for i in range(len(my_list) - 1, -1, -1):
        if i % 2 != 0:
            my_list.pop(i)
    return my_list

    # or 
    return my_list[::2]

def string_to_array(s):
    if s == "":
        return [""]
    return s.split()

def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

def DNA_strand(dna):
    dnaDict = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }

    return "".join(dnaDict[char] for char in dna)

def xo(s):
    return s.lower().count("o") == s.lower().count("x")

def number(bus_stops):
    ## return sum([stop[0] = stop[1] for stop in bus_stops])
    count = 0
    for pair in bus_stops:
        count += pair[0]
        count += pair[1]
    pass

def sort_by_length(arr):
    # return sorted(arr, key=len)
    
    n = len(arr)

    swapped = True
    
    while swapped:
        swapped = False

        for i in range(n - 1):
            if len(arr[i]) > len(arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
    
    return arr

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else: 
        return 0

def arithmetic(a, b, operator):
    if operator.lower() == "add":
        return a + b
    elif operator.lower() == "subtract":
        return a - b
    elif operator.lower() == "multiply":
        return a * b;
    elif operator.lower() == "divide":
        return a / (b * 1.0);

def greet(name):
    print(f"Hello, {name} how are you doing today?")  

def rental_car_cost(d):
    rent = 40
    if d >= 7:
        return (rent * d) - 50
    elif d >= 3:
        return (rent * d) - 20
    else:
        return d * rent
    
def find_short(s):
    # return min(len(x) for x in s.split())
    return len(sorted(s.split(), key=len)[0]) 

def how_much_i_love_you(nb_petals):
    return ["not at all", "I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6]

def plural(n):
    return n != 1

def factorial(n):
    if n < 0 or n > 12:
        raise ValueError("Input must be between 0 and 12")
    
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    
    return result

    #  if n < 0 or n > 12:
        # raise ValueError
    # return 1 if n <= 1 else n*factorial(n-1)

def mouth_size(animal):
    if animal.lower() == "alligator":
        return "small"
    else:
        return "wide"

def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))

def unsual_five():
    return len("hello")
