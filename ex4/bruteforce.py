# ll = ['!','=','%','s','f','g','c','m','S','F','G','C','M']
import itertools
import hashlib

ll = ['s','3','m','1','c','!','S','M','C','=','%']
# sha = 'c0c0f0f1db9807bdc0d4d4094ffac18085c2a955'
sha = 'b8e46064c5cb98321ab378f546d2641881b43563'

for L in range (0, len(ll)+1):
    for subset in itertools.permutations(ll, L):
        if (hashlib.sha1(''.join(subset)).hexdigest() == sha):
            print ''.join(subset)
