#Load a list of first names
#load a list of surnames
#Choose a first name at random
#assign the name to a variable
#choose a surname at random
#assign the name to a variable
#print the names to the screen in order and in red font
#ask the user to quit or play again
#if user plays again:
    #repeat
#if user quits:
    #end and exit
import sys
import random
import time

print('Welcome to the Pyschiatric Ward')
time.sleep(2)
print('You were admitted because you were..')
time.sleep(2)

first = ('Dog', 'Behavioral issues stemming from', 'Thundercats',
         'Beastality','Dragon', 'Basilisk', 'UFO', 'Abduction',
         'Quincy', 'Anime', 'Bonus', 'Bahama Mama', 'marijuana',
         'opium', 'feeling', 'army', 'insole','bathing in',
         'Chair', 'Sitting on', 'Car rides with','Reading Books about ',
         'Speaking in a made up language called',
         'Steaming in', 'Running around naked with')

last = ('Stabbing', 'Breathing', 'Cartwheel', 'Lamp',
        'clamshells','carrots', 'performing', 'wearing',
        'sex', 'running', 'stomping', 'chicken broth',
        'the last supper', 'saturday', 'cold war',
        'dinosaurs', 'television')

while True:
    firstWord = random.choice(first)

    secondWord = random.choice(last)

    print('\n\n')
    print('{} {}'.format(firstWord, secondWord), file=sys.stderr)
    print('\n\n')

    try_again = input('\n\nTry again? (press Enter else N to quit)\n')
    if try_again.lower() == 'n':
        break

input('\nPress Enter to Exit')
