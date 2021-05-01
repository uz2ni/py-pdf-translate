import json
# 번역
from googletrans import Translator
# pdf 변환
from io import StringIO
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser

# function
def read_pdf_PDFMINER(pdf_file_path):
    output_string = StringIO()
    with open(pdf_file_path, 'rb') as f:
        parser = PDFParser(f)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams(), pageno=2)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

    return str(output_string.getvalue())

# 1. 코로나19 관련 한글 학술논물 pdf 다운 (로컬 or 웹에서 다운)
# 일단 로컬에서 진행..

# 2. pdf 가져와서 txt파일 변환 (웹? 로컬?)
text1 = read_pdf_PDFMINER('./korona19_01.pdf')

f = open('./saveTest.txt', 'w', -1, 'utf-8')
print(text1, file=f)
f.close()

#o = open('./saveTest.txt', 'r', -1, 'utf-8')

# 3. 일본어, 아랍어, 영어로 번역
translator = Translator()

print(translator.detect(text1))
#trans1 = translator.translate('아라아러낼ㅇ니', src='ko', dest='en')
#
# print("Korean to English >>>>>>>>>>>>>>>>>")
# print(trans1.text)

# 4. 하나의 텍스트 파일로 합병하여 저장

