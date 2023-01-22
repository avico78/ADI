import pika, sys, os,time


def main():
    
    url = os.environ.get("CLOUDAMQP_URL", "amqp://guest:guest@localhost:5672/")
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel

    channel.queue_declare(queue='avi_test_queue' ,durable=True)


    def callback(ch, method, properties, body):
        print("body", body)
        print("body count",body.count(b'.'))
        if body.decode() == "hi":
            print("Hi trigger")
        elif body.decode() == "bye":
            print("bye")
            ch.basic_ack(delivery_tag=method.delivery_tag) #ackenlege is here , once it's completed it update as ackendlege 
            exit()

        print(" [x] Received %r" % body.decode())
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag) #ackenlege is here , once it's completed it update as ackendlege 

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='avi_test_queue', on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)