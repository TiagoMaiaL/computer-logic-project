import os.path
import csv
from datetime import datetime
from datetime import timedelta

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

DATE_FORMAT = '%d/%m/%y %H:%M:%S'

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

def getEntry(key, value, path):
    """
    Given the key and value of an entry, and the csv file path,
    returns the found entry in the csv, or none.
    """
    try:
        reader = csv.DictReader(open(path))
        for entry in reader:
            if entry[key] == value:
                return entry
    except:
        return None

    return None

def hasEntry(key, value, path):
    """
    Given the key and value of an entry, and the csv file path,
    returns if the csv contains an entry with the provided value.
    """
    return getEntry(key, value, path) != None
    

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
    """
    Lists all rents that are currently late.
    """
    try:
        didDisplayHeader = False
        rentsReader = csv.DictReader(open(RENTS_PATH))

        for rent in rentsReader:
            client = getEntry(NAME_KEY, rent[NAME_KEY], CLIENTS_PATH)
            movie = getEntry(CODE_KEY, rent[CODE_KEY], MOVIES_PATH)
            rentDate = datetime.fromisoformat(rent[DATE_KEY])
            today = datetime.now()

            difference = (today - rentDate).days

            if difference >= 7:
                if not didDisplayHeader:
                    didDisplayHeader = False
                    print('CPF|Name|Title|Rent_date|Situation|Days')

                print(client[CPF_KEY][:6], '|', client[NAME_KEY][:6], '|', movie[NAME_KEY], '|', datetime.strftime(rentDate, DATE_FORMAT), '|', "Late", '|', difference)

    except:
        print("Couldn't open rents.csv")

# Store two clients
storeClient('Jose Augusto', '123.222.312-12', '3.123.234')
storeClient('Sara Moura', '222.222.222-22', '1.223.245')
storeClient('Pedro Afonso', '204.252.231-22', '1.256.212')

# Store 6 DVDs
storeMovie('DVD', '123', 'Jumanji', '2001')
storeMovie('DVD', '124', 'Batman', '2000')
storeMovie('DVD', '125', 'Superman', '2015')
storeMovie('DVD', '126', 'Coringa', '2019')
storeMovie('DVD', '127', 'Ant Man', '2017')
storeMovie('DVD', '128', 'The Godfather', '1972')

today = datetime.now()
late_date = today - timedelta(days = 8)

# Make 2 rents (one late)
rentMovie('Jose Augusto', '123', today)
rentMovie('Sara Moura', '128', late_date)

# List late entries
listLateRents()
