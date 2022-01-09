seq=0
def get_unique_id():
    global seq
    seq+=1
    return "ID"+str(seq)