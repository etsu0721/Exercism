def two_fer(name=""):
    if name == "":
        return "One for you, one for me."
    else:
        return "One for {nm}, one for me.".format(nm=name)