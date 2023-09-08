
if __name__ == '__main__':
    names = []
    ages = []
    while True:
        info = input("Write your name and age please: ")
        info = ' '.join([item for item in info.split(" ") if item != ''])
        if len(info.split(" ")) != 2:
            print("Number of parameters should be 2")
            continue
        try:
            age = int(info.split(" ")[1])
        except ValueError as err:
            print("Second parametr is not age")
            exit(1)
        names.append(info.split(" ")[0])
        ages.append(age)
        answ = input("Do you want to continue ?(Y/n): ")
        if answ in ['y', 'Y', 'yes', 'Yes']:
            continue
        elif answ in ['n', 'N', 'No', 'no']:
            break
        else:
            print("I didn't get it, so continue") 

    avg = 0
    for age, name in zip(ages, names):
        print(f'Name is {name}, age is {age}')
        avg += age
    print(f'Average age is {avg // len(ages)}')
    print(1)
    print(2)
    print(3)
    print(4)
