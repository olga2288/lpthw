class Song (object):
    def __init__(self, lyrics1):
        self.lyrics = lyrics1

    def sing_me_a_song(self):
          print "\n"
          for line in self.lyrics:
              print line


happy_bday  = Song (["Happy birthday to you",
                     "I don't want to get sued",
                     "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                         "With pockets full of shells"])
text = ["one", "two", "three", 'four', "I'm going to look for..."]

add_from_me = Song(text)

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


add_from_me.sing_me_a_song()
