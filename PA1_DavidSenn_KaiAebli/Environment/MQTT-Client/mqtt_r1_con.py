import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe to MQTT topic for Robot 1
        client.subscribe("dobot/r1")
    else:
        print(f"Failed to connect to MQTT broker, rc={rc}")

def on_message(client, userdata, message):
    # Handle incoming MQTT messages here
    print(f"Received message: {message.payload.decode()} on topic {message.topic}")

# Create MQTT client instance
client = mqtt.Client()

# Set callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT broker
broker_address = "test.mosquitto.org"
port = 1883
client.connect(broker_address, port)

# Start the MQTT loop to handle incoming messages
client.loop_forever()
