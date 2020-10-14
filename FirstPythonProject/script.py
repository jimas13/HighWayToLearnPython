
#excercise 3
score = input("Enter Score: ")
s = float(score)

if s<0.0 and s>1.0:
    if s>= 0.9:
    	print('A')
	elif s>=0.8:
    	print('B')
	elif s>=0.7:
    	print('C')
	elif s>=0.6:
    	print('D')
	elif s<0.6:
    	print('F')
else:
    print("Error")

#excercise 2
hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h <= 40.0 :
    gross = h * r
else:
	gross = (40 * r) + ((h - 40) * (r * 1.5))
print(gross)
