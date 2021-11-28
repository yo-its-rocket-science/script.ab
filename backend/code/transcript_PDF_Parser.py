import io
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


def pdf_to_text(path):
    with open(path, 'rb') as fp:
        rsrcmgr = PDFResourceManager()
        outfp = io.StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, outfp, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
    text = outfp.getvalue()
    return text

def transcript_clean(processed_transcript, course_IDs):
    
    proc_tp_lines = processed_transcript.splitlines()
    proc_tp_lines = [x for x in proc_tp_lines if x != '']
    
    course_tab = pd.DataFrame()
    for i in range(0,len(proc_tp_lines)):
        if proc_tp_lines[i] in course_IDs:
            temp_df = pd.DataFrame({'Course_ID':[proc_tp_lines[i]],
                                    'Course_Num':[proc_tp_lines[i+1]]})
            course_tab = pd.concat([course_tab, temp_df], axis=0)
        
    return course_tab

def transcript_parse(path, course_IDs):
    txt = pdf_to_text(path)
    clean_txt = transcript_clean(txt, course_IDs)
    return clean_txt


#example usage
#from transcript_PDF_Parser import *
#processed_transcript = transcript_parse('./Transcript_-_Sample_2.pdf', course_IDs=['CPSC', 'ACCT', 'ENGG'])
#processed_transcript.to_csv('processed_transcript.csv',index=False)
