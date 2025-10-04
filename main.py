from docx import Document
from docx.shared import Pt
from pydbml import PyDBML

db = PyDBML.parse_file('database.dbml')
tables = db.tables

doc = Document()

for table in tables:
    table_doc = doc.add_table(rows=1, cols=4)
    table_doc.style = 'Table Grid'
    table_doc.borders = True
    
    
    
    hdr_cells = table_doc.rows[0].cells
    hdr_cells[0].text = "Tabel naam"
    hdr_cells[0].merge(hdr_cells[3])
    
    hdr_cells = table_doc.add_row().cells
    hdr_cells[0].text = f"Table: {table.name}"
    hdr_cells[0].merge(hdr_cells[3])

    hdr_cells = table_doc.add_row().cells
    hdr_cells[0].text = "naam"
    hdr_cells[1].text = "Type"
    hdr_cells[2].text = "Nullable"
    hdr_cells[3].text = "Opmwerking"
    
    for column in table.columns:
        hdr_cells = table_doc.add_row().cells
        hdr_cells[0].text = f"{column.name}"
        hdr_cells[1].text = f"{column.type}"
        hdr_cells[2].text = { True: "NOT NULL", False: "NULL" }[column.not_null]
        hdr_cells[3].text = f"PK" if column.pk else ""
        
    doc.add_paragraph("\n")



doc.save('specificatie.docx')