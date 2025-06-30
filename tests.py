first = input("1st letter:")
sec = input("2nd letter:")
thir = input("3rd letter:")

if first > sec and first < thir and thir > sec:
    print("The letter in the middle is", first)
elif sec > first and sec < thir and thir > first:
    print("The letter in the middle is", sec)
elif thir < first and thir > sec and first > sec:
    print("The letter in the middle is", thir)






