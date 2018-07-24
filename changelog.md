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
