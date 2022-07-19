import random
from secrets import randbits

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"
    
def make1():
    racers = open('racers.txt', encoding='utf-8')
    racers = racers.read()
    racers = racers.split('\n')[1:]

    z = ''

    for i in racers:
        l = i.split()
        z += 'INSERT INTO racers VALUES('
        z += f"    '{l[0]}',\n"
        z += f"    '{l[1]}',\n"
        z += f"    '{l[2]}',\n"
        z += f"    {l[3]},\n"
        z += f"    {l[4]},\n"
        z += f"    to_date('{l[5]}', 'DD-MM-YYYY')\n"
        z += f"    {random.randint(10, 35)}0000\n"
        z += ');'


    with open('ready\\racers.txt', 'w', encoding='utf-8') as f:
        f.write(z)

def make2():
    cars = open('cars.txt', encoding='utf-8')
    cars = cars.read()
    cars = cars.split('\n')[1:]

    racers = open('racers.txt', encoding='utf-8')
    racers = racers.read()
    racers = racers.split('\n')[1:]

    for i in range(len(cars)):
        l_cars = cars[i].split('|')
        l_racers = racers[i].split()
        print('INSERT INTO cars VALUES(')
        print(f"    {l_racers[3]},")
        print(f"    '{l_cars[0]}',")
        print(f"    '{l_cars[1]}',")
        print(f"    {random.randint(700, 900)},")
        print(f"    {toFixed(random.uniform(1, 4), 2)},")
        print(f"    to_date('{random.randint(1, 25)}-{random.randint(1, 12)}-{random.randint(1997, 2018)}', 'DD-MM-YYYY')")
        
        print(');')


def make3():
    l = [
        'Red Bull', 
        'Vodafone', 
        'Shell', 
        'Honda', 
        'Toyota', 
        'Red Bull', 
        'Mercedes-Benz', 
        'BMW Group',
        'Marlboro',
        'Renault',
        'Bridgestone',
        'ING',
        'Petronas',
        'Intel',
        'Panasonic',
        'Lenovo',
        'RBS',
        'Puma',
        'Aigo',
        'Metro',
        'Santander',
        'Alice'
        'Petrobras',
        'Pvaxx',
        'Denso'
    ]

    racers = open('racers.txt', encoding='utf-8')
    racers = racers.read()
    racers = racers.split('\n')[1:]

    for i in racers:
        l_racers = i.split()

        ran = random.randint(2, 10)
        sponsors = []
        for i in range(ran):
            while True:
                spon = l[random.randint(0, len(l)-1)]
                if spon not in sponsors:
                    sponsors.append(spon)
                    break

        for j in range(ran):
            print('INSERT INTO sponsors VALUES(')
            print(f"    {l_racers[3]},")
            print(f"    '{sponsors[j]}',")
            print(f"    {toFixed(random.uniform(0, 3), 3)},")

            print(');')

def make_racers_txt():
    racers = open('racers.txt', encoding='utf-8')
    racers = racers.read()
    racers = racers.split('\n')[1:]

    team_names = [
         'Loco Kings',
 'Masked Bats',
 'Calypso Rangers',
 'Dynasty Wizards',
 'Psychodelic Defenders', 
 'Hurricane Phenoms',
 'Ice Cold Musketeers', 
 'Clever Bombers',
 'Excellent Roos',
 'All Camels',
 'Mean Top Dogs', 
 'Ancient Force',
 'Psychodelic Dutchmen', 
 'Striped Kings', 
 'Renowned Watchmen', 
 'Supreme Skywalkers', 
 'Serious Lords', 
 'Striped Commanders', 
 'Fiery Brewers',
 'Dynasty Stars', 
 'Clever Doves', 
 'Atlantic Wreckers', 
 'The Fat Flames', 
 'Atlantic Jazz', 
 'Drunk Squires', 
 'Regal Mafia', 
 'Hustlin Ravens', 
 'Brute Raiders', 
 'Odd Elephants', 
 'Hellish Mafia', 
 'Merry Slammers', 
 'Lady Mambas', 
 'Hurricane Vixens', 
 'Epic Hippos', 
 'Grave Champs', 
 'Hidden Ravens', 
 'Wild Fighters', 
 'Hustlin Cajuns', 
 'Brute Flames', 
 'Ball Admirals', 
 'Colossal Cheetahs', 
 'Net Wizards', 
 'Grand Tigers', 
 'Awesome Cubs', 
 'Prime teams', 
 'Loco Eagles', 
 'Loco Champions', 
 'Savage Hoopsters', 
 'Colossal Boars', 
 'Hellish Bananas' ]

    z = ''
    n = 0
    for i in racers:
        l = i.split()
        z += f"'{l[0]}'|"
        z += f"'{l[1]}'|"
        z += f"'{l[2]}'|"
        z += f"{l[3]}|"
        z += f"{team_names[n]}|"
        z += f"{l[4]}|"
        z += f"to_date('{l[5]}', 'DD-MM-YYYY')|"
        z += f"{random.randint(10, 35)}0000\n"
        n+=1

    with open('ready\\racers.txt', 'w', encoding='utf-8') as f:
        f.write(z)


