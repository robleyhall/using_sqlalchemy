from db_connect import connect
from sqlalchemy import Table, Column, Integer, String, ForeignKey


con, meta = connect('ic4vuser', 'ibm', 'ic4v')

customers = meta.tables['customers']
instances = meta.tables['instances']

instances.drop()
customers.drop()
