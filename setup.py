from setuptools import setup, find_packages

setup(
    name='SERPOutreacher',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'serpo = SERPOutreacher.cli_tool:main',
        ],
    },
)