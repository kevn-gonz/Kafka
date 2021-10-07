from kafka import KafkaProducer
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

#Creating producer
producer = KafkaProducer(bootstrap_servers=conf['bootstrap_servers'],
                        sasl_mechanism=conf['sasl_mechanism'],
                        security_protocol=conf['security_protocol'],
                        sasl_plain_username=conf['sasl_plain_username'],
                        sasl_plain_password=conf['sasl_plain_password'])

#Sending message to Kafka
data = bytes("This is a test", encoding="utf-8")
producer.send(conf['topic_name'], data)
producer.flush() #send message as soon as record is available to producer
#producer.close()