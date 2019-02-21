import pyodbc
[x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]