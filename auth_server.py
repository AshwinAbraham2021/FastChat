# First client sends message to auth server containing uname, pwd
# Stores in db and checks
# If credentials don't match, then reject the user
# If they match, forward to other servers (load balancing)

import psycopg2
from threading import *
import socket
from auth_client_handler import *
import ports

#host and port
host = ports.auth_server_host
port = ports.auth_server_port
ThreadCount = 0

#connect to psycopg2
sql_conn = psycopg2.connect(database="authdb", user="ananth", password="ananth", host="127.0.0.1", port =  "5432")
sql_cur = sql_conn.cursor()
#create a table of usernames and passwords
# sql_cur.execute('''DROP TABLE AUTH_DATA''')
sql_cur.executemany('''
    SELECT EXISTS(
        SELECT FROM 
            pg_tables
        WHERE 
            tablename = 'AUTH_DATA' 
    );
''', '''
    IF (EXISTS IS NULL)
    THEN
        CREATE TABLE AUTH_DATA(
        USERNAME TEXT PRIMARY KEY,
        PASSWORD TEXT
        );
    END IF;
''')
sql_conn.commit()

#create the server socket
auth_server = socket.socket()
auth_server.bind((host, port))
auth_server.listen(1)

while True:
    Client, address = auth_server.accept()
    print ("connected")
    conn = Thread(target=auth_client_handler.interact, args = (Client,sql_conn))
    conn.start()