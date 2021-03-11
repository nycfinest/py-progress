
import math

# def say_hello(name):
#     print("Hello", name)
    


    
# def double_num(numb):
#     return numb * 2

def quad_form(a, b, c):
    result_one = (-b + math.sqrt((b ** 2) - (4 * a * c)))/(2 * a)
    result_two = (-b - math.sqrt((b ** 2) - (4 * a * c)))/(2 * a)
    return result_one, result_two
    
    
    # result_two = 0
    
    # return a, b, c 
    



if __name__ == "__main__":
    x = quad_form(2, -3, -18)
    y = quad_form(-3, 4, 20)
    print(y)