#Braden Leach
#January 13 2024
#Local Scope Challenge




#----1----#

# def greet(fname):
#     print(f'Hello, {fname} your name is a local scope!')
# greet('braden')

#----2----#
def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return word
count_vowels(word = 'parameter')




#----3----#
