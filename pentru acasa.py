a=int(input('primul: '))
b=int(input('al doilea: '))
c=int(input('al treilea: '))
import math
def cel_mm_div_com(x,y,z):
    m=[]
    n=[]
    q=[]
    for i in range (1,x+1):
        if (x%i==0):
            m.append(i)
    for j in range (1,y+1):
        if (y%j==0):
            n.append(j)
    for k in range (1,z+1):
        if (y%k==0):
            q.append(k)        
    h=set(m).intersection(n)
    d=set(h).intersection(q)
    l=max(d)
    return (l)
print( "Cel mai mare divizor comun al numerelor este: ",cel_mm_div_com(a,b,c))


def cel_mmic_mult_com(x,y,z):
    if x>y and x>z:
        multiplu=x
    elif b>a and b>c:
        multiplu=y
    elif z>x and z>y:
        multiplu=z
    
    while True:
        if ((multiplu%x==0)and(multiplu%y==0)and (multiplu%z==0)):
            cel_mmic=multiplu
            break
        multiplu +=1
    return (multiplu)
print(" Cel mai mic multiplu comun al numerelor este: ",cel_mmic_mult_com(a,b,c))


def minim(x,y,z):
    return min([x,y,z])
print ("Numarul minim este:",minim(a,b,c))


def maxim(x,y,z):
    return max([x,y,z])
print ("Numarul minim este:",maxim(a,b,c))

def divizorii_comuni_3nr(a,b,c):
    at=[]
    bt=[]
    ct=[]
    for i in range (1,a+1):
        if (a%i==0):
            at.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            bt.append(j)
    for k in range (1,c+1):
        if (c%k==0):
            ct.append(k)
    d=set(at).intersection(bt)
    e=set(d).intersection(ct)
    br=list(e)
    return (br)
print("Toti divizorii comuni ai numerelor sunt :" ,divizorii_comuni_3nr(a,b,c))

def mult_com_cm_mici_primii_3(a,b,c):
    c_m_m_m=[]
    if a>b:
        multiplu=a
    elif b>a:
        multiplu=b
    else:
        multiplu=a
    while len(c_m_m_m)<3:
        if ((multiplu%a==0)and(multiplu%b==0)):
            c_m_m_m.append(multiplu)
            multiplu +=1
        else:
            multiplu +=1
    return (c_m_m_m)
print("Primii 3 multipli comuni al numerelor  sunt: ",mult_com_cm_mici_primii_3(a,b,c))

def semiperimetru(x,y,z):
    s=(x+y+z)/2
    return s 

def triunghi(x,y,z):
    w=[]
    if (x+y)>z and (y+z)>x and (x+z)>y:
        arie='aria='+str(math.sqrt(semiperimetru(x,y,x)*(semiperimetru(x,y,x)-x)*(semiperimetru(x,y,x)-y)*(semiperimetru(x,y,x)-z)))
        perimetru='perimetrul='+str(x+y+z)
    else:
        arie='arie nu exista,'
        perimetru='perimetru nu exista'
    w.extend([arie,perimetru])
    w=' '.join(w)
    return w
print(triunghi(a,b,c))

def ecuatie(x,y,z):
    if ((y**2)-(4*x*z))>=0:
        q=(0-y-math.sqrt((y**2)-(4*x*z)))/(2*x)
        r=(0-y+math.sqrt((y**2)-(4*x*z)))/(2*x)
        sol='x1='+str(q)+', x2='+str(r)
    return sol
print('solutiile ecuatiei ',a,'x**2+',b,'x+',c,'=0 :',ecuatie(a,b,c))
