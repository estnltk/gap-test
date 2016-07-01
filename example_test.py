"""
An example of running a gaps test.

Usage:
  
    python example_test.py <gap file> <candidates' file>

For each sentence in the gap file, outputs the rank of the gap word.

"""
import sys
import codecs
import random


if __name__ == '__main__':
    gap_fnm = sys.argv[1]
    cnd_fnm = sys.argv[2]
    
    gap_file = codecs.open(gap_fnm, 'r', 'utf-8')
    cnd_file = codecs.open(cnd_fnm, 'r', 'utf-8')
    
    while 1:
        # read a line from the gap test file
        gap_ln = gap_file.readline().rstrip()
        if not gap_ln:
            break
        items = gap_ln.split()
        word_offset = int(items[0])
        sentence = items[1:]
        gap_word = sentence[word_offset]
    
        # read a line from the candidates' file
        cnd_ln = cnd_file.readline().rstrip()
        candidates = cnd_ln.split()
       
        # Score the candidates in a smart way here. As for now, just shuffle randomly.
        candidates.append(gap_word)
        random.shuffle(candidates)
       
        # output the rank of the original gap word
        for i, c in enumerate(candidates):
            if c == gap_word:
                print i
