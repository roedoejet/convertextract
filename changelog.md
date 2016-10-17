##### To create a release:
* bump the version number in convertextract.__init__.py
* update docs/changelog.md
* git push
* python setup.py sdist
* python setup.py bdist_wheel
* twine upload dist/*

* Version 1.0.4
  * Supports .docx, .pptx, .txt, .xlsx
  * Supports Heiltsuk Duolos, Heiltsuk Times, Ts'ilhqot'in Duolos
