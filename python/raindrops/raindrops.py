def convert(number):
    potential_factors = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))
    sounds = ''.join( pf[1] for pf in potential_factors if number % pf[0] == 0 )
    return sounds or str(number)