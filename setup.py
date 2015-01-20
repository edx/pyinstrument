from setuptools import setup, find_packages

setup(
    name="pyinstrument",
    packages=['pyinstrument'],
    version="0.13.1",
    description="A call stack profiler for Python. Inspired by Apple's Instruments.app",
    author='Joe Rickerby',
    author_email='joerick@mac.com',
    url='https://github.com/joerick/pyinstrument',
    keywords=['profiling', 'profile', 'profiler', 'cpu', 'time'],
    include_package_data=True,
    entry_points={'console_scripts': ['pyinstrument = pyinstrument.__main__:main', 'pyinstrument-combine = pyinstrument.__main__:combine']},
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Software Development :: Testing',
    ]
)
