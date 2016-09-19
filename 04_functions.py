# The code below extracts log messages from a file ('simulation_00.dat').  Each 
# log message starts with either "info:", "warn:", or "error:".  The log 
# messages are extracted into a new file with the same name as the original, 
# but in a directory with the same name as the log message.  For example, all 
# the "info" lines would be extracted into 'info/simulation_00.dat'.  You might 
# write something like this to check the results of a long simulation.

# Part 1:
# Rewrite the code below using functions to remove as much duplication as 
# possible.

import os

with open('simulation_00.dat') as file:
    info_lines = []
    for line in file:
        if line.startswith('info:'):
            info_lines.append(line)

if info_lines:
    if not os.path.exists('info'):
        os.mkdir('info')
    with open('info/simulation_00.dat', 'w') as file:
        for line in info_lines:
            file.write(line)

with open('simulation_00.dat') as file:
    warn_lines = []
    for line in file:
        if line.startswith('warn:'):
            warn_lines.append(line)
            print line.strip()

if warn_lines:
    if not os.path.exists('warn'):
        os.mkdir('warn')
    with open('warn/simulation_00.dat', 'w') as file:
        for line in warn_lines:
            file.write(line)

with open('simulation_00.dat') as file:
    error_lines = []
    for line in file:
        if line.startswith('error:'):
            error_lines.append(line)
            print line.strip().upper()

if error_lines:
    if not os.path.exists('error'):
        os.mkdir('error')
    with open('error/simulation_00.dat', 'w') as file:
        for line in error_lines:
            file.write(line)

# Part 2:
# Modify your program to process simulations 01 through 09, in addition to 
# simulation 00.
#
# Part 3:
# Modify your program to extract the "trace:" and "debug:" log levels in 
# addition to "info:", "warn:", and "error:".
#
# Part 4:
# Modify your program to extract any lines that aren't part of a log message 
# (i.e. that don't start with one of the five specified prefixes.)
#
# Part 5:
# Modify your program to append today's date to beginning of each file you're 
# extracting.  For example, instead of extracting to 'error/simulation_00.dat', 
# extract to 'error/20160919_simulation_00.dat'.  You can use the following 
# code to get to today's date:

import datetime
datetime.date.today().strftime('%Y%m%d')
