blockchain = []


def get_last_blockchain_value():
    """Returns the last blockchain value"""
    return blockchain[-1]


def add_value(value, last_transaction=[1]):
    blockchain.append([last_transaction, value])


def get_user_input():
    return float(input('Enter Transaction amount: '))


add_value(get_user_input())

add_value(get_user_input(), get_last_blockchain_value())

add_value(get_user_input(), get_last_blockchain_value())

print(blockchain)
