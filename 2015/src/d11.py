# Day 11 of 2015

# NOTE: yeah this one really didn't need a class... but I like class Santa!

class Santa():
    
    def __init__(self, password):
        self.password = password

    def next_letter(self, letter):
        if letter == 'z':
            return 'a'
        else:
            new_letter = chr(ord(letter) + 1)    
            return new_letter
    
    # change password, one letter at a time ..
    def change_pwd(self, position):
        reset = ''
        updated = ''
        unchanged = ''

        # in cases i, o or l are present this will reset the rest to all a
        if position < len(self.password) - 1:
            reset = 'a' * len(self.password[position+1 :])

        for pos in range(position, -1, -1):
            old_letter = self.password[pos]
            new_letter = self.next_letter(old_letter)
            updated = new_letter + updated

            if new_letter != 'a':
                break
        
        # once the letters don't increment , the rest is unchanged
        unchanged = self.password[:pos]

        self.password = unchanged + updated + reset


    def check_pwd(self):

        # first check for letters that immediately break the pwd
        for wrong_char in ['i', 'o', 'l']:
            position = self.password.find(wrong_char)
            if position != -1:
                self.change_pwd(position)
                return False
            
        doubles = dict()
        has_consecutive = False
        for first, second, third in zip(self.password, self.password[1:], self.password[2:]):

            if len(doubles.keys()) < 2:
                if first == second:
                    doubles[first] = 1 # note don't care how many of the same pairs we have
            
            if not has_consecutive:
                if (self.next_letter(first) == second) and (self.next_letter(second) == third) and (second != 'a') and (third != 'a'):
                    has_consecutive = True

        # due to how zip works, need to check last two after the loop ends for doubles
        if len(doubles.keys()) < 2:
            if second == third:
                doubles[second] = 1


        if (len(doubles.keys()) == 2) & (has_consecutive):
            return True
        else:
            # change last letter
            self.change_pwd(len(self.password) - 1)
            return False
        
    def reset_pwd(self, password):
        self.password = password



# ================= PART 1 ======================

santa = Santa('')


test_passwords = {'abcdefgh': 'abcdffaa',
                  'ghijklmn': 'ghjaabcc'}

for wrong_pwd, new_pwd in test_passwords.items():
    santa.reset_pwd(wrong_pwd)

    acceptable_pwd = False
    while not acceptable_pwd:
        acceptable_pwd = santa.check_pwd()

    assert santa.password == new_pwd, f"Password {santa.password} don't match {new_pwd}"


# load in the actual puzzle input
with open('./2015/inputs/d11.txt') as f:
    for j, row in enumerate(f):
        santa_pwd = row.strip()

santa.reset_pwd(santa_pwd)

acceptable_pwd = False
while not acceptable_pwd:
    acceptable_pwd = santa.check_pwd()

print('Part 1 solution:', santa.password)

# ================= PART 2 ======================

# it expired, so need to change it by incrementing
santa.change_pwd(len(santa.password) - 1)

acceptable_pwd = False
while not acceptable_pwd:
    acceptable_pwd = santa.check_pwd()

# hxbyyzaa
print('Part 2 solution:', santa.password)