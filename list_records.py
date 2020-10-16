from db_connect import connect
from sqlalchemy import Table, Column, Integer, String, ForeignKey

con, meta = connect('ic4vuser', 'ibm', 'ic4v')

customers = meta.tables['customers']
instances = meta.tables['instances']

customer_rows = con.execute(customers.select())
instance_rows = con.execute(instances.select())

print('\nCustomer records')
for customer in customer_rows:
    print(customer)

print('\nInstance records')
for instance in instance_rows:
    print(instance)
