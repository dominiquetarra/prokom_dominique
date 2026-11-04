#import module_name
import exercise8_16_function
exercise8_16_function.make_pizza(16, 'pepperoni')

#from module_name import function_name
from exercise8_16_function import make_pizza
make_pizza(12, 'mushroom')

#from module_name import function_name as fn
from exercise8_16_function import make_pizza as mp
mp(14, 'cheese')

#import module_name as mn
import exercise8_16_function as e816f
e816f.make_pizza(10, 'green pepper')

#from module_name import *
from exercise8_16_function import *
make_pizza(13, 'smoked beef')
