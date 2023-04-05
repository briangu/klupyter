if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    from .kernel import KlongpyKernel  # Assuming your kernel class is named KlongpyKernel in kernel.py
    IPKernelApp.launch_instance(kernel_class=KlongpyKernel)

