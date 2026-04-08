
def write_on_file(filename, to_write):
    # Scrittura sovrascrittura (modalità 'w')
    with open(filename, 'w') as f:
        f.write(to_write)
        f.close()

def read_file(filename):
    # letturaa (modalità 'w')
    with open(filename, 'r') as f:
        return f.read()

