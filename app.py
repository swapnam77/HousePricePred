# importing the required libraries  
from time import sleep  
from json import dumps  
from kafka import KafkaProducer 
import os
# initializing the Kafka producer  
my_producer = KafkaProducer(  
    bootstrap_servers = ['localhost:9092'],  
    value_serializer = lambda x:dumps(x).encode('utf-8')  
    )  
