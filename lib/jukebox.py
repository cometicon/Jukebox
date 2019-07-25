#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Nicolas Comte
"""

import time
from abc import ABC, abstractmethod

class Track:
    """Track/song representation."""
    
    ##
    # @param title string. The name of the track.
    # @param artist string. The name of the artist(s).
    # @param length number. The duration of the track. 
    def __init__(self, name, artist, length = None):
        self._name = name
        self._artist = artist
        self._length = length
     
    ##      
    # @returns string. The name of the track.    
    def getName(self):
        return self._name
    
    ##
    # @returns string. The name of the artist(s)
    def getArtist(self):
        return self._artist
    
    ##
    # @returns integer. The duration of the track (seconds).
    def getLength(self):
        return self._length
    
class Playlist:
    """Playlist, set of tracks. It is a simple wrapper of list. If the playlist is ended it will 
    restart by the beginnning."""
    
    ##
    # @param tracks list of tracks. List that represents a collection of tracks.
    def __init__(self, tracks):
        self._current = -1
        self._list = tracks
    
    ##
    # @returns list of tracks.
    def getTrackList(self):
        return self._list
     
    ##    
    # @returns track. The last track returned by the playlist.
    def getCurrentTrack(self):
        return self._list[self._current] if self._current < len(self._list) else None
    
    ##
    # @returns track. Go to the next track and return it. If the playlist is ended, the first track will be returned.  
    def nextTrack(self):
        self._current = self._current + 1 if (self._current + 1) < len(self._list) else 0
        return self.getCurrentTrack()
    
    ##
    # @returns number. The total playlist duration. 
    def getTotalTime(self):
        res = 0
        for s in self._list:
            res += s.getLength()
        return res
    
    ##
    # @param track track. Append a track to the playlist.
    def addTrack(self, track):
        self._list.append(track)
     
    ##    
    # @brief add tracks to the playlist.
    # @param tracks list of tracks. List of tracks to be inserted in the current playlist.
    def addTracks(self, tracks):
        self._list.extend(tracks)
        
        
class Player(ABC):
    """Jukebox player class that can run playlists and play its musics."""
    ##
    # @brief play track. Abstract method   
    # @param track track. The track to play.
    @abstractmethod
    def play(self, track):
        pass
        
    # @brief run the playlist. Can be stopped with Ctrl-D action.
    # @param playlist playlist. The playlist to launch.
    # @param loop boolean. Repeat the playlist after the last song if true.
    def runPlaylist(self, playlist, loop = False):
        timeout = time.time() + playlist.getTotalTime()
        
        try:
            while loop or time.time() < timeout:
                track = playlist.nextTrack()
                self.play(track)
                
        except KeyboardInterrupt:
            print('Stopped.')
            
class TrackPlayer(Player):
    """Music player specialized in Track reading."""
    ##
    # @brief play track. Abstract method   
    # @param track track. The track to play.
    def play(self, track):
        print("Playing: " + track.getName())
        time.sleep(track.getLength()) # simulation of playing Track
            
class Jukebox:
    """Jukebox class"""
    
    ##
    # @param library list of tracks. The collection of tracks associated to the jukebox.
    def __init__(self, library, player):
        self._library = library # collection of tracks
        self._playlist = Playlist([])
        self._player = player
    
    ##    
    # @brief add a track into the current playlist.
    # @param track track.    
    def select(self, track):
        self._playlist.addTrack(track)
    
    ##    
    # @brief set playlist in the jukebox. Will replace the previous by a new one.    
    def setPlaylist(self, playlist):
        self._playlist = playlist
        
    ##    
    # @brief get current playlist of the jukebox.
    def getPlaylist(self):
        return self._playlist
    
    ##
    # @brief set a new library in the jukebox. Will replace the current one.
    def setLibrary(self, library):
        self._library = library
    
    ##    
    # @brief launch the playlist.
    # @param loop boolean. Repeat the playlist after the last song if true.
    def play(self, loop = False):
        self._player.runPlaylist(self._playlist, loop)
        
        
            
            
        
        
        
    
        
        
        