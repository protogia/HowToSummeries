# How to install and setup kafka 


## download and unpack
```
cd /opt/
curl "https://dlcdn.apache.org/kafka/3.1.0/kafka_2.13-3.1.0.tgz"
tar xvfz https://dlcdn.apache.org/kafka/3.1.0/kafka_2.13-3.1.0.tgz --output "kafka_2.13-3.1.0" 
```

Kafka needs at least java8 to run. Make sure you have installed it.

## create systemunits with files from this repo
```
git clone +++
sudo mv kafka.service /etc/systemd/system/
sudo mv zookeeper.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo sysemctl start zookeeper.service
sudo systemctl start kafker.service
```

## Quickstart
To run a quickstart check out https://kafka.apache.org/quickstart

### shortcuts
```
# create topic
bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092

# write into this topic using console-producer
bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
# read from thgis topic using console-consumer
bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092
```
