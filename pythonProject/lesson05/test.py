import json

if __name__ == '__main__':
    with open("info.json", "r") as read_file:
        data_dict = json.load(read_file)

    print("hobbies: ", data_dict["hobbies"])
    print("quantity of hobbies: ", len(data_dict["hobbies"]))

    print("quantity of children: ", len(data_dict["children"]))

    eldest_child_name = ''
    max_age = 0
    for child in data_dict["children"]:
        if child["age"] > max_age:
            max_age = child["age"]
            eldest_child_name = child["firstName"]

    print("eldest child name: ", eldest_child_name)

    data_dict["email"] = "jane@company.com"
    data_dict["phone"] = "123456"

    with open("info2.json", "w") as write_file:
        json.dump(data_dict, write_file)