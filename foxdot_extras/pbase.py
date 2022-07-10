from timeit import repeat
from FoxDot import *

'''Change from base 10 to any base'''
def from_10_to_anybase(number, base):
    '''Returns any base 10 number to any base given #Maximum base - 36'''
    from_base10_to_anybase_num = [] # Initialize the number in any base
    while number > 0: # Iterate while the number is greater than zero
        remainder = int(number % base) # change remainder in integer
        #from_base10_to_anybase_num.append( remainder )
        from_base10_to_anybase_num.insert(0, remainder )
        number //= base # take the integer part after division
    
    #print("number", number, "base", base, from_base10_to_anybase_num)
    return from_base10_to_anybase_num

#@loop_pattern_func
def PBase(num, b=2, l=1):
    ''' Returns the 'n' number in base 'b' split into digits.
        e.g. `PBase(5)` will return `P[1,0,1]`
        gets a pattern by converting the input number (might work with strings etc too) 
    '''
    number_list = [int(i) for i in from_10_to_anybase(num, b)]
    
    while(len(number_list) < l):
        number_list.insert(0, 0)
    
    #print("from_10_to_anybase("+str(num)+","+str(base)+")", number_list)
    
    return Pattern( number_list )

#print(PBase(5, b=5, minlen=5))