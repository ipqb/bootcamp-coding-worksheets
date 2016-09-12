#!/bin/python
import math
import random


last_names_list = ['Lewis','Reder','Tan','Natale','Town','Khoroshkin','Marin','Arhar','Ary','Bergman','Chio','Dai','Dickinson','Elledge','Kirkemo','Lou','Maxwell','Oltion','Rohweder','Schwarz','Tsai','Wassarman','Wu']

first_names_list = ['Greyson','Gabriel','Sophia','Andrew','Jason','Matvei','Wesley','Taylor','Beatrice','Ian','Cynthia','Shizhong','Sasha','Susanna','Lisa','Kevin','Alison','Keely','Peter','Daniel','Kaitlyn','Douglas','Taia']

program_list = ['BP','BP','BP','BP','BMI','BMI','BMI','CCB','CCB','CCB','CCB','CCB','CCB','CCB','CCB','CCB','CCB','CCB','CCB','CCB','CCB','CCB','CCB']

first_to_last_name_dict = dict(zip(first_names_list, last_names_list))

last_to_first_name_dict = dict(zip(last_names_list, first_names_list))

name_to_program_dict = dict(zip(first_names_list, program_list))


def part_1():
    '''
    -> There are many ways for us to match an item in a list with its index
    -> Let's start with range
    ---> When we use range we can specify START, STOP, and STEP
    ---> range(y) will start at index 0 and the last index will be y-1
    ---> range(x, y) will start at index x and the last index will be y-1
           and each round will move the index up by 1
    ---> range(x, y, z) will start and stop at the same place as before,
           but now each round will increase the index by z

    1) Right now range will simply print a first name and its index,
        update range to print every other name 
    '''
    for index in range(len(first_names_list)):
        print first_names_list[index], index
    '''
    -> Now let's use enumerate
    ---> Using enumerate in a for loop will give you the index and item in a list
    ---> for index, item_at_index in enumerate(list_1)

    2) The each index in the lists above is associated to a specific person. Use 
        enumerate to print the first name, last name, and program of each student
    '''
    ##### put code here #####

         
def part_2():
    '''
    -> Try and except can allow you to get passed errors
    -> When using a dict you might ask for the value of a specific key, but
        that key is not in the dict. This will crash you program and say
        KeyError: 'whatever your bad key was'

    ---> random_name_list contains a list of both first and last names. 

    1) for each name in the list try to look up the last name by using the 
        name as a key for the first_to_last_name_dict. Use except to get around
        the error and then use the last_to_first_name_dict to look up the first 
        name. Print the correct first and last names. 

    '''
    first_and_last_names = first_names_list + last_names_list
    random_name_list = random.sample(first_and_last_names, 6)
    for name in random_name_list:
        try:
            pass ##### put code here #####
        except KeyError:
            pass ##### put code here #####

def part_3():
    '''
    Using while will continue to run until it meets the stop condition 

    1) Use while to make a dict with programs as the keys and the lists
        of students in a program as the value

    '''
    program_to_student_list_dict = {}
    ##### put code here #####
    
    print program_to_student_list_dict['BP']
    print program_to_student_list_dict['BMI']
    print program_to_student_list_dict['CCB']

def part_4():
    number_of_students = len(first_names_list)
    number_groups = 6 
    '''
    To find the ideal group size we can take the ceiling (round up) of the
    number of students divided by the number of groups 

    *** note if using python 2.7 make sure both variables are floats
    before you divide them or it will become an int ***

    After finding the ideal group size it might be a good idea to 
    turn it into an int
    '''
    ##### put code here #####
    #print ideal_group_size

    '''
    The ideal number of students would then be = ideal group size * number of groups
    '''
    ##### put code here #####
    #print ideal_number_of_students
    '''
    There is a difference between the ideal number of students and the actual number 

    Lets make a list with the length equal to the number of students 

    Fill this list with ones for all indices up to the actual number of students 

    Then make the rest of the indices = 0
    '''

    ##### put code here #####
    #print binary_student_list

    '''
    ->Now we want to use a for loop to make a list in a fun way called list comprehension
    ---> This is how it should look:

    new_list = [ SOME TYPE OF OPERATION for index in range(START INDEX, STOP INDEX, STEP INDEX) ]

    ---> For an example lets us this:

    new_list = [ index*3 for index in range(0, 13, 2) ]

    Round 1:
    index = 0
    new_list.append(0*3) 
    Round 2:
    index = 2
    new_list.append(2*3)
    ...
    Last Round:
    index = 12
    new_list.append(12*3)

    Output:
    new_list = [0, 6, 12, 18, 24, 30, 36]

    ---> Another way to use this is to split a sequence into codons:
    sequence = 'ATGCAGATTTTCGTCAAGACTTTGACCGGTAAAACC'
    codon_list = [ sequence[index:index+3] for index in range(0, len(sequence), 3) ]
    Output:
    codon_list = ['ATG', 'CAG', 'ATT', 'TTC', 'GTC', 'AAG', 'ACT', 'TTG', 'ACC', 'GGT', 'AAA', 'ACC']

    1) make a list that holds the number of students in each group using this 
    ---> For each round we should take the sum of a temporary list: 
            binary_student_list[index: index+ideal_group_size]
            and then increase the index by the ideal_group_size until we reach
            the end of the binary_student_list

    '''
    ##### put code here #####

def part_5():
    '''
    1) Use the group size list from part_4 to make 6 groups of students such 
        that there is at least one iPQB student in each group (BMI or BP)
    '''



part_1()







