from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re
import json




def extract_pdf_data(pdf_file):
   
    with open(pdf_file, 'rb') as file:
        resource_manager = PDFResourceManager()
        string_io = StringIO()
        pdf_interpreter = PDFPageInterpreter(resource_manager, TextConverter(resource_manager, string_io, laparams=LAParams()))

    
        for page in PDFPage.get_pages(file):
            pdf_interpreter.process_page(page)
        pdf_text = string_io.getvalue()
        
    college_data = re.findall(r'(\d+)\s+(\w+\s+\w+)\s+(\d+)', pdf_text)
  
  
   
    return pdf_text
def  mainlogichere(self):
    pass

pdf_file = '/Users/simrandeepsingh/python_project_Parser/NIRF_BTECH_PDF_1.pdf'
college_data = extract_pdf_data(pdf_file)

print(college_data)
