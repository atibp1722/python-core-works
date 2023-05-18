student={
    "id":1,
    "name":"Ram Karki",
    "subject":"python"
}
print(student["id"])
print(student.get("subject"))
student["subject"]="java script"
print(student)
print("")
print(student.values())
print(student.keys())
print(student.items())
print(student.pop("id"))
print(student.popitem())
# print(student.setdefault("name"))