import pandas

"""
docstring
"""
HEADERS = [['Представительство', 'Адрес1'], ['Склад', 'Адрес2'], ['Дочернее предприятие', 'Адрес3'],
           ['Центральный офис', 'Адрес4'], ['Корпус', 'Адрес5']]


def read_all(filename: str) -> list:
    return [pandas.read_excel(open(filename, 'rb'))[i].dropna() for i in HEADERS]


def read_col(filename: str, column_name: list[str]) -> pandas.DataFrame:
    return pandas.read_excel(open(filename, 'rb'), usecols=column_name, na_values=0).dropna()


def unite_to_exel(data: list[pandas.DataFrame]) -> None:
    for i in range(1, len(data)):
        data[0] = data[0].join(data[i], how='outer')
    data[0].to_excel('ipList.xlsx', index=False)


