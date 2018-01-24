from setuptools import setup

setup(
    name='hellodeploy',    # This is the name of your PyPI-package.
    version='1.0',           # Update the version number for new releases
    entry_points = {
        "console_scripts": ['hellodeploy = hellodeploy']
    },
    url='https://github.com/quantfive/hellodeploy-cli',
    author='Itai Reuveni',
    author_email='itaireuveni@gmail.com',
    license='MIT',
    packages=['hellodeploy'],
    zip_safe=False
)