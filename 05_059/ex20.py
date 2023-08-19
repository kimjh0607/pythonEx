import mp3player as mp3

song1 = mp3.Song('신호등', '이무진', 3)
song2 = mp3.Song('Permission', 'BTS', 4)
song3 = mp3.Song('Butter', 'BTS', 2)
song4 = mp3.Song('Weekend', 'TAEYEON', 5)
song5 = mp3.Song('좋아좋아', '조정석', 4)

player = mp3.Player()
player.addSong(song1)
player.addSong(song2)
player.addSong(song3)
player.addSong(song4)
player.addSong(song5)

player.setIsLoop(False)
player.shuffle()
player.play()