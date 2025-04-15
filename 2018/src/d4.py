# Day 4 of 2018
from datetime import datetime
import re
import numpy as np

# =========== CLASSES AND FUNCTIONS =============
def process_guard_schedule(guard_schedule):

    date_format = '%Y-%m-%d %H:%M'
    cleaned_guard_schedule = []

    for guard_event in guard_schedule:
        tmp_event = []

        timestamp = guard_event[1:17]
        timestamp = datetime.strptime(timestamp, date_format)
        tmp_event.append(timestamp)

        if 'Guard' in guard_event:
            tmp_event.append(int(re.search('#(\d+)', guard_event).group(1)))
        elif 'asleep' in guard_event:
            tmp_event.append('asleep')
        else:
            tmp_event.append('awake')

        cleaned_guard_schedule.append(tmp_event)

    cleaned_guard_schedule.sort(key=lambda x: x[0])
    return cleaned_guard_schedule

def get_guards(cleaned_guard_schedule):

    guards=dict()
    current_guard = -1

    for guard_event in cleaned_guard_schedule:

        # change guard whose schedule it is
        if isinstance(guard_event[1], int):
            current_guard = guard_event[1]

            if current_guard not in guards:
                guards[current_guard] = []
        else:
            # no need for any other checks because the way I sorted it earlier
            # it's always asleep - awake pairs
            guards[current_guard].append(guard_event[0])

    return guards

def sleepy_sleepy_guard(guards):
    # part 1
    time_asleep = 0
    most_asleep_guard = -1
    most_asleep_min = 0

    # part 2 
    repeat_asleep_min = 0
    num_repeat_asleep = 0
    repeat_asleep_guard = -1

    for guard, times in guards.items():

        tmp_asleep = 0
        # I couldn't think of a better way to do this ...
        sleepy_hour = np.zeros(60)

        for i in range(1, len(times), 2):
            # it's always the same hour
            tmp_asleep += (times[i].minute - times[i-1].minute)
            sleepy_hour[times[i-1].minute: times[i].minute] += 1

        if tmp_asleep > time_asleep:
            time_asleep = tmp_asleep
            most_asleep_guard = guard
            most_asleep_min = np.argmax(sleepy_hour)

        tmp_num_repeat = np.max(sleepy_hour)

        if tmp_num_repeat > num_repeat_asleep:
            repeat_asleep_min = np.argmax(sleepy_hour)
            num_repeat_asleep = tmp_num_repeat
            repeat_asleep_guard = guard


    return most_asleep_min * most_asleep_guard, repeat_asleep_min * repeat_asleep_guard


# =============== TEST CASES ====================
guard_schedule = ['[1518-11-01 00:00] Guard #10 begins shift',
'[1518-11-01 00:05] falls asleep',
'[1518-11-01 00:25] wakes up',
'[1518-11-01 00:30] falls asleep',
'[1518-11-01 00:55] wakes up',
'[1518-11-01 23:58] Guard #99 begins shift',
'[1518-11-02 00:40] falls asleep',
'[1518-11-02 00:50] wakes up',
'[1518-11-03 00:05] Guard #10 begins shift',
'[1518-11-03 00:24] falls asleep',
'[1518-11-03 00:29] wakes up',
'[1518-11-04 00:02] Guard #99 begins shift',
'[1518-11-04 00:36] falls asleep',
'[1518-11-04 00:46] wakes up',
'[1518-11-05 00:03] Guard #99 begins shift',
'[1518-11-05 00:45] falls asleep',
'[1518-11-05 00:55] wakes up']

guard_schedule = process_guard_schedule(guard_schedule)
guards = get_guards(guard_schedule)
sleep_combo1, sleep_combo2 = sleepy_sleepy_guard(guards)
assert sleep_combo1 == 240
assert sleep_combo2 == 4455

# =============== PART 1 & 2 ====================
guard_schedule = []

with open('./2018/inputs/d4.txt') as f:
    for row in f:
        guard_schedule.append(row.strip())

guard_schedule = process_guard_schedule(guard_schedule)
guards = get_guards(guard_schedule)
sleep_combo1, sleep_combo2 = sleepy_sleepy_guard(guards)

print('Part 1 solution:', sleep_combo1)
print('Part 2 solution:', sleep_combo2)