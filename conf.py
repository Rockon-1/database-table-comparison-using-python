#--------------------------Oracle--------------------------------------------------------

#enter servername for source database (to connect with database) like 'x12345' in string type
server_db1='x12345'
#enter port Number for source database (to connect with database) like 1500 in int type
port1=1525
#enter username for source database (to connect with database) like 'Username' in string type
username_db1 = 'Username'
#enter password for source database (to connect with database) like '''Password''' in comment type as password may contain special characters
password_db1 = """Password"""
#Enter source table name (for comparing source data)
source_table='SOURCE_TABLE_NAME'


# Enter destination database details
# if source table and destination table exist in same database then enter same above details
# enter servername for destination database (to connect with database)
server_db2='x54321'
#enter port Number for destination database (to connect with database)
port2 = 1525
#enter username for destination database (to connect with database)
username_db2 = 'Destination Username'
#enter password for destination database (to connect with database)
password_db2 = """Destination_password"""
#€nter destination table name (for comparing destination data)
destination_table='DESTINATION_TABLE_NAME'
