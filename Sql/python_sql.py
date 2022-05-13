import mysql.connector
from datetime import datetime, timedelta

mydb = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    password = "" 
)

mycursor = mydb.cursor()

mycursor.execute("use example")
#mycursor.execute("show tables")
mycursor.execute("select * from guarantee_info")

#query = "alter table guarantee_info \
#        add expire_date varchar(100)"

#mycursor.execute(query)

results = mycursor.fetchall()

format_1 = "%d-%m-%Y"
format_2 = "%b %d, %Y"
#format_3 = "%m-%d-%Y"

for x in results:
    #print(list(x))
    #print(list(x)[2])
    #print(list(x)[4])
    
    try:
        
        expire_date_temp = datetime.strptime(list(x)[2], format_1)
    
    except ValueError:
        
        expire_date_temp = datetime.strptime(list(x)[2], format_2)
        
    #warranty_temp = items_sold[i]["guarantee_info"]["warranty_period"]
    warranty_days = list(x)[1] * 7
    expire_date_update = str(expire_date_temp + timedelta(days = warranty_days)).replace(" 00:00:00","")

    #print(expire_date_update)
    order_id = list(x)[0]
    #print(order_id)

    #insert_query = "INSERT INTO guarantee_info(expire_date) VALUES (%s) WHERE id = %s"
    update_query = "update guarantee_info set expire_date = %s where id = %s"
                    
    mycursor.execute(update_query, (expire_date_update, order_id))
    mydb.commit()
