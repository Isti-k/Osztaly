
import datetime
class Szemely:
    def __init__(self,nev:str,szul_ev:str,szem_szam:str):
        self.nev=nev
        self.szul_ev=szul_ev
        self.szem_szam=szem_szam

    def kor(self):
        x = datetime.datetime.now()
        return x.year - self.szul_ev



