import json
from faker import Faker

import pika

from model_user import User

fake = Faker()

credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        credentials=credentials
    )
)
channel = connection.channel()

exchange = "send_email"
queue_name = "hw_8"

channel.exchange_declare(exchange=exchange, exchange_type="direct")
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange, queue=queue_name)


def create_tasks(nums: int):
    for i in range(nums):
        user = User(
            fullname=fake.name(),
            email=fake.ascii_email()
            ).save()

        channel.basic_publish(
            exchange=exchange,
            routing_key=queue_name,
            body=str(user.id).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )

    connection.close()


if __name__ == "__main__":
    create_tasks(10)
