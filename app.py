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

kubectl create deployment --image=cnfldemos/orders-service:sha-844f538
    apiVersion: apps/v1
kind: Deployment
metadata:
  name: orders-service
spec:
  replicas: 1
  containers:
    - name: orders-service
      image: cnfldemos/orders-service:sha-844f538
            kubectl apply -f orders-service-deployment.yaml
            function common::get_config() {
  cat <<EOF
configVersion: v1
kubernetes:
- name: ConnectConfigMapMonitor
  apiVersion: v1
  kind: ConfigMap
  executeHookOnEvent: ["Added","Deleted","Modified"]
  labelSelector:
	matchLabels:
  	  destination: ccloud
  namespace:
	nameSelector:
  	  matchNames: ["default"]
  jqFilter: ".data"
EOF
}
