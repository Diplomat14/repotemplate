from setuptools import setup, find_packages
import os

def readme():
    with open(os.path.dirname(os.path.abspath(__file__)) + '/README.rst') as f:
        return f.read()

setup(
    name='todo_package_name',
    version='0.1',
    description='<todo_package_short_description>',
    long_description=readme(),
    url='TBD',
    author='<todo_author_first_last_name>',
    author_email='<todo_author_email>',
    license='MIT', #TBD
    packages=find_packages(),
    install_requires=[
        # ' privaterepo @ git+http://git@github.com/Diplomat14/privatedependencyhere.git '
        # ' privaterepo @ git+ssh://git@github.com/Diplomat14/privatedependencyhere.git '
    ],
    #dependency_links=['http://server/user/repo/tarball/master#egg=package-1.0'],
    entry_points = {
        'console_scripts':['todo_package_name-main=todo_package_name.console.command_line:main']
    },
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)