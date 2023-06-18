# TODO: replace by preexisting functions

def flatmap(elements):
    accumulator = []
    for element1 in elements:
        for element2 in element1:
            accumulator.append(element2)
    return accumulator

def unique(elements: list):
    return list({k for k in elements})