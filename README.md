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

|    from   |  to           |
|:-:|:-:|
| aa| å| 
| oe| ø|
| ae| æ|

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

#### Using Regular Expressions

As of Version 1.5, there is support for Regular Expressions. If you do not need to use context-sensitive conversions, you do not need to include them. However, if you do, you should set up your correspondence sheet as follows:

|    from   |  to  |  before | after |
|:-:|:-:|:-:|:-:|
| aa| å|[k,d]|$| 
| aa| æ|t|$|
| aa| a:|||

Context-sensitive conversions (conversions using Regular Expressions) will be performed first, in the order they are declared in your correspondence sheet. Then, context-free substitutions will be performed. In the above example: 

`kaa -> kå`
`taa -> tæ`
`kaat -> ka:t`

Please note that some regular expressions will not work well with Microsoft Office documents. For example white spaces `\s` are not reliable because MS Office documents commonly split text runs on whitespaces. It is recommended that if you are using regular expressions to be vigilant in checking your data that the proper conversions were performed. 

#### Use as Python package
You can use the package in a Python script, which returns converted text, but without formatting. Running the script will still create a `foo_converted.docx` file.
```python
import convertextract
text = convertextract.process('foo.docx', language='bar.xlsx')
```
