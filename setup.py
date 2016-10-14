import glob
import os
from setuptools import setup

import convertextract

# get all of the scripts
scripts = glob.glob("bin/*")

# read in the description from README
with open("README.rst") as stream:
    long_description = stream.read()

github_url='https://github.com/roedoejet/convertextract'

# read in the dependencies from the virtualenv requirements file
dependencies, dependency_links = [], []
filename = os.path.join("requirements", "python")
with open(filename, 'r') as stream:
    for line in stream:
        line = line.strip()
        if line.startswith("http"):
            dependency_links.append(line)
        else:
            package = line.split('#')[0]
            if package:
                dependencies.append(package)


setup(
    name=convertextract.NAME,
    version=convertextract.VERSION,
    description="Extract and convert non-Unicode text into Unicode. Based on Textract library by Dean Malmgren",
    long_description=long_description,
    url=github_url,
    download_url="%s/archives/master" % github_url,
    author='Aidan Pine',
    author_email='aidanpine@shaw.ca',
    license='MIT',
    scripts=scripts,
    include_package_data=True,
    packages=[
        'convertextract',
        'convertextract.parsers',
        'convertextract.cors'
    ],
    install_requires=dependencies,
    dependency_links=dependency_links,
    zip_safe=False,
)