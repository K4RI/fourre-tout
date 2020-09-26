from tkinter import *

file = open('jeu-depart.txt', 'r')
data = file.read()
lignes = data.split('\n')

# génère la matrice sans les espaces
M_init = [[int(lignes[i][j]) for j in range(len(lignes[0])) if lignes[i][j]!=' '] for i in range(len(lignes)-1)]
M=M_init
cpt=0

n=len(M)
p=len(M[0])
print(M)
flag=False
interm=True

res=50

def affiche_grille():
    global M
    for i in range(n):
        for j in range(p):
            if M[i][j]==1:
                can.create_rectangle(res*j,res*i,res*(j+1),res*(i+1),fill='grey')
            if M[i][j]==0:
                can.create_rectangle(res*j,res*i,res*(j+1),res*(i+1),fill='white')
            if M[i][j]=='app':
                can.create_rectangle(res*j,res*i,res*(j+1),res*(i+1),fill='green')
            if M[i][j]=='disp':
                can.create_rectangle(res*j,res*i,res*(j+1),res*(i+1),fill='red')

def voisins(i,j):
    if i==0:
        if j==0: # coin sup gauche
            return [(0,1), (1,0), (1,1)]
        if j==p-1: # coin sup droit
            return [(0,p-2), (1,p-1), (1,p-2)]
        else: # reste du coté sup
            return [(0,j-1), (0,j+1), (1,j-1), (1,j), (1, j+1)]
    
    if i==n-1:
        if j==0: # coin inf gauche
            return [(0,1), (1,0), (1,1)]
        if j==p-1: # coin inf droit
            return [(n-1,p-2), (n-2,p-1), (n-2,p-2)]
        else: # reste du côté inf
            return [(0,j-1), (0,j+1), (1,j-1), (1,j), (1, j+1)]
    
    if j==0: # reste du côté gauche
        return [(i-1,0), (i-1,1), (i,1), (i+1,0), (i+1,1)]

    if j==p-1: # reste du côté droit
        return [(i-1,p-1), (i-1,p-2), (i,p-2), (i+1,p-2), (i+1,p-1)]
    
    return [(i-1,j-1), (i-1,j), (i-1,j+1), (i,j-1), (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)] # sur aucun bord

def jouer():
    global M, interm, cpt
    interm=not(interm)
    if not interm: # passe de l'étape n à l'étape n+1/2
        M_temp=[[0 for j in range(p)] for i in range(n)]
        for i in range(n):
            for j in range(p):
                s= sum([M[i][j] for (i,j) in voisins(i,j)])
                if M[i][j]==1:
                    if s in [2,3]:
                        M_temp[i][j]=1
                    else:
                        M_temp[i][j]='disp'
                
                if M[i][j]==0:
                    if s==3:
                        M_temp[i][j]='app'
                    else:
                        M_temp[i][j]=0
        M = M_temp
    
    if interm: # passe de l'étape n+1/2 à l'étape n+1
        for i in range(n):
            for j in range(p):
                if M[i][j]=='disp':
                    M[i][j]=0
                if M[i][j]=='app':
                    M[i][j]=1
    affiche_grille()
    cpt+=0.5
    label.configure(text = 'TOUR %i' % (cpt))

def do_iteration():
    global cpt
    if flag:
        jouer()
        can.after(100, do_iteration)
        b2.config(state=DISABLED)
        b3.config(state=DISABLED)        

def play():
    global flag
    flag=True
    do_iteration()

def stop():
    global flag
    flag=False
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)   

def reinit():
    global cpt, M, flag
    flag=False
    cpt=0
    M=M_init
    affiche_grille()



fen = Tk()
can = Canvas(fen, width=res*len(M[0]), height=res*len(M), bg='white')
can.pack()

b1 = Button(fen, text='Afficher', command=affiche_grille)
b1.pack(side=RIGHT,padx=3, pady=3)
b2 = Button(fen, text='Jouer', command=jouer)
b2.pack(side=RIGHT,padx=3, pady=3)
b3 = Button(fen, text='Play', command=play)
b3.pack(side=RIGHT,padx=3, pady=3)
b4 = Button(fen, text='Stop', command=stop)
b4.pack(side=RIGHT,padx=3, pady=3)
b5 = Button(fen, text='Réinit.', command=reinit)
b5.pack(side=RIGHT,padx=3, pady=3)

label = Label(fen)
label.pack()


def click(event):
    global M
    i=event.y//res
    j=event.x//res
    M[i][j]=1-M[i][j]
    affiche_grille()

fen.bind('<Button-1>', click)

fen.mainloop()
