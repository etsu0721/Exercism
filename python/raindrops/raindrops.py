def convert(number):
    potential_factors = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    sounds = ''.join(
        sound
        for factor, sound in potential_factors 
        if number % factor == 0)
    return sounds or str(number)