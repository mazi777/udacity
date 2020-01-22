## Your code should check if each number in the list is a prime number

check_prime = [26, 39, 51, 53, 57, 79, 85]
number_list=[]

## write your code here

for number in check_prime:

    for i in range(2,6):
        if number%i==0 and number!=i:
            number_list.append(1)
        else:
            number_list.append(0)
    #print("list for number {}: {}". format(number,number_list))
    try:
        if number_list.index(1)>=0:

            #print("index for number 1 {}=".format(number_list.index(1)))
            print("{} is NOT a prime number, because {} is a factor of {}".format(number,number_list.index(1)+2,number))
    except:
            print("{} IS a prime number".format(number))
    number_list =[]
