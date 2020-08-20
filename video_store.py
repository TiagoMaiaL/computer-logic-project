import csv

CLIENTS_PATH = './clients.csv'
NAME_KEY = 'name'
CPF_KEY = 'cpf'
RG_KEY = 'rg'
CLIENTS_FIELD_NAMES = [NAME_KEY, CPF_KEY, RG_KEY]

MOVIES_PATH = './movies.csv'
TYPE_KEY = 'type'
CODE_KEY = 'code'
NAME_KEY = 'name'
YEAR_KEY = 'year'
MOVIES_FIELD_NAMES = [TYPE_KEY, CODE_KEY, NAME_KEY, YEAR_KEY]

def write(header, content, path):
    """
    Given the header of a csv file, the content of a row, and the file path,
    writes the content row into the csv file.
    """

    file = open(path, 'w')

    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerow(content)

def hasEntry(key, value, path):
    """
    Given the key and value of an entry, and the csv file path,
    returns if the csv contains an entry with the provided value.
    """

    didFind = False
    
    try:
        reader = csv.DictReader(open(path))
        for entry in reader:
            if entry[key] == value:
                didFind = True
    except:
	didFind = False
    
    return didFind

def storeClient(name, cpf, rg):
    """
    Given the name, cpf, and rg of a client,
    stores it into the clients.csv file.
    """
    if not hasEntry(CPF_KEY, cpf, CLIENTS_PATH):
        clientData = {
            NAME_KEY: name,
            CPF_KEY: cpf,
            RG_KEY: rg
        }
        write(CLIENTS_FIELD_NAMES, clientData, CLIENTS_PATH)
    
storeClient('testing', '022-222-123-21', '123.232.12')

def storeMovie(type, code, name, year):
    """
    Given the type, code, name and year of a movie,
    stores it into movies.csv file.
    """
    if not hasEntry(CODE_KEY, code, MOVIES_PATH):
        movieData = {
            TYPE_KEY: type,
            CODE_KEY: code,
            NAME_KEY: name,
            YEAR_KEY: year
        }
        write(MOVIES_FIELD_NAMES, movieData, MOVIES_PATH)

storeMovie("dvd", 0223, "test", 2001)

