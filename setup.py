from setuptools import setup, find_packages

setup(
    name='SERPOutreacher',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'requests',
        'lxml',
        'cchardet',
        'beautifulsoup4',
        'selenium',
        'chromedriver-py',
        'pyvirtualdisplay'
    ],
    entry_points={
        'console_scripts': [
            'serpo = SERPOutreacher.cli_tool:main',
        ],
    },
)