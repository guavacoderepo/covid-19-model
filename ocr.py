import os 
import fitz


# OPTICAL CHARACTER RECOGNITION FILE
# FILE FORMAT (FILE_NAME.PDF)
# Script written by evan and deployed to guavacode git repo
# Please this file is not a public file
# This code is segmented for clarity 

# GET FILES AND VERIFY FILR FORMATE SECTION

# create empty docment array
doc_array = []
# get current working dir
cwd = os.getcwd()
# set data model path
data_dir = os.path.join(cwd,"data")
# get all pdf files in folder
all_docx = os.listdir(data_dir)

# check for valid document extension (pdf)

for doc in all_docx:
    # get extension 
    exe = doc.split(".")[1]

    # insert document in a new array with extension name IF DOC IS PDF
    if exe == "pdf":
        doc_array.append(os.path.join(data_dir, doc))



# TEXT EXTRACTION SECTION

# variable declaratio
Keyword1 = "week"
Keyword2 = "its"
Keyword3 = "be"
Keyword4 = "keyword"
Keyword5 = "keyword"

Keyword1_count = 0
Keyword2_count = 0
Keyword3_count = 0
Keyword4_count = 0
Keyword5_count = 0

# Read text from file
doc = fitz.open('/Users/evan-mac/Python/covid-19 model/data/docx4.pdf')

# Extract text from document
for page in doc:
    text = page.get_text()

# keyword context search 
    if Keyword1 in text:
        Keyword1_count = Keyword1_count + text.count(Keyword1)
    if Keyword2 in text:
        Keyword2_count = Keyword2_count + text.count(Keyword2)
    if Keyword3 in text:
        Keyword3_count = Keyword3_count + text.count(Keyword3)
    if Keyword4 in text:
        Keyword4_count = Keyword4_count + text.count(Keyword4)
    if Keyword5 in text:
        Keyword5_count = Keyword5_count + text.count(Keyword5)

# CREATE A CSV FILE FOR OUR MODEL



# print(text)
