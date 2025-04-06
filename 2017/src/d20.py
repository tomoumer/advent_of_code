# Day 20 of 2017
import numpy as np
import pandas as pd

# =========== CLASSES AND FUNCTIONS =============
def make_particles_collide(particles, time_elapsed):

    for _ in range(time_elapsed):
        for coord in ['x', 'y', 'z']:
            particles[f'vel_{coord}'] = particles[f'vel_{coord}'] + particles[f'acc_{coord}']
            particles[f'pos_{coord}'] = particles[f'pos_{coord}'] + particles[f'vel_{coord}']

        # flag duplicate positions
        particles['is_collision'] = particles.duplicated(subset=['pos_x', 'pos_y', 'pos_z'], keep=False)
        particles = particles.loc[particles['is_collision'] == False]

    return particles

# =============== TEST CASES ====================
test_particles = [
    'p=< 3,0,0>, v=< 2,0,0>, a=<-1,0,0>',
    'p=< 4,0,0>, v=< 0,0,0>, a=<-2,0,0>'
]

min_acc = 100000
min_p_num = -1

for i, particle in enumerate(test_particles):
    p_pos, p_vel, p_acc = particle.split(', ')
    p_acc_x, p_acc_y, p_acc_z = map(int, p_acc[3:-1].split(','))
    p_acc_total = abs(p_acc_x) + abs(p_acc_y) + abs(p_acc_z)

    if p_acc_total < min_acc:
        min_acc = p_acc_total
        min_p_num = i

assert min_p_num == 0

test_particles = [
'p=<-6,0,0>, v=< 3,0,0>, a=< 0,0,0>',
'p=<-4,0,0>, v=< 2,0,0>, a=< 0,0,0>',
'p=<-2,0,0>, v=< 1,0,0>, a=< 0,0,0>',
'p=< 3,0,0>, v=<-1,0,0>, a=< 0,0,0>'
]

tmp_particles = []

for i, particle in enumerate(test_particles):
    p_pos, p_vel, p_acc = particle.split(', ')
    p_pos = list(map(int, p_pos[3:-1].split(',')))
    p_vel = list(map(int, p_vel[3:-1].split(',')))
    p_acc = list(map(int, p_acc[3:-1].split(',')))
    tmp_particles.append({'pos_x': p_pos[0],
                          'pos_y': p_pos[1],
                          'pos_z': p_pos[2], 
                          'vel_x': p_vel[0],
                          'vel_y': p_vel[1],
                          'vel_z': p_vel[2],
                          'acc_x': p_acc[0],
                          'acc_y': p_acc[1],
                          'acc_z': p_acc[2],
                          })

particles = pd.DataFrame(tmp_particles)


particles = make_particles_collide(particles,5)

assert len(particles) == 1
assert particles['vel_x'].values[0] == -1

# =============== PART 1 & 2 ====================
min_acc = 100000
min_p_num = -1
tmp_particles = []

with open('./2017/inputs/d20.txt') as f:
    for i, row in enumerate(f):
        p_pos, p_vel, p_acc = row.strip().split(', ')
        p_pos = list(map(int, p_pos[3:-1].split(',')))
        p_vel = list(map(int, p_vel[3:-1].split(',')))
        p_acc = list(map(int, p_acc[3:-1].split(',')))

        p_acc_total = abs(p_acc[0]) + abs(p_acc[1]) + abs(p_acc[2])
        
        if p_acc_total < min_acc:
            # print(p_acc_x, p_acc_y, p_acc_z)
            # print(p_acc_total)
            min_acc = p_acc_total
            min_p_num = i

        tmp_particles.append({'pos_x': p_pos[0],
                        'pos_y': p_pos[1],
                        'pos_z': p_pos[2], 
                        'vel_x': p_vel[0],
                        'vel_y': p_vel[1],
                        'vel_z': p_vel[2],
                        'acc_x': p_acc[0],
                        'acc_y': p_acc[1],
                        'acc_z': p_acc[2],
                        })     


particles = pd.DataFrame(tmp_particles)
particles = make_particles_collide(particles, 1000)


print('Part 1 solution:', min_p_num)
print('Part 2 solution:', particles.shape[0])