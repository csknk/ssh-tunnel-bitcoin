# SSH Tunnel: Python
Simple demo project showing SSH Tunnel setup in Python.

Objective
---------
Set up an SSH tunnel based on parameters set in a config file.

Config
------
Config file is in JSON format:

```json
{
	"local_port": 5555,
	"remote_port": 18443,
	"remote_user": "alice",
	"remote_host": "111.222.43.232",
	"rpc_user": "alice",
	"rpc_password": "password123"
}
```
SSH Tunnel
----------
SSH is a standard for secure remote login and file transfer over untrusted networks.

SSH can be set up to use port forwarding to tunnel any TCP/IP port over SSH. Because data flows over an SSH connection, it is encrypted in transit. This makes SSH tunneling an obvious choice when sending and receiving sensitive data.

This example involves connecting to a remote `bitcoind` RPC-JSON server over an SSH tunnel. The application does not allow HTTPS connection.

Without SSH tunneling (or similar encrypted channel) sensitive information such as authentication data, addresses and Bitcoin amounts would be sent over a public network in cleartext.

When set up, the SSH tunnel forwards any traffic sent to a specified port on localhost to a specified port on a remote host.

Taking the sample config data shown above, the SSH tunnel would forward data sent to `localhost:5555` to `111.222.43.232:18443`.

"Manual" Setup
--------------
You can easily set up an SSH tunnel by running the following terminal command:

```
ssh -v -fNL 5555:111.222.43.232:18443 remote_user@111.222.43.232
```
Once this process is running, a connection can be made to `111.222.43.232:18443` by sending requests to `http://127.0.0.1:5555`. SSH will encrypt and forward data sent to this port on localhost and send it to the remote host, where it is forwarded to the specified remote port.

CURL Request
------------
The HTTP request is analagous to:

```bash
curl --user alice:password123 --data-binary '{"jsonrpc":"1.0","id":"curltext","method":"listunspent","params":[]}' -H 'content-type:text/plain;' http://127.0.0.1:5555
```

Resources
---------
* [ssh.com][1], SSH Tunnel
* [OpenSSH Cookbook: Tunnels][2]
* [Useful SO Answer][3]

[1]: https://www.ssh.com/ssh/tunneling/
[2]: https://en.wikibooks.org/wiki/OpenSSH/Cookbook/Tunnels
[3]: https://stackoverflow.com/a/26656622/3590673
