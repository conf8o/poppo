from .. import Command
from bs4 import BeautifulSoup

from . import googlesearch

class Translate(Command):
    QUIT = {":q", ":e"}
    def __init__(self, options, argv):
        self.options = options
        self.argv = argv
    
    def exec(self):
        if not self.argv:
            self.start_shell()
        else:
            results = self.translate(self.argv)
            print(*results, sep="\n")

    def start_shell(self):
        while (words := input("words: ")) not in Translate.QUIT:
            results = self.translate(words.split())
            print(*results, sep="\n")

    def translate(self, words):
        for word in words:
            result = self.search(word)
            yield result

    def search(self, word):
        response = googlesearch.goolesearch([word, "英語"])
        soup = BeautifulSoup(response.text, "lxml")
        return soup.get_text()