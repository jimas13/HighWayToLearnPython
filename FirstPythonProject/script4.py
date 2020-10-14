def Maximum(array):
    return max(array)

def Minimum(array):
    return min(array)

array = []
while True:
    num = input("Enter a number: ")
    if num == "done" :
        break
    else:
        try:
            array.append(int(num))
            print(array)
        except:
            print("Invalid input")

print("Maximum is", Maximum(array))
print("Minimum is", Minimum(array))
