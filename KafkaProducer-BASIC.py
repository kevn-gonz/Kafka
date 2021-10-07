from kafka import KafkaProducer
#pip install kafka-python

producer = KafkaProducer(bootstrap_servers=['host:port'])
producer.send('topic_name', b'This is a test message')
producer.flush()
#producer.close()