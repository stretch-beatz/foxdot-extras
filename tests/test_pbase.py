import pytest
from FoxDot import *
from foxdot_extras.pbase import PBase

class TestPBase():
    @pytest.mark.parametrize("num, pattern", 
        [(4, P[1,0,0]),(10, P[1,0,1,0]), (0, P[0]), (127, P[1,1,1,1,1,1,1]),(255, P[1,1,1,1,1,1,1,1])]
    )
    def test__binary(self, num, pattern):
        assert PBase(num) == pattern
     
    @pytest.mark.parametrize("num, base, pattern", 
        [(8, 2, P[1,0,0,0]),(10, 2, P[1,0,1,0]), (8, 4, P[2,0]), (10, 4, P[2,2]), (127, 16, P[7,15]),
         (20220709,8,P[1,1,5,1,0,5,4,4,5]),(27071976,8,P[1,4,7,2,1,2,7,5,0])]
    )
    def test__base(self, num, base, pattern):
        assert PBase(num, base) == pattern
    
    
    @pytest.mark.parametrize("num, bas, pattern", 
        [(8, 2, P[1,0,0,0]),(10, 2, P[1,0,1,0]), (8, 4, P[2,0]), (10, 4, P[2,2]), (127, 16, P[7,15]),
         (20220709,8,P[1,1,5,1,0,5,4,4,5]),(27071976,8,P[1,4,7,2,1,2,7,5,0])]
    )
    def test__basenamed(self, num, bas, pattern):
        assert PBase(num, b=bas) == pattern
        
    @pytest.mark.parametrize("num, length, pattern", 
        [(5, 4, P[0,1,0,1]),(5, 2, P[1,0,1]), (127, 8, P[0,1,1,1,1,1,1,1])]
    )
    def test__lennamed(self, num, length, pattern):
        assert PBase(num, l=length) == pattern
    
    
    @pytest.mark.parametrize("num, length, pattern", 
        [(5, 4, P[0,1,0,1]),(5, 2, P[1,0,1]), (127, 8, P[0,1,1,1,1,1,1,1])]
    )
    def test__len(self, num, length, pattern):
        assert PBase(num, 2 ,length) == pattern
    
    
    