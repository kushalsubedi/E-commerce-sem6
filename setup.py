
def main():
    from setuptools import setup, find_packages
    setup(
        name='Merch-Store',
        version='0.1.0',
        description='A Python Django based web application for E-commerce',
        author='Kushal Subedi',

        packages=find_packages(),
        include_package_data=True,
        install_requires=[
            find_packages('requirements.txt'),
        ],
        entry_points={
            'console_scripts': [
                'Merch-Store=Merch-Store.__main__:main',
            ],
        },
    )