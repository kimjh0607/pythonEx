

from time import sleep
import random as ran


class Song:

    def __init__(self, t, s, pt):
        self.title = t
        self.singer = s
        self.play_time = pt

    def printSongInfo(self):
        print(f'Title : {self.title}, Singer : {self.singer}, Play time : {self.play_time}')



class Player:

    def __init__(self):
        self.songList = []
        self.isLoop = False

    def addSong(self, s):
        self.songList.append(s)

    def play(self):
        if self.isLoop:
            while self.isLoop:
                for songIndex in self.songList:
                    print(f'Title : {songIndex.title} / Singer : {songIndex.singer} / Play time : {songIndex.play_time}sec')
                    sleep(songIndex.play_time)

        else:
            for songIndex in self.songList:
                    print(f'Title : {songIndex.title} / Singer : {songIndex.singer} / Play time : {songIndex.play_time}sec')
                    sleep(songIndex.play_time)

    def shuffle(self):
        ran.shuffle(self.songList)

    def setIsLoop(self, flag):
        self.isLoop = flag