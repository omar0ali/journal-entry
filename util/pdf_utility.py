from fpdf import FPDF
import os

class PdfUtility():
    pdf: FPDF
    
    _widthOfEachCell: list = []    
    def __init__(self) -> None:
        self.pdf = FPDF()
        self.pdf.set_margins(3, 10, 3)
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=10)
        self.pdf.set_fill_color(200, 220, 255)
    
    
    def addRowTable(self, array:list):
        for index, item in enumerate(array):
            self.pdf.cell(self._widthOfEachCell[index], 10, item, 1)
    
    def addTextCenter(self, txt:str):
        self.pdf.cell(0, 10,txt,ln=True ,align='C')
    
    def addTextCenterArray(self, array:list):
        for item in array:
            self.pdf.cell(0, 10, item, ln=True, align='C')
    
    
    def styleLine(self):
        self.pdf.line(10, self.pdf.get_y(), 190, self.pdf.get_y())  # Horizontal line
    def emptyNewLine(self, v: int = None):
        if(v==None):
            self.pdf.ln()
            return
        self.pdf.ln(v)
    def createTable(self, array: list, registerRows):
        # Header
        self._widthOfEachCell = []
        for a in array:
            width:float = (len(a)+2) * 2
            self._widthOfEachCell.append(width)
            self.pdf.cell(width, 10, a,align="L", border=1)
        self.pdf.ln()
        registerRows()
        