# Phillipos Admasu
# This code takes an input text file with 4 sections separated with tabs/spaces and outputs a content in a specific format. 

import re

input_file = r" " # Put path to input text file here. Make sure there are no newlines at the end of text doc. 
				  # *Doesn't affect functionality.*

final_file = r" " # Put a path to where you'd like the output file to be written. An empty text document works best.

with open(input_file) as og:
    with open(final_file, 'w+') as final:
        for _,line in enumerate(og):
            initial = re.sub('\s\t+',' ',line).split()  #This makes a line break after every Data unit.
            print(initial[0] + ', ' + initial[1], file = final)
            print("Images: " + initial[2], file = final)
            print('Pathway: ' + initial[3], file = final)
            print('', file = final)
        print("Done")