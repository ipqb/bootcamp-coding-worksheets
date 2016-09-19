#!/usr/bin/env python2

import random, subprocess

random.seed(10)

log_levels = [
        'trace: ',
        'debug: ',
        'info:  ',
        'warn:  ',
        'error: ',
        ''
]

num_inputs = 10
num_fortunes = 15

for i in range(num_inputs):
    input_path = 'simulation_{:02d}.dat'.format(i)
    with open(input_path, 'w') as file:
        for i in range(num_fortunes):
            log_level = random.choice(log_levels)
            fortune = subprocess.check_output('fortune').strip()
            for line in fortune.split('\n'):
                file.write(log_level + line + '\n')
            if log_level.startswith('error'):
                break





