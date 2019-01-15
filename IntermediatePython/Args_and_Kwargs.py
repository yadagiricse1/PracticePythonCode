# args are like list where as kwargs keyword arguments are like dictionaries  args are some what similar to sum(String...s) like passing one or more strings in Java
# for agrs there will be only one star where as for kwargs 2 stars
# we can also write methods that that accepts both args and kwargs myblog_posts(*args,**kwargs)
blog_1 = 'I am so awesome'
blog_2 = 'Cars are cool.'
blog_3 = 'Aww look at my cat.'


'''
def blog_posts(*args):
    for post in args:
        print(post)
    
#blog_posts(blog_1)    
blog_posts(blog_1,blog_2,blog_3)
'''

'''
def blog_posts(title,*args):
    print(title)
    for post in args:
        print(post)
site_title='My Blogs'      
#blog_posts(site_title) # here i didnt pass any arguments except title
#blog_posts(site_title,blog_1)
blog_posts(site_title,blog_1,blog_2,blog_3)
'''

site_title='My Blogs' 
def blog_posts_kw(title,**kwargs):
    print(title)
    for p_title,post in kwargs.items():
        print(p_title,post)
        
#blog_posts_kw(site_title) # no arguments

blog_posts_kw(site_title,blog_1 = 'I am so awesome',
                         blog_2 = 'Cars are cool.',
                         blog_3 = 'Aww look at my cat.')
def blog_posts_args_kwargs(title,*args,**kwargs):
    print(title)
    for arg in args:
        print(arg)
    for p_title,post in kwargs.items():
        print(p_title,post)

print("below is args and kwargs calling  ")
blog_posts_args_kwargs(site_title,'1','2','3',blog_1 = 'I am so awesome',
                         blog_2 = 'Cars are cool.',
                         blog_3 = 'Aww look at my cat.')
                        
                        
