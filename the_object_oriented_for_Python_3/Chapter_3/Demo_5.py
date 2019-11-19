# -*- coding:utf-8 -*-  
__author__ = 'Mr.Lin'
__date__ = '2019/11/19 17:04'


"""
多态机制
"""




class AudioFile:

    def __init__(self,filename):

        if not filename.endswith(self.ext):
            raise Exception("Invalid")

        self.filename = filename


class Mp3File(AudioFile):

    ext = "mp3"

    def play(self):

        print("play".format(self.filename))


class WavFIle(AudioFile):

    ext = "Wav"

    def play(self):

        print("Play".format(self.filename))


# mp3 = Mp3File("Mympa3")
#
# mp3.play()

# >>>
#     raise Exception("Invalid")
# Exception: Invalid



mp3 = Mp3File("djjdj.mp3")

mp3.play()
# >>>
# play














































