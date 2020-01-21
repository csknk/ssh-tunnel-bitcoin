import subprocess
from threading import Thread

class SSHTunnel(Thread):
    def __init__(self, local_port, remote_port, remote_user, remote_host):
        Thread.__init__(self)
        self.local_port = local_port
        self.remote_port = remote_port
        self.remote_user = remote_user
        self.remote_host = remote_host
        self.daemon = True

    def run(self):
        if subprocess.call([
            'ssh',
            '-N',
            '-L',
            str(self.local_port) + ':' + self.remote_host + ':' + str(self.remote_port),
            self.remote_user + '@' + self.remote_host
            ]):
            raise Exception("ssh tunnel setup failed.")
