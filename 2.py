import sys
S = sys.argv[1]
number_list = S.split(",")
evenlist = []
sum = 0
evensum = 0
for i in range(len(number_list)):
    if(int(number_list[i])>0):
        if(int(number_list[i]) % 2 == 0):
            evenlist.append(int(number_list[i]))
            evensum += int(number_list[i])
        sum += int(number_list[i])
rate = float("{0:.3f}".format(evensum/float(sum)))
print('Even numbers: "' + str(evenlist)[1:-1] + '"')
print("Sum of even numbers: " + str(evensum))
print("Even Number Rate: " + str(rate))
