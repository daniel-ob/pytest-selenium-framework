import csv


class DataCollector:
    def __init__(self, file):
        self.file = file

    def get_test_data(self):
        try:
            test_data = []
            with open(self.file, 'r') as csv_file:
                reader = csv.reader(csv_file)
                # skips first row of file (header)
                next(reader)
                # Format data to parameterize tests (list of tuples)
                test_data = [tuple(row) for row in reader]
                return test_data
        except FileNotFoundError:
            print("File %s not found" % self.file)
