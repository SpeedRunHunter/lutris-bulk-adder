from setuptools import setup

with open('README.md') as file:
    long_description = file.read()
    
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3',
    'Topic :: Games/Entertainment',
    'Topic :: Utilities'
]

setup(
    name = 'lutris-bulk-adder-srh',
    packages = ['lutris_bulk_adder'],
    version = '0.1.0',
    license='MIT',
    description = 'Python script to bulk import a directory of ROM files into Lutris',
    long_description = long_description,
    author = 'SpeedRunHunter',
    author_email = 'marcell2003.sm@gmail.com',
    url = 'https://github.com/SpeedRunHunter/lutris-bulk-adder',
    keywords = ['Lutris', 'ROMs', 'Emulation'],
    entry_points = {'console_scripts': ['lutris_bulk_adder=lutris_bulk_adder.lutris_bulk_adder:main']},
    install_requires = [
        'PyYAML'
    ],
    classifiers=CLASSIFIERS
)
