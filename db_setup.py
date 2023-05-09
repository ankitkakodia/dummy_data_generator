import pymysql
from setting import *

conn = pymysql.connect(host=host, user=user, password=password)
cur = conn.cursor()

create_db = f"""create database if not exists {database};"""
cur.execute(create_db)
# print('db created')
cur.execute(f"""use {database};""")

create_table = f"""create table if not exists user (id int auto_increment primary key,name varchar(25),email_id varchar(30), phone varchar(10), password varchar(256));"""
cur.execute(create_table)
# print('users table created')

create_table = f"""create table if not exists transactions (id int auto_increment primary key,user_id int, transaction_date varchar(64),total_amount int);"""
cur.execute(create_table)
# print('transactions table created')

create_table = f"""create table if not exists transactions_details (id int auto_increment primary key,transaction_id int, item_name varchar(40),quantity int, price int);"""
cur.execute(create_table)
# print('transactions_details table created')

create_table = f"""create table if not exists products (id int auto_increment primary key,product_name varchar(50), category varchar(40),price int);"""
cur.execute(create_table)

# conn.close()