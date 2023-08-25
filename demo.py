import sys

import sqlalchemy

#import ingres_sa_dialect

 

print('Python %s on %s' % (sys.version, sys.platform))

print('SQLAlchemy %r' % sqlalchemy.__version__)

con_str = 'ingres://dbuser:dbuser#@av-medy9l3pk6zc.avprod.actiandatacloud.com:27832/db'  # local demodb

#con_str = 'ingres://dbuser:PASSWORD@HOSTNAME:27832/db'  # remote database called "db"

print(con_str)

# If the next line is uncommented, need to also uncomment: import ingres_sa_dialect

#print(ingres_sa_dialect.base.dialect().create_connect_args(url=sqlalchemy.engine.make_url(con_str)))

 

engine = sqlalchemy.create_engine(con_str)

connection = engine.connect()

query = 'SELECT * FROM employee'

for row in connection.execute(sqlalchemy.text(query)):

    print(row)