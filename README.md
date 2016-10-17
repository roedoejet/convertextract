# convertextract
========

Extract and find/replace text based on arbitrary correspondences. This library is a fork from the Textract library by Dean Malmgren. https://github.com/deanmalmgren/textract

# Documentation

## Installation
To install, you must have Python 2.7 and pip installed.
```{r, engine='python', count_lines}
pip install convertextract
```
Some source libraries need to be installed for different operating systems to support various file formats. Visit <http://textract.readthedocs.org/en/latest/installation.html> for documentation.

=========

## Basic CLI Use

Basic Textract functions are preserved. Please visit <http://textract.readthedocs.org> for documentation.

#### Converting a file based on xlsx
convertextract requires two arguments:
1. A file containing text to convert (as of Version 1.0.4, this includes **.pptx**, **.docx**, **.xlsx**, and **.txt**)
2. An **.xlsx** file containing the find/replace correspondences.

Running the comand:
```{r, engine='python', count_lines}
convertextract path/to/foo.docx -l path/to/bar.xlsx
```
Will produce a new file `path/to/foo_converted.docx` which will contain the same content as `path/to/foo.docx` but with find/replace performed for all correspondences listed in `path/to/bar.xlsx`.

#### Creating an .xlsx correspondence sheet
Your correspondence sheet must be set up as follows:

|    replace with    |  find           |
|:-:|:-:|
| å| aa|
| ø| oe|
| æ| ae|

Here, this correspondence sheet (do not include headers like "replace with" or "find") would replace all instances of aa, oe, or ae in a given file with å, ø, or æ respectively.

#### Supported conversions

As of Version 1.0.4, the following conversions are supported:

* Heiltsuk Duolos Font -> Unicode
```{r, engine='python', count_lines}
convertextract path/to/foo.docx -l heiltsuk_duolos
```

* Heiltsuk Times Font -> Unicode
```{r, engine='python', count_lines}
convertextract path/to/foo.docx -l heiltsuk_times
```

* Ts'ilhqot'in Duolos Font -> Unicode
```{r, engine='python', count_lines}
convertextract path/to/foo.docx -l tssilhqut-in_duolos
```

#### Use as Python package
You can use the package in a Python script, which returns converted text, but without formatting. Running the script will still create a `foo_converted.docx` file.
```python
import convertextract
text = convertextract.process('foo.docx', language='bar.xlsx')
```
