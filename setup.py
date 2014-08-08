from setuptools import setup

setup(
    name='twiggy-goodies',
    version='0.4.0',
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
        'anyjson',
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
    ],
    keywords='logging'
)
