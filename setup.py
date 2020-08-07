import glob
import os
import sys
from setuptools import setup

import convertextract

# get all of the scripts
scripts = glob.glob("bin/*")

# read in the description from README
with open("README.md") as stream:
    long_description = stream.read()

github_url = 'https://github.com/roedoejet/convertextract'


def parse_requirements(requirements_filename):
    """read in the dependencies from the requirements files
    """
    dependencies, dependency_links = [], []
    requirements_dir = os.path.dirname(requirements_filename)
    with open(requirements_filename, 'r') as stream:
        for line in stream:
            line = line.strip()
            if line.startswith("-r"):
                filename = os.path.join(requirements_dir, line[2:].strip())
                _dependencies, _dependency_links = parse_requirements(filename)
                dependencies.extend(_dependencies)
                dependency_links.extend(_dependency_links)
            elif line.startswith("http"):
                dependency_links.append(line)
            else:
                package = line.split('#')[0]
                if package:
                    dependencies.append(package)
    return dependencies, dependency_links


requirements_filename = "requirements.txt"
dependencies, dependency_links = parse_requirements(requirements_filename)

setup(
    name=convertextract.__name__,
    version=convertextract.VERSION,
    python_requires='>3.4',
    description="Arbitrary transliterations on Microsoft Office documents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=github_url,
    download_url="%s/archives/master" % github_url,
    author='Aidan Pine',
    author_email='info@mothertongues.org',
    license='MIT',
    scripts=scripts,
    include_package_data=True,
    packages=[
        'convertextract',
        'convertextract.parsers'
    ],
    install_requires=dependencies,
    dependency_links=dependency_links,
    zip_safe=False,
)
