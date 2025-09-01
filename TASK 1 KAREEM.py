temperature =24
if temperature >= 30:
    print("Its a hot day.stay hydrated!")
elif 20<= temperature <=29:
    print("Its a warm day.Enjoy the weather!")
elif 10<= temperature <=19:
    print("Its a cool day.Wear a jacket!")
else :
    print("Its a cold day.Stay Warm!")




    numbers = list (range (1,21))
    print(f"All numbers: {numbers}")
    print("Numbers divisible by 3:")
    for num in numbers:
     if num %3 == 0:
        print(num)