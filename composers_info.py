from statistics import mean

if __name__ == '__main__':
    try:
        number = int(input("Type number of composers:"))
    except ValueError as err:
        print("This is not number, try again")
    composers = []
    for i in range(number):
        info = input(f'Type full name, year of birth and death of composer number {i + 1}:')
        info = ' '.join([item for item in info.split(" ") if item != ''])
        if len(info.split(" ")) != 4:
            print('Number of parameters is not 4')
            # print(info.split(" "))
            break
        try:
            birth = int(info.split(" ")[2])
            death = int(info.split(" ")[3])
        except ValueError as err:
            print("This is not year, try again")
        composers.append(info)
    avg = []
    for i in range(number):
        duration = int(composers[i].split(" ")[3]) - int(composers[i].split(" ")[2])
        avg.append(duration)
        print(f'First Name: {composers[i].split(" ")[0]}, Last Name: {composers[i].split(" ")[1]}, Age:  {duration}')
    print(f'Average duration of life of give composers is {mean(avg)}')
