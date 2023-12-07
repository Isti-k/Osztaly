
etelnev=["húsleves","paradicsomleves","gyümölcsleves"]
etelar=[1200,1100,2000]

'''Most annyi lista van, ahány tulajdonsága az adott ételnek'''

'''Úgy lenne a jobb, ha csak 1 listánk lene,
és egy ételnek egybe kezelhetnénk a tuéajdonságait!
Létrehozunk egyétel típust - ez az étel általános leírását jelenti.
Konkrét étel a típus példányosításakor jön létre.'''


'''print("Az első leves ára",etelnev[0],etelar[0])'''

from Etel import Etel
etelek=[]
etel=Etel("húsleves",1200,"Leves")#pédányosítás
etelek.append(etel)
etel=Etel("paradicsomleves",1100,"Leves")#pédányosítás
etelek.append(etel)
etel=Etel("pörkölt",1200,"főétel")#pédányosítás
etelek.append(etel)

for i in range(0,len(etelek),1):
    print(f"Az {i}. étel: {etelek[i].nev},{etelek[i].ar},{etelek[i].tipus}")


szemelyeknev=["Jani","Pari","Béla"]
szemelyszul_ev=[1998,2002,1967]

from Szemely import Szemely
szemelyek=[]
szemely=Szemely("Jani",1998,"1-1969122-123")#pédányosítás
szemelyek.append(szemely)
szemely=Szemely("Pari",2002,"1-1969122-123")#pédányosítás
szemelyek.append(szemely)
szemely=Szemely("Béla",1967,"1-1969122-123")#pédányosítás
szemelyek.append(szemely)

for i in range(0,len(etelek),1):
    print(f"Az {i+1}. személy: {szemelyek[i].nev},{szemelyek[i].szul_ev},{szemelyek[i].szem_szam}")
    print(f"{szemelyek[i].nev} {szemelyek[i].kor()} éves")


