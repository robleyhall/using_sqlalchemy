from db_connect import connect
from sqlalchemy import Table, Column, Integer, String, ForeignKey

con, meta = connect('ic4vuser', 'ibm', 'ic4v')

customers = meta.tables['customers']
instances = meta.tables['instances']

con.execute(customers.insert().values(name='VMware', contact_email='head_honcho@vmware.com'))

thing_to_do = instances.insert().values(customer='VMware', instance_name='vcs1', datacenter='dal10')
con.execute(thing_to_do)
