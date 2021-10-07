from kafka import KafkaProducer
import json
#pip install kafka-python

#Connection information
conf = {
    'bootstrap_servers': ["host:port"],
    'topic_name': 'topic_name',
    'sasl_plain_username': 'username',
    'sasl_plain_password': 'password',
    'sasl_mechanism':'SCRAM-SHA-512',
    'security_protocol':'SASL_PLAINTEXT'
}

#Creating test json object
jsonData = {
  "event": {
    "kind": "event",
    "outcome": "success",
    "code": "4627"
  },
  "log": {
    "level": "information"
  },
  "message": "Test message",
  "host": {
    "name": "kevin-host"
  },
}

#Creating producer
producer = KafkaProducer(bootstrap_servers=conf['bootstrap_servers'],
                        sasl_mechanism=conf['sasl_mechanism'],
                        security_protocol=conf['security_protocol'],
                        sasl_plain_username=conf['sasl_plain_username'],
                        sasl_plain_password=conf['sasl_plain_password'],
                        #If sending json, we have to convert the python object into a json string and then encode it
                        value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#Sending message to Kafka
producer.send(conf['topic_name'], jsonData)
producer.flush() #send message as soon as record is available to producer
#producer.close()