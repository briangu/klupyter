from setuptools import setup

setup(name='klongpy_kernel',
      version='0.1',
      description='A KlongPy kernel for Jupyter',
      author='Brian Guarraci',
      author_email='brian@ops5.com',
      license='MIT',
      packages=['klongpy_kernel'],
      install_requires=['ipykernel'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Framework :: IPython',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
      ],
      zip_safe=False)

