from FoxDot import *
from functools import partial

def group_method(f):
    """ Decorator for assigning functions as Group methods.
    If the function name contains "_group" that will be removed while assigning
    allowing you to a have a function, a player method and group method all called the same thing

    >>> @group_method
    ... def test(self):
    ...    print(self)

    >>> p1.test()
    """
    name = f.__name__.replace("_group", "")
    setattr(Group, name, f)
    return getattr(Group, name)

GroupMethod = group_method # Temporary alias

@player_method
def soloBars(self,n=2,end=False):
    ''' Solo's the current player from the next bar for the specified amount of bars
    '''
    nextBar(self.solo)
    soloEnd = Clock.next_bar() + (n * Clock.bar_length())
    Clock.schedule(self.metro.solo.reset, soloEnd)
    if(end):
        Clock.schedule(self.stop, soloEnd)
        
        
@player_method
def soloBeats(self, n=8, end=False):
    ''' Solo's the current player from now for the specified amount of beats
    '''
    Clock.schedule(self.solo, Clock.now())
    soloEnd = Clock.now() + n
    Clock.schedule(self.metro.solo.reset, soloEnd)
    if(end):
        Clock.schedule(self.stop, soloEnd)
    

@group_method
def soloBars_group(self,n=2, end=False):
    ''' Solo's the current group from the next bar for the specified amount of bars
    '''
    if self.metro is None:
        self.__class__.metro = Player.metro

    soloEnd = Clock.next_bar() + (n * Clock.bar_length())
    Clock.schedule(self.metro.solo.reset, soloEnd)
    if(end):
        for player in list(self.metro.playing):
            if player in self.players:
                Clock.schedule(player.stop, soloEnd)

    nextBar(self.solo)

@group_method
def soloBeats_group(self,n=8, end=False):
    ''' Solo's the current group from now for the specified amount of beats
    '''
    if self.metro is None:
        self.__class__.metro = Player.metro
    
    soloEnd = Clock.now() + n
    Clock.schedule(self.metro.solo.reset, soloEnd)
    if(end):
        for player in list(self.metro.playing):
            if player in self.players:
                Clock.schedule(player.stop, soloEnd)
    
    Clock.schedule(self.solo, Clock.now())
