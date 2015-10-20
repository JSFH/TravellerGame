class Planet:
    ' allegedly, this will be the object which represents a system'
    def __init__(self, name):
        sysfo=open(name+'.txt', 'r')
        self.Name=sysfo.readline().rstrip('\n')
        self.starport=sysfo.readline().rstrip('\n')
        self.size=sysfo.readline().rstrip('\n')
        self.atmo=sysfo.readline().rstrip('\n')
        self.hydro=sysfo.readline().rstrip('\n')
        self.popu=sysfo.readline().rstrip('\n')
        self.gov=sysfo.readline().rstrip('\n')
        self.law=sysfo.readline().rstrip('\n')
        self.tech=sysfo.readline().rstrip('\n')
        sysfo.readline()
        self.zone=sysfo.readline().rstrip('\n')
        self.popmul=sysfo.readline().rstrip('\n')
        self.plan=sysfo.readline().rstrip('\n')
        self.gas=sysfo.readline().rstrip('\n')
        sysfo.close()
        self.TradeCode=TradeCode(self)
    def display(self):
        code=''
        code=self.starport+self.size+self.atmo+self.hydro+self.popu+self.gov+self.law+'-'+self.tech
        sys=self.zone+self.popmul+self.plan+self.gas
        print code
        print sys
        '''print self.Name
        print self.starport
        print self.size
        print self.atmo
        print self.hydro
        print self.popu
        print self.gov
        print self.law
        print self.tech
        print self.zone
        print self.popmul
        print self.plan
        print self.gas'''


class TradeCode(Planet):
    'supposed to be the trade code generator and holder for planets'
    def __init__(self, parent):
        if ((4<=parent.atmo<=9) and (4<=parent.hydro<=8) and (5<=parent.popu<=7)):
            self.Ag = True
        else:
            self.Ag = False
        if (parent.size==0 and parent.atmo==0 and parent.hydro==0):
            self.As = True
        else:
            self.As = False
        if (parent.popu==0 and parent.gov==0 and parent.law==0):
            self.Ba = True
        else:
            self.Ba = False

        if (100000**100000<=parent.popu):
            self.NI = True
        else:
            self.NI = False
            
    


        


abydos = Planet("Abydos")
abydos.display()
print abydos.TradeCode.NI
        
        
        
