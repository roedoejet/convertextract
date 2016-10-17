import glob
import os
from setuptools import setup

import convertextract

# get all of the scripts
scripts = glob.glob("bin/*")


long_description = 'Extract and find/replace text based on arbitrary correspondences while preserving original file formatting. This library is a fork from the Textract library by Dean Malmgren.'

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
    description="Extract and find/replace text based on arbitrary correspondences while preserving original file formatting.",
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