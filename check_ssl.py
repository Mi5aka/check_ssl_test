import re
import ssl
import socket
import validators
from multiprocessing import Pool


DATA = []


def prepare_data(obj):
    if 'http://' in obj:
        return None
    obj = re.split('https://|/|\n', obj)
    return obj[0] if obj[0] else obj[1]


def get_hosts():
    with open('input.txt', 'r') as file:
        DATA.extend(list(map(prepare_data, file.readlines())))
        return DATA


def write_data(data):
    with open('output.csv', 'w') as file:
        for obj in data:
            if obj:
                file.write(f'{obj}\n')


def check_ssl(obj):
    if validators.domain(obj):
        try:
            context = ssl.create_default_context()
            conn = context.wrap_socket(
                socket.socket(socket.AF_INET),
                server_hostname=obj
            )

            conn.connect((obj, 443))
            cert = conn.getpeercert()
            return f"{obj}_{cert['notAfter'].replace(' ', '_')}"
        except Exception as e:
            raise e


if __name__ == '__main__':
    get_hosts()
    with Pool(32) as p:
        result = list(p.map(check_ssl, DATA))
        write_data(result)
