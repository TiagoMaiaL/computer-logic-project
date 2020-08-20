import os.path
import csv
import datetime

CLIENTS_PATH = './clients.csv'
NAME_KEY = 'name'
CPF_KEY = 'cpf'
RG_KEY = 'rg'
CLIENTS_FIELD_NAMES = [NAME_KEY, CPF_KEY, RG_KEY]

MOVIES_PATH = './movies.csv'
TYPE_KEY = 'type'
CODE_KEY = 'code'
YEAR_KEY = 'year'
MOVIES_FIELD_NAMES = [TYPE_KEY, CODE_KEY, NAME_KEY, YEAR_KEY]

RENTS_PATH = './rents.csv'
DATE_KEY = 'date'
RENT_FIELD_NAMES = [NAME_KEY, CODE_KEY, DATE_KEY]

def write(header, content, path):
    """
    Given the header of a csv file, the content of a row, and the file path,
    writes the content row into the csv file.
    """

    alreadyExists = os.path.exists(path)

    file = open(path, 'a')

    writer = csv.DictWriter(file, fieldnames=header)

    if not alreadyExists:
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
            if entry[key] == str(value):
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
storeClient('testing2', '023-232-333-12', '111.111.11')

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

storeMovie("dvd", 223, "test", 2001)

def rentMovie(name, movieCode, date):
    """
    Given the name of a client, the code of a movie, and a date,
    rents the associated movie to the user.
    """

    if not hasEntry(CODE_KEY, movieCode, MOVIES_PATH):
        print("There's no movie with the passed code.")
        return

    if not hasEntry(NAME_KEY, name, CLIENTS_PATH):
        print("There isn't a person with the provided name")
        return

    rentEntry = {
        NAME_KEY: name,
        CODE_KEY: movieCode,
        DATE_KEY: date
    }
    write(RENT_FIELD_NAMES, rentEntry, RENTS_PATH)

def listLateRents():
    print("listing late entries")

today = datetime.datetime.now()
past_date = today - datetime.timedelta(days = 7)

print(today)
print(past_date)

rentMovie("testing", 223, today)

