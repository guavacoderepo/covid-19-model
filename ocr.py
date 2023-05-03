import os
import fitz
import pandas as pd


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
data_dir = os.path.join(cwd, "data")
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
Key1 = "machine learning"
Key11 = "machine"
Key2 = "scale-free"
Key22 = "scale free"
Key3 = "power-law"
Key33 = "power law"
Key4 = "complex network"
Key5 = "modeling"
Key6 = "epidemic"
Key7 = "economic outcomes"
Key77 = "economic"
Key8 = "china"
key9 = "covid"
key10 = "government"
Key11 = "economic policy"


# variable declaratio
documents = []
machine = []
scale_free = []
power_law = []
complex_network = []
modeling = []
epidemic = []
economic = []
china = []
covid = []
government = []
policy = []
index = []

# document id
id = 0

file = open('myfile.txt', 'w')

# read text from documents and write to text
for docx in doc_array:
    Key1_count = 0
    Key2_count = 0
    Key3_count = 0
    Key4_count = 0
    Key5_count = 0
    Key6_count = 0
    Key7_count = 0
    Key8_count = 0
    Key9_count = 0
    Key10_count = 0
    Key11_count = 0


# Read text from file
    doc = fitz.open(docx)

# Extract text from document

    for page in doc:
        text = page.get_text().lower()

        # print(text)

    # keyword context search
        if Key1 in text or Key11 in text:
            Key1_count = Key1_count + text.count(Key1)
        if Key2 in text or Key22 in text:
            Key2_count = Key2_count + text.count(Key2)
        if Key3 in text or Key33 in text:
            Key3_count = Key3_count + text.count(Key3)
        if Key4 in text:
            Key4_count = Key4_count + text.count(Key4)
        if Key5 in text:
            Key5_count = Key5_count + text.count(Key5)
        if Key6 in text:
            Key6_count = Key6_count + text.count(Key6)
        if Key7 in text or Key77 in text:
            Key7_count = Key7_count + text.count(Key7)
        if Key8 in text:
            Key8_count = Key8_count + text.count(Key8)
        if key9 in text:
            Key9_count = Key9_count + text.count(key9)
        if key10 in text:
            Key10_count = Key10_count + text.count(key10)
        if Key11 in text:
            Key11_count = Key11_count + text.count(Key11)


# CREATE A CSV FILE FOR OUR MODEL

    # print(os.path.basename(docx).split('/')[-1])xw
    # create index for document

    documents.append(os.path.basename(docx).split('/')[-1])
    index.append(id)
    machine.append(int(Key1_count))
    scale_free.append(int(Key2_count))
    power_law.append(int(Key3_count))
    complex_network.append(int(Key4_count))
    modeling.append(int(Key5_count))
    epidemic.append(int(Key6_count))
    economic.append(int(Key7_count))
    china.append(int(Key8_count))
    covid.append(int(Key9_count))
    government.append(int(Key10_count))
    policy.append(int(Key11_count))

    id += 1
print(china)


dataset = {
    "document": documents,
    "doc_index": index,
    Key1: machine,
    Key2: scale_free,
    Key3: power_law,
    Key4: complex_network,
    Key5: modeling,
    Key6: epidemic,
    Key7: economic,
    Key8: china,
    key9: covid,
    key10: government,
    Key11: policy
}
df = pd.DataFrame(dataset)
df.to_csv("dataset.csv")

print(dataset)

file.close()
print("done")
# print(text)
