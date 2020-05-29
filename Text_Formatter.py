import re

input_file = r" " #Insert path to text file here
final_file = r" " #Insert path to text file here. Name it how you want. This will create a text file in pathway provided. 

with open(input_file) as og:
    with open(final_file, 'w+') as final:
        for _,line in enumerate(og):
            initial = re.sub('\s\t+',' ',line).split()  #This makes a line break after every Data unit.
            print(initial[0] + ', ' + initial[1], file = final)
            print("Images: " + initial[2], file = final)
            print('Pathway: ' + initial[3], file = final)
            print('', file = final)