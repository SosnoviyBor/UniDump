import task1
import task2
import task3
import task4

while True:
    inp = input("Pick the task to be shown [1-4]: ")
    if inp not in ["1","2","3","4"]:
        print("Wrong input!")
        continue
    print(f"You picked task {inp}")
    match inp:
        case "1":
            # random and determined arrays
            task1.foo()
        case "2":
            # calling negative elements and slicing arrays
            task2.foo()
        case "3":
            # arithmetic operations with arrays
            task3.foo()
        case "4":
            # inspects iris.csv
            task4.foo()
        case _:
            print("Uhm, wrong option?")
    inp = input("Exit? [y/N]: ").lower()
    if inp == "y":
        break
