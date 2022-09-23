import math

# define/build the function
# Type hinting
def calc_pythagoras(a: float, b: float, rounding: int=1, return_sqrd=False) -> float:
    '''
    This is a function that applies the Pythagoras theorem

    Parameters:
        * a: a side 
        * b: b side
    
    Returns:
        * c

    '''
    # create a local variable
    c_sqrd = math.pow(a, 2) + math.pow(b, 2)
    c = math.sqrt(c_sqrd)
    c_rounded = round(c, rounding)

    if return_sqrd:
        return c_rounded, c_sqrd
    else:
        return c_rounded

# use the function
my_c, my_c_sqrd = calc_pythagoras(a=10, b=15, return_sqrd=True)


