c = [-44, -96, 81, -85, -99, 76, -36, -8, 11, -93, 0, -8, 86, 26, 93, -48, -64, -31, 20, 40, -39, 86, -78, -81, -29, -89, 56, 53, 75, -71, 66, 58, -62, 0, 76, -71, 72, -45, 47, 94, 13, 87, 28, 32, -31, -92, 94, 94, -5, 19, -32, -3, -100, 93, -50, 75, 3, -18, 46, 81, 19, -85, -49, 98]

b = [-1,-2,-3,]
def positive_sum(arr):
    i = 0
    for x in arr:
       if x > 0:
           i = i + x
    return i

def sum_array(a):
    x = 0
    for i in a:
        x = i + x
    if a == []:
        return 0


print sum_array(b)