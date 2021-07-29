def two_fer(name=None):
    return "One for you, one for me." if name == None else "One for {nm}, one for me.".format(nm=name) 