import argparse
import json
import redis


def process_message(msg, bad_guys):
    message = json.loads(msg)
    from_account = message['metadata']['from']
    to_account = message['metadata']['to']
    amount = message['amount']

    if to_account in bad_guys and amount > 0:
        message['metadata']['from'] = to_account
        message['metadata']['to'] = from_account

    return json.dumps(message)


def main(bad_guys):
    redis_conn = redis.Redis(host='localhost', port=6379, db=0)
    pubsub = redis_conn.pubsub()
    pubsub.subscribe('transactions')

    for msg in pubsub.listen():
        if msg['type'] == 'message':
            processed_msg = process_message(msg['data'], bad_guys)
            print(processed_msg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', type=str, required=True,
                        help='comma-separated list of bad guys account numbers')
    args = parser.parse_args()
    b_guys = set(args.e.split(','))

    main(b_guys)
