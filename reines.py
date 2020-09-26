def reine(M,config):
    if M==0:
        return True
    pos=config[M]
    for i in range(M):
        interdits=(pos,pos-(M-i),pos+(M-i))
        if config[i] in interdits:
            return False
    return reine(M-1,config)

from itertools import permutations
def reines(N):
    perm_ok=()
    for config in list(permutations(range(N))):
        if reine(N-1,config):
            perm_ok=perm_ok+(config,)
    return len(perm_ok), perm_ok
print(reines(4))