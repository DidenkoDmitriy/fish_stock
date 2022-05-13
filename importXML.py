import pandas as pd
from docx import Document
import initial_variables as init_var
from docx.shared import Inches


tmp_DF = pd.DataFrame({
    'age': [0, 1, 2, 3, 4],
    'count': [15, 19, 23, 22, 10]
     })
el_watrer_body = 'р. Хор'
var_sample_size = 19
print(str(el_watrer_body) + ' ' + str(init_var.current_cur_year))
print(tmp_DF)

document = Document()

table = document.add_table(rows=1, cols=len(tmp_DF['age'])+3, style='Table Grid')
hdr_cells = table.rows[0].cells
hdr_cells[0].text = 'Год'
hdr_cells[1].text = 'Место лова'
for col_number in range(len(tmp_DF['age'])):
    hdr_cells[col_number + 2].text = str(list(tmp_DF['age'])[col_number])
hdr_cells[len(tmp_DF['age'])+2].text = 'Экз.'


row_cells = table.add_row().cells
row_cells[0].text = '2021'
row_cells[1].text = el_watrer_body
for col_number in range(len(tmp_DF['age'])):
    row_cells[col_number + 2].text = str(list(tmp_DF['count'])[col_number])
row_cells[len(tmp_DF['age'])+2].text = str(var_sample_size)
document.add_page_break()
#
document.save('demo.docx')
