from setuptools import setup, find_packages

setup(name='biomples_py_api',
      version='0.1',
      description='A biosample API library',
      author='Luca Cherubin',
      author_email='luca.cherubin@gmail.com',
      license='MIT',
      packages=find_packages(),
      requires=[
            'requests',
            'simplejson'
      ],
      zip_safe=False)