from setuptools import setup, find_packages

setup(
  name = "prediction",
  version = "1.0",
  description = 'prediction of stock price or forex price',
  author = 'Nagi',
  author_email = 'komoootv@gmail.com',
  license = "MIT,"
  packages=find_packages(['forex-prediction']),
  # packages = ['forex-prediction']
  install_requires = ['tensorflow', 'einops', 'yfinance', 'MetaTrader5', 'numpy', 'pandas', 'sklearn']
)
