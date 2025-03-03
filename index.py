# Perfect number
def perfectnumber(num):
    if num<=0:
        return "Enter a Valid Number"
    sum = 1
    for i in range(2, (num//2)+1):
        if num%i == 0:
            sum+=i   
    return "Perfect Number" if sum == num else "Not a Perfect Number"
print(perfectnumber(32))
print(perfectnumber(6))


# lcm of two number
def lcm(num1, num2):
    if num1>num2:
        big = num1
    else:
        big = num2
    while(True):
        if (big % num1 == 0 and big%num2 ==0):
            return big
        big+=1
print(lcm(21,40))



# gcd of two number
def gcd(num1, num2):
    if num1<num2:
        small = num1
    else:
        small = num2
    while(True):
        if (num1 % small == 0 and num2%small ==0):
            return small
        small-=1
print(gcd(21,45))


# sum of odd digits
def sumOfOdd(number):
    sum=0
    while(number):
        digit = number%10
        if digit%2 != 0:
            sum+=digit
        number//=10
    return sum
print(sumOfOdd(1234567))



# sum of non prime
def sumOfNonPrime(number):
    sum=0
    while(number):
        digit = number%10
        for i in range(2,digit//2 +1):
            if digit % i == 0:
                digit=0
        sum+=digit
        number//=10
    return sum
print(sumOfNonPrime(34567))

