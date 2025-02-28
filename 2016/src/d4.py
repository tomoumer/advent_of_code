# Day 4 of 2016
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

# =========== CLASSES AND FUNCTIONS =============
def decode_room(encoded_room):
    encoded_room = encoded_room.replace('-', '')
    room_chksum = encoded_room[-6:-1]
    sector_id =  int(encoded_room[-10:-7])

    encoding = encoded_room[:-10]
    # count the letters and frequency
    encoding = Counter(encoding)
    # sort the dictionary based on number of appearances and then alphabet
    encoding = {k: v for k, v in sorted(encoding.items(), key=lambda item: (-item[1], item[0]))}
    encoded_key = ''
    for i, key in enumerate(encoding.keys()):
        if i <5:
            encoded_key = encoded_key + key

    if room_chksum == encoded_key:
        return sector_id
    else:
        return 0
    
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def shift_cypher(encoded_room):
    global alphabet

    sector_id =  int(encoded_room[-10:-7])
    encoding = encoded_room[:-10]

    unencoded_room = ''
    for letter_enc in encoding:
        if letter_enc == '-':
            unencoded_room = unencoded_room + ' '
        else:
            # how many letters to get to end of alphabet
            len_to_end = len(alphabet) - alphabet.find(letter_enc)
            # how many letters in alphabet to shift
            num_in_order = (sector_id - len_to_end) % 26
            # add new letter
            unencoded_room = unencoded_room + alphabet[num_in_order]

    return unencoded_room, sector_id


# =============== TEST CASES ====================
test_rooms = {'aaaaa-bbb-z-y-x-123[abxyz]': True,
              'a-b-c-d-e-f-g-h-987[abcde]': True,
              'not-a-real-room-404[oarel]': True,
              'totally-real-room-200[decoy]': False}

test_sum = 0
for test_room, _ in test_rooms.items():
    test_sum += decode_room(test_room)

assert test_sum == 1514

# ================= PART 1 ======================
rooms = []

with open('./2016/inputs/d4.txt') as f:
    for row in f:
        rooms.append(row.strip())


decrypt_sum = 0
actual_rooms = [] # for part 2
for room in rooms:
    room_value = decode_room(room)
    decrypt_sum += room_value

    if room_value > 0:
        actual_rooms.append(room)

print('Part 1 solution:', decrypt_sum)

# ================= PART 2 ======================
unencoded_rooms = []
for room in actual_rooms:
    unencoded_room, room_value = shift_cypher(room)
    unencoded_rooms.append(unencoded_room)

    if 'northpole' in unencoded_room:
        decrypt_value = room_value

# room names are super fun lol
# print(unencoded_rooms)

print('Part 2 solution:', decrypt_value)

# fun stuff!
# note stopwords are not needed, but in general can be
stopwords = set(STOPWORDS)
all_room_words = " ".join(unencoded_rooms)

wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                stopwords = stopwords,
                min_font_size = 10).generate(all_room_words)
 
# plot the WordCloud image                       
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.savefig(f'./2016/img/rooms_wordcloud_d4.png', bbox_inches='tight', pad_inches=0)
plt.close()