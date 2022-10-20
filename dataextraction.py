from cgi import print_form
import PyPDF2
import re

# Assign file
file_name ="660557.pdf"
doc =PyPDF2.PdfFileReader(file_name)
# print(type(doc))

#pages of number
pages = doc.getNumPages()
# print(pages)


#search term

search = 'VALIDATION'

#list of tuples(all occurences,page number )
list_pages  = []
for i in range(pages):
    current_page = doc.getPage(i)
    text = current_page.extractText()
    if re.findall(search,text):
        count_page = len(re.findall(search,text))
        list_pages.append((count_page,i))
#result

print(list_pages)