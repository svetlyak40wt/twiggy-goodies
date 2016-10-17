from setuptools import setup

setup(
    name='twiggy-goodies',
    version='0.11.1',
    description='Handlers and helpers for Twiggy logging library.',
    author='Alexander Artemenko',
    author_email='svetlyak.40wt@gmail.com',
    url='https://github.com/svetlyak40wt/twiggy-goodies',
    packages=[
        'twiggy_goodies',
    ],
    install_requires=[
        'twiggy<0.5.0',
        'pytz',
        'six',
    ],
    license='BSD',
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='logging'
)
