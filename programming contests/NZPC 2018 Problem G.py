# Author: Josh Keegan
# Date: Who Cares
# NZPC 2018 Problem G.py
##


string = input('')                    #INPUT
#string = '18 = 25 + -6'

# Define variables
chains = []
string_chain = False
prev_link_was_coma_or_dot = False
# Make the string a list
string = list(string)

# Reverse the order of the input
string = string[::-1]

# Find chains of numbers
for c in range(len(string)):
    try:
        int(string[c])                  # Find intergers
        if prev_link_was_coma_or_dot:
            prev_link_was_coma_or_dot = False
            
        if not string_chain:            # Find the start of a chain
            start = c
            string_chain = True
            
        if c == len(string)-1:          # Account last position
            chains.append((start,c+1))
    except:                             # Find other characters
        if string_chain and (string[c] == ',' or string[c] == '.'):
            prev_link_was_coma_or_dot = True
            
        elif prev_link_was_coma_or_dot:           # If it is a string following a coma dont add coma to chain
            chains.append((start,c-1))
            prev_link_was_coma_or_dot = False

        elif string_chain:                # If there has been a chain
            if string[c] == '-' or string[c] == '+':    # Add plus and minus to the chain
                pass
            else:
                string_chain = False        
                chains.append((start,c))    # Add the start and finish of the chain to chains
                                            # (Start, Finish)
        else:
            pass

# Reverse the chains in the string 
for loc in chains:                      # Get each tupple of chain start finishes
    l = []                              # Redifine new list of characters every time
    for c in range(loc[0],loc[1]):      # c goes from start to finsish of each chain
        l.append(string[c])             # Add each character in a chain to l
    l = l[::-1]                         # Reverse extracted chain
    for a in range(loc[0],loc[1]):      # Replace the values of the extracted chain with the old ones
        string[a] = l[a-loc[0]]

# Create output
output = ''                             
for i in string:
    output += i

#Display output
print(output)
