# using_sqlalchemy
example of how to using sqlalchemy to create two linked tables

assumes macos (hence brew) but that is the only piece of this that should be mac-specific

# setup

## install required packages
1. postgres

  brew install postgres
  
2. sqlalchemy

  pip install sqlalchemy
  
3. psycopg2

  pip install psycopg2-binary

## start/restart postgres
brew services restart postgres

## create database
createdb ic4v

## create db user
create user ic4vuser --password

(at password prompt enter password `ibm`)

# Using the samples

## create the tables

python create_tables.py

## insert some records

python insert_records.py

## list the records

python list_records.py

## drop the tables to cleanup

python drop_tables.py
