import subprocess
import pandas as pd
import multiprocessing.dummy


def ping_func(host: list[str]) -> str:
    try:
        result = subprocess.run(["ping", "-n", "1", host], capture_output=True, text=True,
                                creationflags=subprocess.CREATE_NO_WINDOW)
        if result.returncode == 0:
            return '✅'
        else:
            return '🔴'
    except subprocess.CalledProcessError:
        return '🔴'



def transact_data(table: pd.DataFrame) -> pd.DataFrame:
    try:
        if table['ping']:
            table.drop(columns=['ping'])
    except Exception:
        pass
    table['ping'] = ping_range(table[table.columns[1]])
    return table.sort_values(by="ping", ascending=False)


def ping_range(ping_list):
    return multiprocessing.dummy.Pool(40).map(lambda x: ping_func(x), ping_list)
