class A(object):
    def who_am_i(self):
        print "I am A"

class B(A):
    def who_am_i(self):
        print "I am B"
#     pass

class C(A):
    def who_am_i(self):
        print "I am C"

class D(B,C):
    def who_am_i(self):
        print "I am D"
#     pass


d1 = D()
d1.who_am_i()

super(D, d1).who_am_i()
    
