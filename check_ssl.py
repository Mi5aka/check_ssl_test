import re
import os
import ssl
import socket
from multiprocessing import Pool


def prepare_data(obj):
    obj = re.split('https://|/|\n', obj)
    return obj[0] if obj[0] else obj[1]


def get_hosts():
    with open('input.txt', 'r') as file:
        return list(map(prepare_data, file.readlines()))


def write_data(data):
    with open('output.csv', 'w') as file:
        for obj in data:
            if obj:
                file.write(f'{obj}\n')


def is_valid_hostname(hostname):
    if len(hostname) > 255:
        return False
    if hostname[-1] == '.':
        hostname = hostname[:-1]
    allowed = re.compile('(?!-)[A-Z\d-]{1,63}(?<!-)$', re.IGNORECASE)
    return all(allowed.match(x) for x in hostname.split('.'))


def check_ssl(obj):
    if is_valid_hostname(obj):
        try:
            context = ssl.create_default_context()
            conn = context.wrap_socket(
                socket.socket(socket.AF_INET),
                server_hostname=obj
            )

            conn.connect((obj, 443))
            cert = conn.getpeercert()
            return f"{obj}_{cert['notAfter'].replace(' ', '_')}"
        except ssl.SSLError:
            return


if __name__ == '__main__':
    result = []
    data = get_hosts()
    with Pool(os.cpu_count()) as p:
        result.extend(p.map(check_ssl, data))
    write_data(result)
