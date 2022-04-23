class Codec:
    def __init__(self):
        self.long_short = {}
        self.short_long = {}
        self.alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def encode(self, longUrl):
        while longUrl not in self.long_short:
            code = "".join(choices(self.alphabet, k=6))
            if code not in self.short_long:
                self.short_long[code] = longUrl
                self.long_short[longUrl] = code
        return 'http://tinyurl.com/' + self.long_short[longUrl]
    def decode(self, shortUrl):
        return self.short_long[shortUrl[-6:]]
