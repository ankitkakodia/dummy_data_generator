from db_setup import *
import random,string
from datetime import datetime

def generate_name():
    mail_domain = ['@gmail.com','@hotmail.com','@yahoo.in','@blinkit.com']
    first_name = ''
    second_name = ''
    for el in range(random.randint(3,10)):
        first_name += random.choice(string.ascii_lowercase)
    for el in range(random.randint(3,10)):
        second_name += random.choice(string.ascii_lowercase)
    name = first_name +" "+ second_name
    email_id = first_name[:3]+second_name[-2:]+random.choice(mail_domain)
    phone = random.randint(6000000001,10000000000)
    password = str(phone)[:4]+'!'+first_name

    # password = hashlib.sha256((str(phone)[:4]+random.choice(string.punctuation)+first_name).encode())
    # password = password.hexdigest()

    select = f"select name from user;"
    cur.execute(select)
    if name not in cur.fetchall():
        insert = f"insert into user (name,email_id,phone,password) values('{name}','{email_id}','{phone}','{password}');"
        cur.execute(insert)
        conn.commit()
    

def generate_product():
    product_name= ''
    for pd in range(random.randint(3,16)):
        product_name += random.choice(string.ascii_lowercase)
    category = random.choice(string.ascii_uppercase)
    price = random.randint(5,500)

    select = f"select product_name from products;"
    cur.execute(select)
    if product_name not in cur.fetchall():
        insert = f"insert into products (product_name,category,price) values ('{product_name}','{category}','{price}');"
        cur.execute(insert)
        conn.commit()
    

def generate_transaction():
    num = int(input("Please enter no. of Products in Transaction: "))
    total_amount = 0
    product_list = []
    price_list =[]
    qty_list = []
    t_date = datetime.now().strftime("%y/%m/%d %H:%M:%S")
    for transactions_details in range(num):
        select = f"select product_name, price from products;"
        cur.execute(select)
        out = cur.fetchall()
        if (len(out) == 0):
            print('No Product Available')
            break     
        else:
            product_name,price= random.choice(out)
            item_qty = random.randint(1,6)
            product_list.append(product_name)
            price_list.append(price)
            qty_list.append(item_qty)
            total_amount += price*item_qty
    
    if product_list:
        select = f"select id from user;"
        cur.execute(select)
        output = cur.fetchall()
        if (len(output) == 0):
            print('No User Available')
        else:
            user_id = random.choice(output)[0]
            insert = f"insert into transactions (user_id,transaction_date,total_amount) values({user_id},'{t_date}',{total_amount});"
            cur.execute(insert)
            conn.commit()
                
            select = f"select id from transactions order by id DESC limit 1;"
            cur.execute(select)
            txn_id = cur.fetchall()[0][0]

            for i in range(len(product_list)):
                insert = f"insert into transactions_details (transaction_id,item_name,quantity,price) values ({txn_id},'{product_list[i]}',{qty_list[i]},{price_list[i]});"
                cur.execute(insert)
                conn.commit()
            print("Tranasction Successfully")
                
        

    