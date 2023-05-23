# ASMT k8s cheat sheet
## Cluster section
<br />

### AKHQ:
> Install akhq:
```less
helm repo update
helm install akhq akhq/akhq -n elk-kafka --version 0.2.1 -f akhq-dev-pod.yaml
```
> Update/Apply new changes to akhq:
```less
helm upgrade akhq akhq/akhq -n elk-kafka -f akhq-dev-pod.yaml
```
> Delete/uninstall akhq:
```less
helm uninstall -n elk-kafka akhq
```
<br />

### Kafka:
> Install Kafka:
```less
First install the corresponding metrics:
kubectl apply -n elk-kafka -f kafka-dev-cluster-kafka-metrics.yaml

Second install Kafka: 
kubectl apply -n elk-kafka -f kafka-dev-cluster-kafka-cluster.yaml
```
> Apply changes to kafka:
```less
kubectl apply -n elk-kafka -f kafka-dev-cluster-kafka-cluster.yaml
```
> Get the current yaml configuration of Kafka:
```less
kubectl get k -n elk-kafka -o yaml
```
> Get the Kafka cluster information:
```less
kubectl get k -n elk-kafka
```
> Delete Kafka:
```less
kubectl delete k -n elk-kafka kafka-dev-cluster
```
<br />

## Users Section:
> Create new user:
```less
kubectl apply -n elk-kafka -f global-logstash-consumer.yaml
```
> Get secrets (user) from cluster:
```less
kubectl get secrets -n elk-kafka
```
> Delete secret (user) from the cluster:
```less
First delete the user
kubectl delete ku -n elk-kafka beat-producer

Second delete the secret:
kubectl delete secret -n elk-kafka beat-producer
```
<br />

## Topics section
> Create/Apply changes to a specific topic:
```less
kubectl apply -n elk-kafka -f createTopic-test-topic.yaml
```
> Create/Appy changes to several topics in a folder/directory yaml files
```less
kubectl apply -n elk-kafka -f topics
```
> Delete existing topic:
```less
kubectl delete kt -n elk-kafka test-topic
```
> Get topic details:
```less
kubectl get kt -n elk-kafka test-topic
kubectl describe kt -n elk-kafka test-topic
```
> Apply changes/Create specific topic:
```less
kubectl apply -n elk-kafka -f createTopic-test-topic.yaml
```
> Get entire list of kafka topcis:
```less
kubectl get kt -n elk-kafka
```
> Get entire list of kafka users:
```less
kubectl get ku -n elk-kafka
```
<br />

---

## Final notes
- The full format of kt, ku, etc is kafkatopics.kafka.strimzi.io. More info can be found [here](https://strimzi.io/blog/2020/07/22/tips-and-tricks-for-running-strimzi-with-kubectl/) </br>
Example: </br>
```less
kubectl get -n elk-kafka kafkas.kafka.strimzi.io
kubectl get k -n elk-kafka
-----------------------------------------------------
kubectl delete -n elk-kafka kafkatopics.kafka.strimzi.io test-topic
kubectl delete kt -n elk-kafka test-topic
```
---
# IMPORTANT notes

> First create the topic AND THEN you can specify the topic name in the Logstash pipeline, if you specify the topic name in the pipeline and the topic doesn't exist yet, it may cause Logstash to crash 

> 