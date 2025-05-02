print('**********PALINDROME_CHECKER**********'.center(150))
def palindrome():
    i = input('Enter a word: ').strip()
    j = i.upper()
    lst1=[a for a in j]
    lst2=lst1.copy()
    lst2.reverse()
    if lst1 == lst2:
        print(i,"is a palindrome")
    else:
        print(i,'is not a palindrome')
palindrome()