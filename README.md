# using_sqlalchemy
example of how to using sqlalchemy to create two linked tables


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
