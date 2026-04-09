
def write_on_file(filename, to_write):
    # Scrittura sovrascrittura (modalità 'w')
    with open(filename, 'a') as f:
        f.write(to_write + "\n")
        f.close()

def read_file(filename):
    # lettura (modalità 'r')
    with open(filename, 'r') as f:
        return f.read()

