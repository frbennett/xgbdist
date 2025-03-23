from setuptools import setup, find_packages

setup(
   name='xgboost_distribution',
   version='0.2',
   description='Python implementation RS-HDMR',
   keywords='sobol sensitivity analysis',
   author='Frederick Bennett',
   author_email='frederick.bennett@des.qld.gov.au',
   packages=find_packages(),  #same as name
   install_requires=[
            'xgboost>=3.0.0',
            'scikit-learn' 
    ]
)