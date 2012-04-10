from setuptools import setup, find_packages
import re

setup(
    name = "tornadotest",
    version = "0.0.1",
    description = "",
    author = "",
    author_email = "",
    url = "",
    package_dir = { '' : 'src' },
    packages = find_packages('src'),
    include_package_data = True,
    install_requires = [
        'tornado>=2.2',
    ],
    entry_points = {
        'console_scripts' : [
            'test=tornadotest:start_service',
         ]
    }
)
