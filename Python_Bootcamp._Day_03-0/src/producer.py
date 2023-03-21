import json
import random
import redis
import logging


def main():
    redis_conn = redis.Redis(host='localhost', port=6379, db=0)

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    def generate_message():
        from_account = str(random.randint(1000000000, 9999999999))
        to_account = str(random.randint(1000000000, 1000000003))
        amount = random.randint(-100000, 100000)
        message = {
            "metadata": {
                "from": from_account,
                "to": to_account
            },
            "amount": amount
        }
        return json.dumps(message)

    for i in range(10):
        msg = generate_message()
        redis_conn.publish('transactions', msg)
        logger.info(f"Produced message: {msg}")


if __name__ == '__main__':
    main()
