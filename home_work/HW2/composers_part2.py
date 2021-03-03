def input_loop():
    composers = {"Name": [], "Surname": [], "BirthYear": [], "DeathYear": []}
    while True:
        info = input(f'Type full name, year of birth and death of composer: ')
        info = ' '.join([item for item in info.split(" ") if item != ''])
        if len(info.split(" ")) != 4:
            print('Number of parameters is not 4')
            exit(1)
        try:
            birth = int(info.split(" ")[2])
            death = int(info.split(" ")[3])
        except ValueError as err:
            print("This is not year, try again")
            print(f'Error: {err}')
            exit(1)
        composers["Name"].append(info.split(" ")[0])
        composers["Surname"].append(info.split(" ")[1])
        composers["BirthYear"].append(birth)
        composers["DeathYear"].append(death)
        answ = input("Do you want to continue ?(Y/n): ")
        if answ in ['y', 'Y', 'yes', 'Yes']:
            continue
        elif answ in ['n', 'N', 'No', 'no']:
            break
        else:
            print("I didn't get it, so continue")
    return composers


def estimate_duration(composers=None):
    if composers:
        if all(k in composers for k in ["BirthYear", "DeathYear"]):
            composers["Duration"] = []
            for birth, death in zip(composers["BirthYear"], composers["DeathYear"]):
                composers["Duration"].append(death - birth)
        else:
            print(f'Wrong dictionary keys content')
            exit(1)
    return composers


def mean_duration(composers=None):
    if composers:
        if "Duration" in composers:
            dur_sum = 0
            for dur in composers["Duration"]:
                dur_sum += dur
            avg = dur_sum / len(composers["Duration"])
            print(f'Average composers life duration is {avg}')
        else:
            print(f'Wrong dictionary keys content')
            exit(1)


def print_composers(composers=None):
    if composers:
        if all(k in composers for k in ["Name", "Surname", "Duration"]):
            for i, v in enumerate(composers["Name"]):
                print(f'First Name: {v}, Last Name: {composers["Surname"][i]} '
                f'Age: {composers["Duration"][i]}')



if __name__ == '__main__':
    comp = input_loop()
    comp = estimate_duration(comp)
    # в задании не было, но если предполагалось, то раскомментируй
    #print_composers(comp)
    mean_duration(comp)
