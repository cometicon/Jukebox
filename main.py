#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 22:33:10 2019

@author: Nicolas Comte
"""

import sys
from lib.jukebox import *

queen = [
            Track('The Prophet\'s Song', 'Brian May', 3),
            Track('Love of My Life', 'Freddie Mercury', 1),
            Track('Good Company', 'Brian May', 1),
            Track('Bohemian Rhapsody', 'Freddie Mercury', 2),
            Track('God Save the Queen', '-', 1)
        ]

def main(argv):
    print('Hello world')
    my_jukebox = Jukebox(queen) # our jukebox has the album "Queen"
    my_jukebox.select(queen[1]) # We select the tracks 1, 3 and 4
    my_jukebox.select(queen[3])
    my_jukebox.select(queen[4])
    my_jukebox.play()

if __name__ == '__main__':
    main(sys.argv)