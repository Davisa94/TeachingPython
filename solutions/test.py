

def fizz_buzz():
    var = ""
    num = 1
    while num < 100:
        # Reset var to prevent issues of adding buzz to buzz or buzz to fizzbuz
        var = ""
        #print(num)
        # if num % 3 == 0 and num % 5 == 0:
        #     var = "fizz_buzz"
        #    continue
        if num % 3 == 0:
            print("number is :" + str(num))
            var = "fizz"
        if num % 5 == 0:
            var += "buzz"
        else:
            var = num
        print("\t" + str(var))
        num += 1

fizz_buzz()

