import timeit
# to  check how much time it took to execute a perticular method or logic

print('generator time',timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = list(i for i in input_list if div_by_two(i))
''', number=50000))

print('List time',timeit.timeit('''input_list = range(100)

def div_by_two(num):
    if (num/2).is_integer():
        return True
    else:
        return False

# generator:
xyz = [i for i in input_list if div_by_two(i)]''', number=50000))