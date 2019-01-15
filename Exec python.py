# Exec compiles and evaluates what we send in string form its like compiler in compiler. This is dangerous to run on virtual private servers like webservers
exec("print('so this works like eval')")

list_str = "[5,6,2,1,6]"
list_str = exec(list_str)
print(list_str)

# it looks like miracle please observe below. we defined data related to the list in exec and trying to print which will consider and print
exec("list_str2 = [1,5,7,8,2]") # the sttement inside exec is considered as if this is defined in the code
print(list_str2)

exec("def test(): print('oooo snap!!!')")
test()

exec("""
def test2():
    print('lets see if multi line works....')
""")

test2()