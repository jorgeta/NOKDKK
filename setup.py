from setuptools import setup, find_packages

setup(
    name='nokdkk',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'nokdkk=scripts.app:main'
        ]
    }
)