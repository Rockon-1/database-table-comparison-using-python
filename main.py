'''/*********************************************************************************
Script    : Comparison between 2 tables
Date      : 29/06/22
version   : v1.0
Author    : Sachin Goyal
*********************************************************************************
Description :
Compare source table and destination table exist in same or different database.
it compared table structure and data.
*********************************************************************************
*********************************************************************************
VERSION     BY         DATE        DESCRIPTION
  1.0     sachin     29/06/22     Initial version
*********************************************************************************/
'''


# importing module
import cx_Oracle
from datetime import datetime

import pandas
import conf
import datacompy

# Create a table in Oracle database
cursor1=None
con1=None
cursor2=None
con2=None
index=0
flag=True

squery1="""select count(*) from """
squery2="""select * from """

queries1=[squery1+conf.source_table, squery2+conf.source_table]
queries2=[squery1+conf.destination_table, squery2+conf.destination_table]



def getPrimarykeyQuery(table):
    return """SELECT cols.column_name
    FROM all_constraints cons, all_cons_columns cols
    WHERE 
    cols.table_name = '"""+table+"""' AND
    cons.constraint_type = 'P'
    AND cons.constraint_name = cols.constraint_name
    AND cons.owner = cols.owner
    ORDER BY cols.table_name, cols.position"""

try:
    #cx_Oracle.init_oracle_client(lib_dir="C:\Oracle\instantclient_21_6")
    dsn_tns2 = cx_Oracle.makedsn(conf.server_db2, conf.port1, conf.server_db2)
    con2 = cx_Oracle.connect(user=conf.username_db2, password=conf.password_db2, dsn=dsn_tns2)
    con2.ping()

    dsn_tns1 = cx_Oracle.makedsn(conf.server_db1, conf.port1, conf.server_db1)
    con1 = cx_Oracle.connect(user=conf.username_db1, password=conf.password_db1, dsn=dsn_tns1)
    con1.ping()
    
    cursor1=con1.cursor()
    result1=cursor1.execute(queries1[index]).fetchall()
    if (len(result1)==0):
        #raise Exception('no data found for Source Table')
        print('data Not found in Source Table')
    cursor2 = con2.cursor()
    result2=cursor2.execute(queries2[index]).fetchall()
    if len(result2)==0:
        #raise Exception('no data found for destination table')
        print('Data Not found in Destination Table')
    if (result1[0][0]!=result2[0][0]):
        flag=False
        #raise Exception("count did not match result 1 ",result1,"\n result 2", result2)
        print('Rows count did not match \n source table rows => ',result1[0][0],"\n destination table rows => ", result2[0][0])
    else:
        print("source and destination table both have ",result1[0][0],"rows")
    index+=1

    # update query for sort by primary key
    source_primarkey_result=cursor1.execute(getPrimarykeyQuery(conf.source_table.split('.')[-1].strip())).fetchall()
    destination_primarykey_result=cursor2.execute(getPrimarykeyQuery(conf.destination_table.split('.')[-1].strip())).fetchall()
    if len(source_primarkey_result)>0:
        queries1[index]+=" order by "+",".join([x[0] for x in source_primarkey_result])

    if (len(destination_primarykey_result)>0):
        queries2[index]+=" order by "+",".join([x[0] for x in destination_primaryKey_result])
    # print(queries1,"\n",queries2)

    result1=cursor1.execute(queries1[index]).fetchall()
    result2=cursor2.execute(queries2[index]).fetchall()
    #print(cursor1.description, result1)
    if cursor1.description!=cursor2.description:
        flag=False
        print("cursor Defination mismatch (sorce and destination table does not have same structure)")
        # raise Exception(" cursor Defination mismatch")
    else:
        print("Cursor defination matches")
    index+=1
    result1=pandas.DataFrame(result1)
    result2=pandas.DataFrame(result2)

    compare=datacompy.Compare(result1,result2,on_index=True)

    print(compare.report())
    print("-------------------------------\n Comparison Result:- ",compare.matches() and flag)

except cx_Oracle.DatabaseError as e:
    print("Error-------------Oracle------------- " ,"\n",e)

except Exception as e:
    print("Error------------Exception---------- ","\n",e)

# by writing finally if any error occurs
# then  we can close the all database operation
finally:

    if cursor2:
        cursor2.close()
    if cursor1:
        cursor1.close()
    if con1:
        con1.close()
    if con2:
        con2.close()
    input("press any key to exist")

