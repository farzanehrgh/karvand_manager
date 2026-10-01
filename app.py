import json
import os

file_path = "data/karvands.json"

if os.path.exists(file_path):
    with open(file_path,"r",encoding="utf-8")as file:
        data = json.load(file)
else:
    data = {"karvands":[]}

while True:
        options =input("please select:\n1- add new karvand\n2-show karvand list\n3-edit info karvand\n4-delete karvand\n5-report\n6-exit")
        if options == "1":
             full_name = input("Enter full name: ").strip().lower()
             email = input("Enter email: ").strip().lower()
             city = input("Enter city: ").strip().lower()
             degree = input("Enter degree: ").strip().lower()
             field = input("Enter field: ").strip().lower()
             skills = input("Enter skills: ").strip().lower()

             new_karvand = {
                  "full_name":full_name,
                  "email":email,
                  "city":city,
                  "education":{
                       "degree":degree,
                       "field":field
                  },
                  "skills":[
                       {
                            "name":skills
                       }
                  ]

             }
        if "karvands" not in data:
             data["karvands"] = []
             data["karvands"].append(new_karvand)

             with open(file_path, "w") as file:
                  json.dump(data, file, ensure_ascii=False, indent=4)


        if options == "2":
              for karvand in data["karvands"]:
                   print(karvand)

        if options == "3":
             name = input("enter full name : ").strip().lower()
             for karvand in data["karvands"]:
                  if karvand["full_name"]==name:
                       new_email=input("edit- enter new_email: ").strip().lower()
                       karvand["email"]= new_email
                       with open(file_path, "w") as file:
                                         json.dump(data, file, ensure_ascii=False, indent=4)
                       
                               
