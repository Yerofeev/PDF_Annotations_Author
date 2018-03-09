# PDF_Annotations_Author
Python3 tool to change 'Author' field of PDF-files.
For example, you have thousand of PDF files and want to change the author for some of them. It may be very useful, 
if you rely on Author to estimate importance of annotations, for example, '+' is less significant than '+++'. Especially 
this utility may be handy if you want to alter thousands of them.

Usage:
1. git clone https://github.com/Yerofeev/PDF_Annotations_Author.git
2. cd PDF_Annotations_Author
3. sudo apt-get install python3-poppler-qt5
3. python3 pdf_utils.py
4. Specify folder with PDFs
5. Enter the author of annotations you want to change, for example, 'i', to 'Important', or '+' to '!'.
6. PDFs with changed author in annotations were added in specified directory/PDF
