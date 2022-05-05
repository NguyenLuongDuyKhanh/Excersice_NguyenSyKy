import os

#print(os.getcwd())

table1 = []

dir_path = 'External_File\data'

element_dict = {}

for file in os.listdir(dir_path):
    if file.endswith(".txt"):
        file_path = f"{dir_path}\{file}"
        with open(file_path, "r") as f:
            for line in f:
                #print(str(line.splitlines()).split(":")[0].replace("['", ""))
                #print(str(line.splitlines()).split(":")[1].replace("']","").strip())
                element_dict[(str(line.splitlines()).split(":")[0]).replace("['", "")] = str(line.splitlines()).split(":")[1].replace("']","").strip()

            table1.append(element_dict)
            element_dict = {}

#print(table1)

table2 = {}
table2_path = 'External_File\data\\references'
with open(table2_path,"r") as f:
    for line in f:
        #print(str(line.splitlines()).split(":")[0].replace("['", "").replace("\"", ""))
        #print(str(line.splitlines()).split(":")[1].replace("']", "").replace(",", ""))
        table2[str(line.splitlines()).split(":")[0].replace("['", "").replace("\"", "")] = int(str(line.splitlines()).split(":")[1].replace("']", "").replace(",", ""))

#print(table2)