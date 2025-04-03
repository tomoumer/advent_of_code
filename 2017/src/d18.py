# Day 18 of 2017
import re
from collections import deque

# =========== CLASSES AND FUNCTIONS =============
class Program():

    def __init__(self, programID, instruction_in, registers):
        self.programID = programID
        self.instruction_in = instruction_in
        self.received = deque([])
        self.status = 'ready'
        self.registers = registers
        self.num_sent = 0

    def get_status(self):
        return self.status

    def assembling(self, instructions, other_program):

        while True:
            # print(self.programID, self.instruction_in)
            # program got out of bounds and is therefore finished
            if (self.instruction_in < 0) | (self.instruction_in > len(instructions) - 1):
                self.status = 'done'
                break

            instruction = instructions[self.instruction_in]
            self.instruction_in += 1

            if ('snd' in instruction) | ('rcv' in instruction):
                command, val1 = instruction.split()

            else:
                command, val1, val2 = instruction.split()
                if re.match('-?\d+', val2):
                    val2 = int(val2)
                else:
                    val2 = self.registers[val2]

            if re.match('-?\d+', val1):
                reg_val1 = int(val1)
            else:
                reg_val1 = self.registers[val1]

            match command:

                case 'snd':
                    other_program.received.append(reg_val1)
                    self.num_sent += 1

                case 'set':
                    self.registers[val1] = val2

                case 'add':
                    self.registers[val1] += val2

                case 'mul': 
                    self.registers[val1] *= val2

                case 'mod': 
                    self.registers[val1] = reg_val1 % val2

                case 'rcv': 
                    if len(self.received) == 0:
                        self.status = 'waiting' 
                        # have to return to this same instruction next time
                        self.instruction_in -= 1
                        break
                    else:
                        received_value = self.received.popleft()
                        self.registers[val1] = received_value

                case 'jgz': #X Y'
                    if reg_val1 > 0:
                        # note the -1 is because I increment instruction in each loop
                        self.instruction_in = self.instruction_in -1 + val2
     

def get_or_create_register(val, registers):
    
    # existing register
    if val in registers.keys():
        reg_val = registers[val]

    # new register
    else:
        registers[val] = 0
        reg_val = 0

    return reg_val


def assemble_away(instructions):
    registers = dict()
    instruction_in = 0

    while True:
        instruction = instructions[instruction_in]
        instruction_in += 1

        if ('snd' in instruction) | ('rcv' in instruction):
            command, val1 = instruction.split()

        else:
            command, val1, val2 = instruction.split()
            if re.match('-?\d+', val2):
                val2 = int(val2)
            else:
                val2 = get_or_create_register(val2, registers)

        # this both creates a register for val1, and gets its value
        reg_val1 = get_or_create_register(val1, registers)

        match command:

            case 'snd':
                last_sound = reg_val1

            case 'set':
                registers[val1] = val2

            case 'add':
                registers[val1] += val2

            case 'mul': 
                registers[val1] *= val2

            case 'mod': 
                registers[val1] = reg_val1 % val2

            case 'rcv': 
                if reg_val1 != 0:
                    return last_sound, registers

            case 'jgz': #X Y'
                if reg_val1 > 0:
                    # note the -1 is because I increment instruction in each loop
                    instruction_in = instruction_in -1 + val2
                

# =============== TEST CASES ====================
test_instructions = ['set a 1',
'add a 2',
'mul a a',
'mod a 5',
'snd a',
'set a 0',
'rcv a',
'jgz a -1',
'set a 1',
'jgz a -2']

assert assemble_away(test_instructions)[0] == 4

# =============== PART 1 & 2 ====================
instructions = []

with open('./2017/inputs/d18.txt') as f:
    for row in f:
        instructions.append(row.strip())

last_sound, registers = assemble_away(instructions)

# since the run in part 1, might as well just initialize all registers for each program
program_zero = Program(0, 0, {k:0 for k in registers.keys()})
program_one = Program(1, 0, {k:1 if k=='p' else 0 for k in registers.keys()})


while (program_zero.status == 'ready') | (program_one.status == 'ready'):

    if program_zero.status == 'ready':
        # print('first program running')
        program_zero.assembling(instructions, program_one)
    elif program_one.status == 'ready':
        # print('second program running')
        program_one.assembling(instructions, program_zero)

    if (program_zero.status == 'waiting') & (len(program_zero.received) > 0):
        program_zero.status = 'ready'
    if (program_one.status == 'waiting') & (len(program_one.received) > 0):
        program_one.status = 'ready'

print('Part 1 solution:', last_sound)
print('Part 2 solution:', program_one.num_sent)