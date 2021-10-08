# Kafka producers

These scripts can be used to produce data and send it to any Kafka arquitecture.

* KafkaProducer-BASIC .py
    * Use this script for BASIC arquitectures, the script basically needs
* Kafkaroducer-Json-SASL_PLAINTEXT.py
    * Use this script for JSON formatted messages AND if you are using SASL PLAINTEXT authentication (SASL mechanism: SCRAM-SHA-512). You can change the SASL mechanism if you want it to be SCRAM-SHA-256 or whatever other mechanism is supported by the "KafkaProducer" python library
* KafkaProducer-SASL_PLAINTEXT.py
    * The same as the above one with the only difference that the messages will be sent in plain text, not JSON.