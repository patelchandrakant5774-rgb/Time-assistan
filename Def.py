def calc_sum (a,b):
    sum = a+b 
    print (sum)
    return (sum)
calc_sum(4,7)
calc_sum(87,54)
def calc_sub (a,b):
    return a-b
sub = calc_sub(87,45)
print (sub)
def calc_mult(a,b):
    return a*b
multi = calc_mult(4,7)
print(multi)
def calc_div(a,b):
    if b == 0:           
        return "Bhai 0 se divide nahi hota!"
    return a/b
div = calc_div(8,7)
print(div)
div2= calc_div(7,0)
print (div2) 
