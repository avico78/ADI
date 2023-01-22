import pika, os,sys



url = os.environ.get("CLOUDAMQP_URL", "amqp://guest:guest@localhost:5672/")
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue="avi_test_queue" ,durable=True)

message = ' '.join(sys.argv[1:]) or "Hi aaaaaaaaaaaaa"
channel.basic_publish(exchange='',
                      routing_key="avi_test_queue",
                      body=message,
                      properties=pika.BasicProperties(
                        delivery_mode=2,
                      ))
print(" [x] Sent %r" % message)                      
connection.close()