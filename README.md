# convertextract
========

[![Build Status](https://travis-ci.org/roedoejet/textract.svg?branch=master)](https://travis-ci.org/roedoejet/textract)
[![Version](https://img.shields.io/pypi/v/convertextract.svg)](https://warehouse.python.org/project/convertextract/)
[![Coverage Status](https://coveralls.io/repos/github/roedoejet/textract/badge.svg?branch=master)](https://coveralls.io/github/roedoejet/textract?branch=master)


Extract and find/replace text based on arbitrary correspondences. This library is a fork from the Textract library by Dean Malmgren. https://github.com/deanmalmgren/textract

# Documentation

## Installation
To install, you must have Python 3.4+ and pip installed.
```{r, engine='python', count_lines}
pip install convertextract
```
Some source libraries need to be installed for different operating systems to support various file formats. Visit <http://textract.readthedocs.org/en/latest/installation.html> for documentation.

=========

## Basic CLI Use

Some basic Textract functions are preserved. Please visit <http://textract.readthedocs.org> for documentation.

#### Converting a file based on xlsx
convertextract requires two arguments:

1. A file containing text to convert (as of Version 1.0.4, this includes **.pptx**, **.docx**, **.xlsx**, and **.txt**)
2. An **.xlsx** file containing the find/replace correspondences. As of Version 2.0.1 you can also use either **.csv** files or feed a list of correspondences (as Python dicts) directly into the language keyword argument for either `process` or `process_text`

Running the comand:
```{r, engine='python', count_lines}
convertextract path/to/foo.docx -l path/to/bar.xlsx
```
Will produce a new file `path/to/foo_converted.docx` which will contain the same content as `path/to/foo.docx` but with find/replace performed for all correspondences listed in `path/to/bar.xlsx`.

#### Creating an .xlsx correspondence sheet
Your correspondence sheet must be set up as follows:

|    in   |  out           |
|:-:|:-:|
| aa| å| 
| oe| ø|
| ae| æ|

Here, this correspondence sheet (do not include headers like "replace with" or "find") would replace all instances of aa, oe, or ae in a given file with å, ø, or æ respectively.

#### Supported conversions

As of Version 2.0, the following conversions are supported:

* Heiltsuk Doulos Font -> Unicode
```{r, engine='python', count_lines}
convertextract path/to/foo.docx -l hei -t Doulos
```

* Heiltsuk Times Font -> Unicode
```{r, engine='python', count_lines}
convertextract path/to/foo.docx -l hei -t Times
```

* Tsilhqot'in Doulos Font -> Unicode
```{r, engine='python', count_lines}
convertextract path/to/foo.docx -l clc -t Doulos
```

* Navajo Times Font -> Unicode
```{r, engine='python', count_lines}
convertextract path/to/foo.docx -l nav -t Times
```

#### Using Regular Expressions

As of Version 1.5, there is support for Regular Expressions. If you do not need to use context-sensitive conversions, you do not need to include them. However, if you do, you should set up your correspondence sheet as follows:

|    in   |  out  |  context_before | context_after |
|:-:|:-:|:-:|:-:|
| aa| å|[k,d]|$| 
| aa| æ|t|$|
| aa| a:|||

For more information on how the g2p is acutally processed, please visit <https://github.com/roedoejet/g2p>.

#### Use as Python package
You can use the package in a Python script, which returns converted text, but without formatting. Running the script will still create a `foo_converted.docx` file.
```python
import convertextract
text = convertextract.process('foo.docx', language='bar.xlsx')
```

You can also use convertextract to just convert text in Python using `process_text`.

```python
import convertextract
text = convertextract.process_text('test', language=[{'in': 't', 'out': 'p', 'context_before': '^', 'context_after': 'e'}])
```
