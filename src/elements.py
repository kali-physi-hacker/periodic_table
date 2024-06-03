import csv

from terminaltables import AsciiTable


class Element:
    def __init__(self, name, symbol, atomic_number, neutron_number, **kwargs):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number 
        self.neutron_number = neutron_number
        self.mass_number = atomic_number + neutron_number

        # set the remaining fields
        for field, value in kwargs.items():
            setattr(self, field, value)
    
    def __repr__(self):
        return f"∞{self.symbol}: {self.atomic_number}"

periodic_table_filepath = "periodic_table_data.csv"

with open(periodic_table_filepath) as file:
    reader = csv.reader(file)

    header = [item.lower() for item in next(reader)]
    rows = [row for row in reader]


elements_data = [dict(zip(header, row)) for row in rows]
elements = []
for data in elements_data:
    kwargs = data.copy()
    name = kwargs.pop("name")
    atomic_number = kwargs.pop("atomic_number")
    symbol = kwargs.pop("symbol")
    neutron_number = kwargs.pop("neutron_number")
    
    element = Element(name=name, atomic_number=atomic_number, symbol=symbol, neutron_number=neutron_number, **kwargs)
    elements.append(element)
    globals()[name.lower()] = element


class ObjectsManager:
    FIELDS = tuple(vars(elements[0]).keys())

    def filter(self, **filters):
        """
        Usage: Manage.filter(name="Hydrogen", period="1")
        """
        filter_results = list(filter(lambda element: all([getattr(element, field) == filters[field] for field in filters]), elements))
        return filter_results

    def get(self, **filters):
        """
        Usage: Manager.get(name="Hydrogen")
        """ 
        results = self.filter(**filters)
        return results[0]


class PeriodicTable:
    objects = ObjectsManager()
    @staticmethod
    def print_table():
        data = [['' for _ in range(18)] for _ in range(7)]
        for element in elements:
            if element.period and element.group:
                period = data[int(element.period) - 1]
                period[int(element.group) - 1] = element.symbol 

        table = AsciiTable(data)
        print(table.table)



