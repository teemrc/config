from pynput import keyboard
import os, numpy as np, random

c = ['📄', '📒', '📗', '📘', '📕', '📙']
e = False
cc =False
itt = False

l = [[[ur for i in range(3)] for iu in range(3)] for ur in c]
ln = np.array(l)
km = ['f', 'u', 'r', 'l', 'd', 'b', 'm', 'e', 's', 'x', 'y', 'z']

def p():
    os.system('cls')
    print("                    l' m' r           /\\-x     <-y    >\/-z")
    for i in range(3):
        if i == 0:
            o="d'"
        elif i == 1:
            o ="c'"
        elif i == 2:
            o ="u "
        else:
            o = ''                                               # ж
        print('                  ', *ln[1][i], o)
    print("                    l' m' r")                                                                         
    for i in range(3): 
        if i == 0:
            o="b'"
        elif i == 1:
            o ="s "
        elif i == 2:
            o ="f "
        else:
            o = ''                                               # з
        print('                  ', *ln[2][i], o)
    print("        b' s  f     l' m' r     f' s' b")
    for i in range(3):                                           #к б о
        if i == 0:
            o="u'"
        elif i == 1:
            o ="e "
        elif i == 2:
            o ="d "
        else:
            o = '  '
        print('      ', *ln[4][i],o , *ln[0][i],o, *ln[5][i], o)
    print("                    l' m' r")
    for i in range(3): 
        if i == 0:
            o="f'"
        elif i == 1:
            o ="s'"
        elif i == 2:
            o ="b "
        else:
            o = '  '                                           #с
        print('                  ', *ln[3][i], o)

def mov(k):
    l0 = ln[0].copy()
    l1 = ln[1].copy()
    l2 = ln[2].copy()
    l3 = ln[3].copy()
    l4 = ln[4].copy()
    l5 = ln[5].copy()

    if k == 'f':
        ln[2][2] = l4[:,2][::-1]
        ln[3][0] = l5[:,0][::-1]
        ln[4][:,2] = l3[0]
        ln[5][:,0] = l2[2]  

        ln[0] = np.rot90(ln[0], k=-1)     

    if k == 'd':
        ln[0][2] = l4[2]
        ln[1][0] = l5[2][::-1]
        ln[4][2] = l1[0][::-1]
        ln[5][2] = l0[2]  

        ln[3] = np.rot90(ln[3], k=-1) 

    if k == 'u':
        ln[0][0] = l5[0]
        ln[1][2] = l4[0][::-1]
        ln[4][0] = l0[0]
        ln[5][0] = l1[2][::-1] 

        ln[2] = np.rot90(ln[2], k=-1)

    if k == 'r':
        ln[0][:, 2] = l3[:, 2]
        ln[1][:, 2] = l2[:, 2]
        ln[2][:, 2] = l0[:, 2]
        ln[3][:, 2] = l1[:, 2] 

        ln[5] = np.rot90(ln[5], k=-1)

    if k == 'l':
        ln[0][:, 0] = l2[:, 0]
        ln[1][:, 0] = l3[:, 0]
        ln[2][:, 0] = l1[:, 0]
        ln[3][:, 0] = l0[:, 0] 

        ln[4] = np.rot90(ln[4], k=-1)

    if k == 'b':
        ln[2][0] = l5[:,2]
        ln[3][2] = l4[:,0]
        ln[4][:,0] = l2[0][::-1]
        ln[5][:,2] = l3[2][::-1]  

        ln[1] = np.rot90(ln[1], k=-1)

    if k == 'm':
        ln[0][:, 1] = l2[:, 1]
        ln[1][:, 1] = l3[:, 1]
        ln[2][:, 1] = l1[:, 1]
        ln[3][:, 1] = l0[:, 1]

    if k == 'e':
        ln[0][1] = l4[1]
        ln[1][1] = l5[1][::-1]
        ln[4][1] = l1[1][::-1]
        ln[5][1] = l0[1] 

    if k == 's':
        ln[4][:, 1] = l3[1]
        ln[5][:, 1] = l2[1]
        ln[2][1] = l4[:, 1][::-1]
        ln[3][1] = l5[:, 1][::-1]

    if k == 'x':
        ln[0] = l3
        ln[1] = l2
        ln[2] = l0
        ln[3] = l1

        ln[4] = np.rot90(ln[4], k=1)
        ln[5] = np.rot90(ln[5], k=-1)

    if k == 'y':
        ln[0] = l5
        ln[1] = np.flip(l4[::-1], axis=1)
        ln[4] = l0
        ln[5] = np.flip(l1[::-1], axis=1)

        ln[2] = np.rot90(ln[2], k=-1)
        ln[3] = np.rot90(ln[3], k=1)    

    if k == 'z':
        ln[4] = l3
        ln[5] = l2
        ln[2] = l4
        ln[3] = l5

        ln[0] = np.rot90(ln[0], k=-1)
        ln[1] = np.rot90(ln[1], k=1)
        ln[4] = np.rot90(ln[4], k=-1)
        ln[5] = np.rot90(ln[5], k=-1)
        ln[2] = np.rot90(ln[2], k=-1)
        ln[3] = np.rot90(ln[3], k=-1)

