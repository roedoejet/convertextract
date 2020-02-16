* Version 3.0.0
  * Uses udpated external g2p library for conversions
  * Breaking change: both an *input_language* and and *output_language* now have to be specified instead of just *table* as in the previous API. In the command line, this is done with the `-il` and `-ol` arguments respectively. 
  * Breaking change: The argument *language* `-l` has now been deprecated and if using a custom mapping file (csv, tsv, psv, json, or xlsx) you must write your rules in the style used by `g2p` and provide the path with the *mapping* `-m` argument.

* Version 2.5.0
  * Uses external g2p library for transductions
  * Breaking change: **from** is now labelled **in**, **to** is now labelled **out**, **after** is now labelled **context_after** and **before** is now labelled **context_before**
  * Breaking change: custom tables can still be passed as a path with the `-l` flag, but all default languages are now from the g2p library and must be called with the language `-l` flag and an ISO code and the table `-t` flag and the name of the lookup table. Type `convertextract -h` for a list of available languages.
  
* Version 2.0.1
  * Added ability to take csv or plain list as cors
  * Fixed some problems with regex. Before columns are processed as positive lookbehinds, after columns are processed as positive lookaheads

* Version 2.0
  * Migrated to Python 3
  * Added processText method for processing of plain text
  * Added --no-write argument

* Version 1.6
  * Added support for feeding edge case https://medium.com/digital-linguistics/transliteration-in-javascript-99d306996752
  * Note: this solution will cause problems for documents that contain characters in the geometric shapes code block: Hex 25A0-25FF.

* Version 1.5.1
  * Fixed typo from Duolos to Doulos

* Version 1.5
  * Added Regex support for .txt, .docx, .pptx and .xlsx conversions
  * Breaking change: correspondence charts must now be ordered with the character to convert **from** in **column A** and the character to convert **to** in **column B**

* Version 1.3
  * Fixed an issue with pptx not preserving underlines.
  * Updated URL in warning messages
  * Fixed package includes for default correspondences

* Version 1.2.2
  * Fixed a typo for xlsx parser
  
* Version 1.2.1
  * Fixed a typo in PyPi submitted version 1.2
  
* Version 1.2
  * Fixed a silly issue causing pptx conversions to take far too long, they are faster now.
  * Revised docx conversions to allow for pictures to be preserved
 
* Version 1.1
  * Fixed txt_parser error with new line breaks. First release of stable version.
  
* Version 1.0.8 & 1.0.9
  * Fixed correspondence path for server deployment

* Version 1.0.7
  * Fixed script kwargs issue 

* Version 1.0.6
  * Added -p argument for .xlsx files

* Version 1.0.5
  * Fixed shebang issue

* Version 1.0.4
  * Supports .docx, .pptx, .txt, .xlsx
  * Supports Heiltsuk Duolos, Heiltsuk Times, Ts'ilhqot'in Duolos
