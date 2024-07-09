from setuptools import setup, find_packages

setup(
    name='fastapi_framework_core',
    version='0.1',
    packages=find_packages(),
    description='Descripción corta de tu paquete', 
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Marcos Alegrette',
    author_email='gamarcosalegrette@gmail.com',
    install_requires=[
        'fastapi',
        'uvicorn',  
        'sqlalchemy',  
        'pymysql'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  
        'Intended Audience :: Developers',        
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9', 
    ],
)