def shtr(t):
    for i in range(3):
        mov(t)

def req(ll):
    l = ll.split(' ')
    for i in l:
        if len(i) == 1:
            mov(i)
        else:
            shtr(i[1])

def pif():
    re = "r u 'r 'u"
    req(re)

def l_pif():
    re = "'l 'u l u"
    req(re)

def prov():
    global e
    if np.array_equal(ln, l) and  itt:
        print('You win!')
        e = True

def zam():
    n0 = np.where(ln == l[0])[0][0]
    n1 = np.where(ln == l[1])[0][0]
    n2 = np.where(ln == l[2])[0][0]
    n3 = np.where(ln == l[3])[0][0]
    n4 = np.where(ln == l[4])[0][0]
    n5 = np.where(ln == l[5])[0][0]
    
    ln0 = ln[n0].copy()
    ln1 = ln[n1].copy()
    ln2 = ln[n2].copy()
    ln3 = ln[n3].copy()
    ln4 = ln[n4].copy()
    ln5 = ln[n5].copy()
    
    if np.array_equal(ln0, l[0]) and  np.array_equal(ln1, l[1]) and  np.array_equal(ln2, l[2]) and  np.array_equal(ln3, l[3]) and  np.array_equal(ln4, l[4]) and  np.array_equal(ln5, l[5]):
        ln[0] = ln0
        ln[1] = ln1
        ln[2] = ln2
        ln[3] = ln3
        ln[4] = ln4
        ln[5] = ln5    

def proccess_key(key):
    global e, km, cc
    try:
        c = key.char.lower()

        if c in km:
            if cc:
                shtr(c)
                cc = False
            else:
                mov(c)
            p()

        if c == 'p':
            if cc:
                for i in range(5):
                    pif()
            else:
                pif()
            p()
            cc = False

        if c == '[':
            if cc:
                for i in range(5):
                    l_pif()
            else:
                l_pif()
            p()
            cc = False

        if itt and c == 'n':
            for i in r[::-1]:
                shtr(i)
                p()

        if c == "'":
            cc = True
        
        if c == 'q':
            e =True        

    except AttributeError:
        pass

listener = keyboard.Listener(
    on_press = None,
    on_release = proccess_key)
listener.start()

os.system('cls')
it = int(input('Напишите 1 для песочницы, 2 для сборки: '))
if it == 1:
    p()

elif it == 2:
    r = ' '.join(random.choices(km[:6], k=random.randint(30, 40)))
    r = "r u 'r 'u 'r f r r 'u 'r 'u r u 'r 'f"*2    
    req(r)
    p()
    itt = True
    
while True:
    if itt:
        zam()
        prov()
    if e:
        break
