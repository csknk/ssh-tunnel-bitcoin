#!/usr/bin/env python3
from ssh_tunnel import SSHTunnel
import requests, time, json, sys
from pygments import highlight, lexers, formatters

def main(config):
    with open(config) as file:
        config_data = json.load(file)
    tunnel = SSHTunnel(
            config_data["local_port"],
            config_data["remote_port"],
            config_data["remote_user"],
            config_data["remote_host"]
            )
    tunnel.start()
    time.sleep(1)

    headers = {'content-type': 'text/plain;'}
    data = '{"jsonrpc":"1.0","id":"curltext","method":"listunspent","params":[]}'
    response = requests.post(
            "http://127.0.0.1:{}/".format(config_data["local_port"]),
            headers=headers, data=data, auth=(config_data["rpc_user"], config_data["rpc_password"])
            )
    response_dict = response.json()
    my_vals = [{
        'txid': x['txid'],
        'amount': x['amount'],
        'address': x['address'],
        'vout': x['vout']} for x in response_dict['result']]
    print(highlight(json.dumps(my_vals, indent=2), lexers.JsonLexer(), formatters.TerminalFormatter()))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please pass a path to a config file.")
    else:
        main(sys.argv[1])

