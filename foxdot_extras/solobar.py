from FoxDot import *
from functools import partial

@nextBar
@player_method
def solobar(self, n=1):
    
    self.solo()
    futureBar(partial(self.solo, False), n=n)

'''
@player_method
def test(self):
    print(self.degree)
 
l1.test()

from foxdot_extras.pbase import PBase
from functools import partial

l1 >> dub(P[0,2,4,2,3,4,5])
d1 >> play("x X ")

@player_method
def solobar(self, sn=1):
    nextBar(self.solo)
    futureBar(partial(self.solo, False, n=sn))


d1.solobar()

'''