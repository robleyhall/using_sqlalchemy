from db_connect import connect
from sqlalchemy import Table, Column, Integer, String, ForeignKey


con, meta = connect('ic4vuser', 'ibm', 'ic4v')

customers = Table('customers', meta,
    Column('name', String, primary_key=True),
    Column('contact_email', String)
)

instances = Table('instances', meta,
    Column('customer', String, ForeignKey('customers.name')),
    Column('instance_name', String),
    Column('datacenter', String)
)

# Create the above tables
meta.create_all(con)
