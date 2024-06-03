from terminaltables import AsciiTable

from elements import elements 


data = [[] for i in range(7)]

for element in elements:
    # breakpoint()
    try:
        group_list = data[int(element.period) - 1]
        group_list.append(f"{element.symbol}")
    except:
        pass

table = AsciiTable(data)
# print(table.table)
breakpoint()
