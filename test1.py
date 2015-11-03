import regex as re

with open('F:/College Park/More Than 500.txt') as file:
    for firm in file:

        print(re.sub('[^A-Za-z0-9]+ ', '', firm[firm.strip().find('and')+5:firm.strip().find('#80')]))
