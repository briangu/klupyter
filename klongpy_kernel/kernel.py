import sys
from io import StringIO
from ipykernel.kernelbase import Kernel

class KlongPyKernel(Kernel):
    implementation = 'KlongPyKernel'
    implementation_version = '0.1'
    language = 'Klong'
    language_version = '0.1'
    language_info = {'name': 'Klong', 'mimetype': 'text/plain', 'file_extension': '.kg'}
    banner = "KlongPy - Vectorized port of Klong array language" 

    def eval_expr(self, expr):
        try:
            print(expr)
            result = eval(expr)
            return str(result)
        except Exception as e:
            return str(e)

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):
        print(code)
        output = self.eval_expr(code.strip())

        if not silent:
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok', 'execution_count': self.execution_count, 'payload': [], 'user_expressions': {}}


