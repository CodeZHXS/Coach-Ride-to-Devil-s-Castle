from client.client import Client
import sys

client = Client('127.0.0.1', 17623)
client.register(sys.argv[1])
client.close()

