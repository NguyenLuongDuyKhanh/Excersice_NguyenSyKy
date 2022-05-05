from external_file_reading import table1, table2

#print(table1)
#print(table2)

vietnamese_customer = 0
chinese_customer = 0
vietnamese_customer_info = []
chinese_customer_info = []

for i in table1:
    #print(i["phone"].split(")")[0].replace("(", ""))
    country_code = i["phone"].split(")")[0].replace("(", "")
    if int(country_code) == table2["VietNam"]:
        vietnamese_customer += 1
        vietnamese_customer_info.append(i)
    elif int(country_code) == table2["China"]:
        chinese_customer += 1
        chinese_customer_info.append(i)


#print(vietnamese_customer)
#print(chinese_customer)
#print(vietnamese_customer_info)
#print(chinese_customer_info)

all_domain = {
    "yahoo"   : 0,
    "gmail"   : 0,
    "outlook" : 0,
    "github"  : 0
}


for i in table1:
    #print(type(i["email"]))
    #print(i["email"].split(","))
    for email in i["email"].split(","):
        #print(email)
        #print(email.split("@")[0])
        #username = email.split("@")[0]
        #print(email.split("@")[1])
        domain = str(email.split("@")[1]).replace(".com", "")
        #print(domain)
        if domain in all_domain.keys():
            all_domain[domain] += 1
        elif domain not in all_domain.keys():
            all_domain[domain] = 1

#print(all_domain.keys())
#print(all_domain["yahoo"])
#print(all_domain.values())

most_domain = max(all_domain, key = all_domain.get)
#print(most_domain)


#print(chinese_customer_info)

chinese_customer_email_count = 0
email_list = []
for i in chinese_customer_info:
    #print(i["email"])
    for email in i["email"].split(","):
        #print(email)
        email_list.append(email)
        chinese_customer_email_count = len(email_list)

#print(chinese_customer_email_count)


"""
    1. How many customers come from VietNam
    2. Print information of customer who comes from China
    3. Which is the most popular mailing service
    4. How many customers' emails in China
"""
#print(vietnamese_customer)
#print(chinese_customer_info)
#print(most_domain)
#print(chinese_customer_email_count)

results = {
    "Vietnamese Customer" : vietnamese_customer,
    "Most domain" : most_domain,
    "Chinese customer email count" : chinese_customer_email_count
}

#print(results)

#solution_dir = 'D:\Learning\Python\Excercise\solution'

import json, yaml, csv

#result_json = json.dumps(results)
#print(result_json)

with open("External_File\solution\json_file.json", "w") as f:
    json.dump(results, f)

with open("External_File\solution\json_file.yaml", "w") as f:
    yaml.dump(results, f)

header = ["Vietnamese Customer", "Most domain", "Chinese customer email count"]
results_value = results.values()

with open("External_File\solution\json_file.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(results_value)
