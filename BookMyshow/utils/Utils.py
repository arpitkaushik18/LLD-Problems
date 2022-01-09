seq = 0

def get_unique_sequence():
    global seq
    seq+=1
    return "ID" + str(seq)