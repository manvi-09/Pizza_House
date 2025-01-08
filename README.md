
# PizzaQueue

This project demonstrates a Python-based pizza ordering application designed to streamline the process of placing and managing orders. By integrating Apache Kafka for real-time order queuing and processing, the system significantly reduces delays and enhances operational efficiency.


## Features

- **Real-Time Order Processing**: Utilizes Apache Kafka    for seamless handling of high-order volumes.
- **API-Driven Architecture:** Provides endpoints for creating, reading, updating, and deleting orders.
- **Scalable Design:** Built to handle growing demand efficiently.
- **Improved Analytics:** Detailed logging for operational insights.


## Tech Stack

**Programming Language:** Python

**Message Broker:** Apache Kafka

**Frameworks/Libraries:** Flask, Kafka-Python


## Architecture
- **Flask Application:** Hosts RESTful APIs for CRUD operations.
- **Apache Kafka:** Ensures real-time queuing and reliable message delivery.
- **Producer-Consumer Model:** Kafka producers handle incoming API requests, and consumers process these messages to update order states in real-time.
## Installation and Setup

**Prerequisites**
- Python 3.8+
- Apache Kafka

**Steps**

**1. Clone the Repository**
```bash
git clone https://github.com/manvi-09/PizzaQueue.git
cd PizzaQueue
```
**2. Install Dependencies**
```bash
pip install -r requirements.txt
```
**3. Set Up Kafka**
- Download and install Apache Kafka.
- Start Zookeeper and Kafka broker services:
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties
```
**4. Run the Application**
- Start the Flask server:
```bash
python app.py
```
- Start Kafka consumers to process messages.
    

