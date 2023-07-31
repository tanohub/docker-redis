#!/usr/bin/python3
from redis.sentinel import Sentinel

# Set the Sentinel IP address and port
sentinel_ip = "127.0.0.1"
sentinel_port = 2631

# Set the Master name
master_name = "mymaster"
master_password = "Password123"

# Set key and value
key = 'python_key'
value = 'python_value'

# Create redis sentinel client
client = Sentinel([(sentinel_ip, sentinel_port)], socket_timeout=0.1)

# Create redis MASTER client
master = client.master_for(master_name,password=master_password, socket_timeout=0.1)

# Discover master via discover_master
print( "Master: -->", client.discover_master(master_name))

# Set key on master
master.set(key, value)

# Discover slaves via discover_slaves
slave_list = client.discover_slaves(master_name)
print("Slave list: -->", slave_list)

# Iterate slave list
for item in slave_list:
	slave_address = item[0]
	slave_port = item[1]
	print("slave addr:", slave_address, " --- slave port:", slave_port)

# Create redis SLAVE client
slave = client.slave_for(master_name, password=master_password, socket_timeout=0.1)

# get key on slave ( choosen from SLAVE client )
print("Value is:", slave.get(key))

