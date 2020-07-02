Sample_Input= '''2
e
Test sentence
Tester sentence
a
The ACM International Collegiate Programming Contest
The Association for Computing Machinery’s Collegiate Programming Contest'''
Sample_output = '''Differences 2 and 6
Differences 31 and 33'''



##### TASK #####
# Compute minimum changes
# Add
# Remove
# Substitute

# Replace with C with @
# Compute minimum changes


def min_edit_dist(s1,s2,to_check_s1, to_check_s2):
    if to_check_s1 == 0:
        return to_check_s2;

    elif to_check_s2 == 0:
        return to_check_s1

    if s1[to_check_s1] == s2[to_check_s2]:
        check = 0
    else:
        check = 1
    return min(min_edit_dist(s1,s2,to_check_s1 -1, to_check_s2) + 1, min_edit_dist(s1,s2,to_check_s1, to_check_s2 - 1)+1, min_edit_dist(s1,s2,to_check_s1-1,to_check_s2-1)+check)

        
#### PSUDO ####

input_ = Sample_Input.split('\n')
output_list = []

for i in range(1,len(input_)):
    input_[i] = list(input_[i])


for i in range(int(input_[0])):
    # find s1 and s2
    
    s1 = input_[3*i + 2]
    s2 = input_[3*i + 3]
    output_list.append(min_edit_dist(s1,s2,len(s1)-1,len(s2)-1))
    print('done {}'.format(i+1))
    
   

    
            
    




'''
output = ''
if output == Sample_output:
    print('Success')
'''
