# Day 7 of 2018
from copy import deepcopy
import numpy as np

# =========== CLASSES AND FUNCTIONS =============
def parse_instructions(instructions):

    steps = dict()

    for instruction in instructions:
        # fixed positions
        # print(instruction[5], instruction[-12])
        step1 = instruction[5]
        step2 = instruction[-12]

        if step1 not in steps:
            steps[step1] = []
        if step2 not in steps:
            steps[step2] = []

        steps[step2].append(step1) 

    # sort in order
    steps = {k: v for k, v in sorted(steps.items(), key=lambda item: item[0])}

    return steps

def follow_steps(steps):

    code = ''

    while True:
        # find the first step that is accessible, i.e
        # its corresponding list is empty
        for key in steps.keys():

            if len(steps[key]) == 0:
                current_step = key
                break

        del steps[current_step]
        code = code + current_step

        if len(steps) == 0:
            break

        # remove the current step from other steps
        for key in steps.keys():
            if current_step in steps[key]:
                steps[key].remove(current_step)

    return code

def multi_worker_steps(steps, num_workers, base_time):

    elapsed_time = 0

    step_time = {letter : i+1+base_time for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ')}
    workers = np.zeros(num_workers)
    work_letters = ['' for i in range(num_workers)]


    while True:

        elapsed_time += 1

        workers -= np.ones(num_workers)
        just_finished_workers =  np.argwhere(workers == 0)

        if len(just_finished_workers) > 0:
            for worker_num in just_finished_workers:
                finished_step = work_letters[worker_num[0]]

                # remove the finished step from other steps
                for key in steps.keys():
                    if finished_step in steps[key]:
                        steps[key].remove(finished_step)

                work_letters[worker_num[0]] = ''

        # get free workers (or rather their indices)
        free_workers = np.argwhere(workers<=0)

        if len(free_workers) == 0:
            continue

        if len(steps) > 0:
            for worker_num in free_workers:
                found_work = False
                for key in steps.keys():

                    if len(steps[key]) == 0:
                        current_step = key
                        found_work = True
                        break
                
                if found_work:
                    del steps[current_step]
                    workers[worker_num[0]] = step_time[current_step]
                    work_letters[worker_num[0]] = current_step

        elif len(steps) == 0 and len(np.argwhere(workers > 0)) == 0:
            # because I increment this at the beginning of loop
            elapsed_time -= 1
            break
         
    return elapsed_time


# =============== TEST CASES ====================
instructions = ['Step C must be finished before step A can begin.',
'Step C must be finished before step F can begin.',
'Step A must be finished before step B can begin.',
'Step A must be finished before step D can begin.',
'Step B must be finished before step E can begin.',
'Step D must be finished before step E can begin.',
'Step F must be finished before step E can begin.']

steps = parse_instructions(instructions)
code = follow_steps(deepcopy(steps))
time_to_complete = multi_worker_steps(steps, 2, 0)
assert code == 'CABDFE'
assert time_to_complete == 15

# =============== PART 1 & 2 ====================
instructions = []

with open('./2018/inputs/d7.txt') as f:
    for row in f:
        instructions.append(row.strip())

print('input rows', len(instructions))

steps = parse_instructions(instructions)
code = follow_steps(deepcopy(steps))
time_to_complete = multi_worker_steps(steps, 15, 60)

print('Part 1 solution:', code)
print('Part 2 solution:', time_to_complete)
