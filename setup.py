from setuptools import setup, find_packages

VERSION = '0.0.5' 
DESCRIPTION = 'Extract PDF text in reading order.'
LONG_DESCRIPTION = 'Extract PDF text in reading order! Formats supported are .txt and .md. Multiple column PDFs supported.'

setup(
        name="autoPDF", 
        version=VERSION,
        author="Gustavo L. Matos",
        author_email="matosgustavo@statmatos.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['pandas', 'numpy', 'pdfminer', 'sklearn'], 
        
        keywords=['python', 'PDF', 'extract'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
        ]
)