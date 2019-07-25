#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nicolas Comte
"""

import unittest
import sys
sys.path.append('../')

from lib.jukebox import *
    
class jukeboxTest(unittest.TestCase):
    """Test lib/jukebox.py classes."""
    
    def setUp(self):
        self.tracks = [
            Track('First movement', 'Schumann', 3),
            Track('Second movement', 'Schumann', 2),
            Track('Third movement', 'Schumann', 2),
            Track('Fourth movement', 'Schumann', 3)
                ]

    def test_Track(self):
        """Test Track class"""
        track = self.tracks[0]
        self.assertEqual(track.getName(), "First movement")
        self.assertEqual(track.getArtist(), "Schumann")
        
        track = self.tracks[1]
        self.assertEqual(track.getLength(), 2)
        
    def test_playlist(self):
        """Test Playlist class"""
        # test with an empty playlist
        p = Playlist([])
        self.assertEqual(p.nextTrack(), None)
        p.addTrack(self.tracks[0])
        self.assertEqual(p.nextTrack().getName(), self.tracks[0].getName())
        p.addTracks(self.tracks[1:3])
        self.assertEqual(p.nextTrack().getName(), self.tracks[1].getName())
        self.assertEqual(p.nextTrack().getName(), self.tracks[2].getName())
        
        # test with a filled playlist
        p = Playlist(self.tracks)
        self.assertEqual(p.nextTrack(), self.tracks[0])
        self.assertEqual(p.getCurrentTrack(), self.tracks[0])
        self.assertEqual(p.nextTrack(), self.tracks[1])
        self.assertEqual(p.nextTrack(), self.tracks[2])
        self.assertEqual(p.nextTrack(), self.tracks[3])
        self.assertEqual(p.nextTrack(), self.tracks[0]) # test loop in playlist
        self.assertListEqual(p.getTrackList(), self.tracks)
        
    def test_player(self):
        """Test Jukebox class"""
        p = TrackPlayer()
        p.runPlaylist(Playlist(self.tracks), False)
        
    def test_jukebox(self):
        """Test Jukebox"""
        j = Jukebox([], TrackPlayer())
        j.play()
        
        j = Jukebox(self.tracks, TrackPlayer())
        p = j.getPlaylist()
        tl = p.getTrackList()
        self.assertListEqual(p.getTrackList(), [])
        
        j.select(self.tracks[2])
        j.select(self.tracks[3])
        p = j.getPlaylist()
        tl = p.getTrackList()
        self. assertListEqual(p.getTrackList(), [self.tracks[2], self.tracks[3]])
        
        j.play()
        
    
if __name__ == '__main__':
    unittest.main()  
        
        