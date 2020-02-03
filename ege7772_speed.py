import sys
import datetime




def fill_array():
    print("Enter array of numbers that will exist more than 8 elements or equal...")
    arr = list(map(int, input().split()))
    res = (all(element < 1000 for element in arr) and all(element >= 0 for element in arr)) #check each element for required state
    
    if ( (len(arr) >= 8) and res and (len(arr) < 10000) ):
        return arr
    else:
        print("You entered incorrect array.")
        sys.exit()


test_arr = fill_array() #getting a new array from console
start = datetime.datetime.now()
print("In process...")
max_i = len(test_arr) - 8
max_multiple = 0

for i in range(max_i):
    for j in range(i+8, len(test_arr)): 
        if( (test_arr[j] * test_arr[i]) > max_multiple):
            max_multiple = test_arr[j] * test_arr[i]

print("The max multiplication = " + str(max_multiple))
finish = datetime.datetime.now()
print (finish-start)
