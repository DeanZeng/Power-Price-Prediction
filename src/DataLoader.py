import csv

class Table:
    def __init__(self, header, data):
        self.header = header
        self.data = data
        
        
def test_load_borzen_consumption():
    """Load power consumption of various suppliers."""
    print("Load test borzen consumption.")
    file_name = '/Users/ales/Desktop/STUDIJ/DodatnoLeto/MatematikaZracunalnikom/Borzen/Odjem/PDO_PRO_ODJ_2016.csv/01 2016-Table 1.csv'
    # open file and read content in a csv format
    csvfile = open(file_name, 'r')
    reader = csv.reader(csvfile, delimiter=';')
    # get header and clean data
    data = list(reader)
    header = data[7]
    data_clean = data[9:]
    # finish
    print("Loading test borzen consumption successful!")
    return Table(header, data_clean)


def test_load_borzen_price():
    """Load power prices."""
    print("Load test borzen prices.")
    file_name = '/Users/ales/Desktop/STUDIJ/DodatnoLeto/MatematikaZracunalnikom/Borzen/Cena/Cp_in_Cn_2017_/01 2017-Table 1.csv'
    # open file and read content in a csv format
    csvfile = open(file_name, 'r')
    reader = csv.reader(csvfile, delimiter=';')
    # get header and clean data
    data = list(reader)
    header = data[7]
    data_clean = data[9:]
    # finish
    print("Loading test borzen prices successful!")
    return Table(header, data_clean)
    
          

def test_load_ksedlo():
    """Load weather data for Korenjsko sedlo that has been dowloaded 
    from ARSO website."""
    print('Start loading korenjsko sedlo')
    import csv
    test_file_ksedlo = '/Users/ales/Desktop/STUDIJ/DodatnoLeto/MatematikaZracunalnikom/WeatherDataTest/KorenjskoSedloTest'
    # open file and read content in a csv format
    csvfile = open(test_file_ksedlo, 'r')
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)
    # extract header and clean up data by removing empty lines
    header = data[0]
    data_clean = data[2:len(data):2]
    data_deleted = data[1:len(data):2]
    # check if deleted data is really empty
    for lst in data_deleted:
        if len(lst) != 0:
            # there is a non empty line
            print("Warning: not empty line " + lst)
            return None
    # finish
    print('Loading successful')
    return Table(header, data_clean)
    