import random
class forest():
  def __init__(self,journalist,hunter,idol):
    self.journalist = journalist
    self.hunter = hunter
    self.idol = idol
  def hunt(self):
    jrinc = random.randint(1,10)
    huinc = random.randint(1,10)
    idinc = random.randint(1,10)
    if (jrinc >= huinc and jrinc >= idinc):
        self.journalist = self.journalist + jrinc
        self.hunter = self.hunter + huinc
        self.idol = self.idol + idinc
        print("Point Journalist >> ",self.journalist)
        print("Point Hunter >> ",self.hunter)
        print("Point Idol >> ",self.idol)
        print("")
        print(">>>")
        print("Got some News!!! -- Journalist one point!")
    elif(huinc > jrinc and huinc >= idinc):
        self.journalist = self.journalist + jrinc
        self.hunter = self.hunter + huinc
        self.idol = self.idol + idinc
        print("Point Journalist >> ",self.journalist)
        print("Point Hunter >> ",self.hunter)
        print("Point Idol >> ",self.idol)
        print("")
        print(">>>")
        print("Party Carnival!!!! -- Hunter one point")
    elif(idinc > jrinc and idinc > jrinc):
        self.journalist = self.journalist + jrinc
        self.hunter = self.hunter + huinc
        self.idol = self.idol + idinc
        print("Point Journalist >> ",self.journalist)
        print("Point Hunter >> ",self.hunter)
        print("Point Idol >> ",self.idol)
        print("")
        print(">>>")
        print("Stage Clear!!! -- Idol one point")
    else:
        print("--ERROR Inspectors are watching you all--")

game1 = forest(0,0,0)
game1.hunt()
    