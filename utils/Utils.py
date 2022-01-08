seq = 0
counter = 0

def get_sequence():
    global seq
    seq+=1
    return "ID " + str(seq)

def numberCounter():
    global counter
    counter+=1
    return counter