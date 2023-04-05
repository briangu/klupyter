import sys
from io import StringIO
from ipykernel.kernelbase import Kernel

class KlongpyKernel(Kernel):
    implementation = 'ArithmeticKernel'
    implementation_version = '0.1'
    language = 'arithmetic'
    language_version = '0.1'
    language_info = {'name': 'arithmetic', 'mimetype': 'text/plain', 'file_extension': '.arith'}
    banner = "Arithmetic Kernel - A simple kernel that evaluates arithmetic expressions"

    def eval_expr(self, expr):
        try:
            result = eval(expr)
            return str(result)
        except Exception as e:
            return str(e)

    def do_execute(self, code, silent):
        output = self.eval_expr(code.strip())

        if not silent:
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok', 'execution_count': self.execution_count, 'payload': [], 'user_expressions': {}}


