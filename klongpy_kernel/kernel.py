import sys
from io import StringIO
from ipykernel.kernelbase import Kernel
from klongpy import KlongInterpreter


class KlongPyKernel(Kernel):
    implementation = 'KlongPyKernel'
    implementation_version = '0.1'
    language = 'Klong'
    language_version = '0.1'
    language_info = {'name': 'Klong', 'mimetype': 'text/plain', 'file_extension': '.kg'}
    banner = "KlongPy - Vectorized port of Klong array language" 
    klong = KlongInterpreter()

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        try:
            output = str(self.klong(code))
        except Exception as e:
            print(e)
            output = "<error>"

        if not silent:
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok', 'execution_count': self.execution_count, 'payload': [], 'user_expressions': {}}


