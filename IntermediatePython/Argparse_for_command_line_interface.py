import argparse
import sys
# tutorial https://pythonprogramming.net/argparse-cli-intermediate-python-tutorial/
def main():
    parser=argparse.ArgumentParser() # we can assue ArgumentParser as a class and parser as object because it the ArgumentParseris in capital leters in it
    parser.add_argument('--x',type=float,default=1.0,
                     help="What is the first Number")
    parser.add_argument('--y',type=float,default=1.0,
                     help="What is the second Number")
    parser.add_argument('--operation',type=str,default='add',
                     help="What operation?(add, sub,mul,div)")
    args =parser.parse_agrs()
    sys.stdout.write(str(calc(args)))
                 

# convert the below function through command line interface with argparse
def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y
                            
                                
if __name__ == '__main__':
     main()                                
                                        