def make_cars_txt():
    cars = open('cars.txt', encoding='utf-8')
    cars = cars.read()
    cars = cars.split('\n')[1:]

    racers = open('ready\\racers.txt', encoding='utf-8')
    racers = racers.read()
    racers = racers.split('\n')

    z = ''

    for i in range(len(cars)):
        l_cars = cars[i].split('|')
        l_racers = racers[i].split('|')
        z += f"{l_racers[3]}|"
        z += f"'{l_cars[0]}'|"
        z += f"'{l_cars[1]}'|"
        z += f"to_date('{random.randint(1, 25)}-{random.randint(1, 12)}-{random.randint(1997, 2018)}', 'DD-MM-YYYY')|"
        z += f"{random.randint(700, 900)}|"
        z += f"{toFixed(random.uniform(1, 4), 2)}|"
        z += f"{random.randint(270, 400)}"
        z += '\n'

    with open('ready\\cars.txt', 'w', encoding='utf-8') as f:
        f.write(z)

def make_team_txt():
    cars = open('ready\\cars.txt', encoding='utf-8')
    cars = cars.read()
    cars = cars.split('\n')

    racers = open('ready\\racers.txt', encoding='utf-8')
    racers = racers.read()
    racers = racers.split('\n')

    z = ''

    for i in range(len(cars)):
        l_cars = cars[i].split('|')
        l_racers = racers[i].split('|')

        z += f"{l_racers[4]}|"
        z += f"{random.randint(100, 999)}|"
        z += f"to_date('{random.randint(1, 25)}-{random.randint(1, 12)}-{random.randint(1997, 2018)}', 'DD-MM-YYYY')|"
        z += f"{random.randint(10, 20)}"
        z += '\n'

    with open('ready\\team.txt', 'w', encoding='utf-8') as f:
        f.write(z)

def make_sponsors_txt():
    cars = open('ready\\cars.txt', encoding='utf-8')
    cars = cars.read()
    cars = cars.split('\n')

    team = open('ready\\team.txt', encoding='utf-8')
    team = team.read()
    team = team.split('\n')

    racers = open('ready\\racers.txt', encoding='utf-8')
    racers = racers.read()
    racers = racers.split('\n')

    z = ''

    l = [
        'Red Bull', 
        'Vodafone', 
        'Shell', 
        'Honda', 
        'Toyota', 
        'Red Bull', 
        'Mercedes-Benz', 
        'BMW Group',
        'Marlboro',
        'Renault',
        'Bridgestone',
        'ING',
        'Petronas',
        'Intel',
        'Panasonic',
        'Lenovo',
        'RBS',
        'Puma',
        'Aigo',
        'Metro',
        'Santander',
        'Alice'
        'Petrobras',
        'Pvaxx',
        'Denso'
    ]

    z = ''

    for i in range(len(cars)):
        l_team = team[i].split('|')
        l_cars = cars[i].split('|')
        l_racers = racers[i].split('|')

        ran = random.randint(2, 10)
        sponsors = []
        for i in range(ran):
            while True:
                spon = l[random.randint(0, len(l)-1)]
                if spon not in sponsors:
                    sponsors.append(spon)
                    break

        for j in range(ran):
            z += f"{l_team[1]}|"
            z += f"'{sponsors[j]}'|"
            z += f"{toFixed(random.uniform(0, 3), 3)}"
            z += '\n'

    with open('ready\\sponsors.txt', 'w', encoding='utf-8') as f:
        f.write(z)


def make_requ_txt():
    racers = open('ready\\racers.txt', encoding='utf-8')
    racers = racers.read()
    racers = racers.split('\n')
    
    cars = open('ready\\cars.txt', encoding='utf-8')
    cars = cars.read()
    cars = cars.split('\n')

    team = open('ready\\team.txt', encoding='utf-8')
    team = team.read()
    team = team.split('\n')

    sponsors = open('ready\\sponsors.txt', encoding='utf-8')
    sponsors = sponsors.read()
    sponsors = sponsors.split('\n')
    
    z = ''

    for i in range(len(racers)):
        l_racers = racers[i].split('|')

        z += 'INSERT INTO racers VALUES(\n'
        for j in range(len(l_racers)-1):
            z += f'    {l_racers[j]},\n'

        z += f'    {l_racers[-1]}\n'
        z += ');\n'
        
    for i in range(len(cars)):
        l_cars = cars[i].split('|')

        z += 'INSERT INTO cars VALUES(\n'
        for j in range(len(l_cars)-1):
            z += f'    {l_cars[j]},\n'

        z += f'    {l_cars[-1]}\n'
        z += ');\n'

    for i in range(len(team)):
        l_team = team[i].split('|')

        z += 'INSERT INTO team VALUES(\n'
        for j in range(len(l_team)-1):
            z += f'    {l_team[j]},\n'

        z += f'    {l_team[-1]}\n'
        z += ');\n'

    for i in range(len(sponsors)):
        l_sponsors = sponsors[i].split('|')

        z += 'INSERT INTO sponsors VALUES(\n'
        for j in range(len(l_sponsors)-1):
            z += f'    {l_sponsors[j]},\n'

        z += f'    {l_sponsors[-1]}\n'
        z += ');\n'
        


    with open('ready\\requ.txt', 'w', encoding='utf-8') as f:
        f.write(z)

def make_ready_request_txt():
    add_table_requ = open('ready\\add_table_requ.txt', encoding='utf-8')
    add_table_requ = add_table_requ.read()
    
    requ = open('ready\\requ.txt', encoding='utf-8')
    requ = requ.read()

    z = add_table_requ + '\n' + requ 
    with open('ready\\ready_request.txt', 'w', encoding='utf-8') as f:
        f.write(z)


make_ready_request_txt()
