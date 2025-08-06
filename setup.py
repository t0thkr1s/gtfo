from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='gtfobins',
    version='1.0.0',
    url='https://github.com/t0thkr1s/gtfo',
    author='t0thkr1s',
    author_email='t0thkr1s@icloud.com',
    description='Command-line tool for GTFOBins - Unix binaries exploitation helper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='GPL-3.0',
    packages=find_packages(),
    package_data={
        'gtfo': ['data/*.json'],
    },
    include_package_data=True,
    install_requires=[
        'colorama>=0.4.0',
        'pygments>=2.0.0'
    ],
    entry_points={
        'console_scripts': [
            'gtfo=gtfo.cli:main',
        ],
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Security',
        'Topic :: System :: System Shells',
        'Topic :: Utilities',
    ],
    keywords='gtfobins security exploitation privilege-escalation pentesting',
)
