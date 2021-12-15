import numpy as np
from itertools import product
from difflib import SequenceMatcher

def gen_adn(n):
    ADN = {}
    for i in range(n):
        ADN[i+1] =  ['A','C','T','G']
    return ADN

def validate(words, length):
    
    ADN = gen_adn(length)
    
    for c in product(*[ADN[k] for k in sorted(ADN.keys())]):
        vaccine = ''.join(c)
        valid = 0
        for word in words:
            distance = levenshtein_ratio_and_distance(word.upper(), vaccine.upper())
            if(distance <= 3):
                valid += 1
        if valid == len(words):
            return vaccine
    
    return 'IMPOSSIBLE'


def levenshtein_ratio_and_distance(s, t, ratio_calc = False):
    rows = len(s)+1
    cols = len(t)+1
    distance = np.zeros((rows,cols),dtype = int)

    for i in range(1, rows):
        for k in range(1,cols):
            distance[i][0] = i
            distance[0][k] = k
  
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                if ratio_calc == True:
                    cost = 2
                else:
                    cost = 1
            distance[row][col] = distance[row-1][col-1] + cost  
            
    if ratio_calc == True:
        Ratio = ((len(s)+len(t)) - distance[row][col]) / (len(s)+len(t))
        return Ratio
    else:
        return distance[row][col]

def main(n,m):
    words = []
    for _ in range(m):
        words.append(input())
    print(validate(words,n))

if __name__ == '__main__':
    n, m = input().split()
    n, m = int(n), int(m)
    while(n != 0 and m != 0):
        main(n, m)
        n, m = input().split()
        n, m = int(n), int(m)

