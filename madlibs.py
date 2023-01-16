import sys

usage = f'''Usage: 
python3 {sys.argv[0]} PATH_TO_FILE_WITH_STORY'''

if len(sys.argv) < 2:
    print(usage)
    exit(-1)

# File containing a story
filename = sys.argv[1]

# Read the story
with open(filename) as f:
    TEXT = f.read()

# Answers
blanks = []

# split story
words = TEXT.split()

# Take input from user and store
for w in words:
    if w.startswith('<<'):
        if w.endswith('>>'):
            pass
        # If it ends with characters like .,? then remove them
        else:
            w = w[0:-1]
        user_word = input(w[2:-2] + ": ")
        blanks.append((w, user_word))

# Arrange the story
for word in words:
    hold = ''
    if word.startswith('<<') and '>>' in word:
        if not word.endswith('>>'):
            hold = word[word.index('>>')+2:]
        ind = words.index(word)
        words.pop(ind)
        words.insert(ind, blanks[0][1]+hold)
        blanks.pop(0)

# Print the story
print('\n\nThe story: \n')
print(' '.join(words))
