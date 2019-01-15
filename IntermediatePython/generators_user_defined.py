def simple_gen():
    yield 'Oh'
    yield 'hello'
    yield 'there'
    
for i in simple_gen():
    print(i)
    
CORRECT_COMBO = (3, 6, 1)

# we need to figure out the combo in below  10 X 10 X10 for loop . which is very time consuming and requires lot of code to write while generator will reduce lot of code 
found_combo = False
i=0
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            i+=1
            if (c1, c2, c3) == CORRECT_COMBO:                
                print('Found the combo:{}'.format((c1, c2, c3)),'number of iterations ',i)
                found_combo = True
                break
                
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield(c1,c2,c3)
k=0               
for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    k+=1
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo:{}'.format((c1, c2, c3)),'number of iterations ',i)
        break