a='**********EVEN/odd checker**********'
print(a.center(130))
def check():
    i =int(input(" Enter a Number:"))
    match i:
        case _ if i%2==0:
            print('The Entered Number Is Even.')
        case _ :
            print('The Entered Number Is Odd.')
check()