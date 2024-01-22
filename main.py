from random import randint

num = randint(1, 10)
print(num)

nums = input("Вгадай число: ")
print("Ви ввели номер :", nums)

if str(num) == nums:
    print("Вгадав!!!")
else:
    if nums.isalnum():
        if nums.isdigit():
            nums = int(nums)
            if nums < 1:
                print("Число меньше 1")
            elif nums > 10:
                print("Число бiльше 10")
            elif 1 <= nums <= 10:
                print("Ти був близько")
        else:
            print("Введiть цiле чило, а не букви")
    else:
        print("Введи цiле число")