list_of_members = [
            {
                "name": "Harry",
                "birthday": "23/11/2000",
                "intimacy point": 15,
            },
            {
                "name": "Linda",
                "birthday": "25/1/1995",
                "intimacy point": 30,
            },
            {
                "name": "Robert",
                "birthday": "5/1/1998",
                "intimacy point": 15,
            }
        ]

#...
#["Harry","Linda","Robert"]
name_list = []
for x in list_of_members:
    name_list.append(x["name"])

if "Harry" in name_list:
    print("Khach hang than thiet")