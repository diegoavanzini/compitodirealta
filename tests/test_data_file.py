from src.data_file import write_on_file, read_file

def test_write_on_file():
    write_on_file('../compiti.txt', "12/04/2026;test titolo;test descrizione breve;\n")
    assert read_file('../compiti.txt', ) == "12/04/2026;test titolo;test descrizione breve;\n"


def test_read_from_file():
    assert read_file('../compiti.txt', ) == "12/04/2026;test titolo;test descrizione breve;\n"