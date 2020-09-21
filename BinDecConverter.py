
#Whether from bin to dec or vice cersa
def Checker(number):
    if '.' in number:
        s = {'0','1'}
        p = set(number)
        p.remove('.')
        return s == p or p == {'0'} or p =={'1'}   
    else: 
        s = {'0','1'}
        p = set(number)
        return s == p or p == {'0'} or p =={'1'}  

#when bin conversion
def binConvert(number):
    fH = []
    if '.' in number:
        binary = number.split('.')
        firstHalf = binary[0]
        secondHalf = binary[1]
        sH = []
        count1 = 0
        count2 = 1
        for num in reversed(firstHalf):
            fH.append(int(num)*(2**count1))
            count1 = count1 + 1
        for num in secondHalf:
            sH.append(int(num)*(2**(-(count2))))
            count2 = count2 + 1
        decimal = str((sum(fH))+ (sum(sH)))
        print(decimal)
    else:
        NoDec = number
        count = 0 
        for num in reversed(NoDec):
            fH.append(int(num)*(2**count))
            count = count + 1
        print(sum(fH))



#when dec conversion
def decConvert(num):
    if num > 1:
        decConvert(num // 2)
    print (num % 2)
        

if __name__ == "__main__":
    while True:
        number = input("Enter the number ")
        if Checker(number):
            binConvert(number)
        else:
            decConvert(int(number))
        cont = input(("Do you wish to continue ? Y for YES and N for NO").lower())
        if cont =='y':
            continue
        else:
            break
#agar 10 daala problem 