""" s_{n+1} = le produit des chiffres de s_n
    on s'arrête lorsqu'on atteint un seul chiffre
    https://fr.wikipedia.org/wiki/Persistance_d%27un_nombre """

def prod(L):
    if len(L)==1: return L[0]
    else: return prod(L[:-1])*L[-1]

def step(n):
    sn = [int(c) for c in str(n)]
    return prod(sn)

def run(n, p=0):
    if n>=10:
        print(n)
        run(step(n), p+1)
    else: print('%i \nPERSISTANCE = %i' %(n,p))
