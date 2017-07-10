class mobile(object):
    def __init__(self, comp, col):
        self.comp = comp
        self.col = col
    
class basic(mobile):
    pass

class adv(mobile):
    def __init__(self, comp, col, os):
#        super(adv, self).__init__(comp, col)
        mobile.__init__(self,comp,col)
        self.os = os

b1 = basic("samsung","black")
print b1.comp
print b1.col


b2 = adv("moto","gray", "andriod")
print b2.comp
print b2.col
print b2.os


    
