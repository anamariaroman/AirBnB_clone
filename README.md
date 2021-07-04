<h1 align="center">
  <br>
  <a href="https://github.com/anamariaroman/AirBnB_clone"><img src="https://raw.githubusercontent.com/anamariaroman/AirBnB_clone/master/images/hbnb.png" alt="AirBnB logo"></a>
  <br>AirBnB clone - The console 💻 <br>
</h1>

---

### 🐶 Description 💅

This is a Holberton school project which its main goal is to create and develop our knowledge towards building our first full web application, the AirBnB clone!

### Functionalities of this command interpreter📃

- Create a new object (For instance: a new user, place, city. review...)
- Retrieve an object from a file, a database in order to see its information.
- Update an object to add more records to that specific record or just change its information.
- Destroy a record in order to remove it from the database.

---

# 🦩 Environment 🦩

This project was interpreted and tested on Ubuntu 20.04 LTS using python3 (version 3.8.5) but you should be able to run it on any other version! 🙈

---

## ❤️ File descriptor 👩🏻‍🔬

| **File**          | **Brief description**                                                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AUTHORS`         | [AUTHORS](https://github.com/anamariaroman/AirBnB_clone/blob/master/AUTHORS "AUTHORS") - List that contents the contributors to this project                                                                    |
| `amenity.py`      | [amenity.py](https://github.com/anamariaroman/AirBnB_clone/blob/master/models/amenity.py "amenity.py]") - Class that inherites from Base Model.                                                                 |
| `base_model.py`   | [base_model.py](https://github.com/anamariaroman/AirBnB_clone/blob/master/models/base_model.py "base_model.py]") - Defines all common methods that other classes will inherit from                              |
| `city.py`         | [amenity.py](https://github.com/anamariaroman/AirBnB_clone/blob/master/models/city.py "city.py]") - Class that inherites from Base Model.                                                                       |
| `console.py`      | [console.py](https://github.com/anamariaroman/AirBnB_clone/blob/master/console.py "console.py]") - Contains the entry point of the command interpreter.                                                         |
| `file_storage.py` | [file_storage.py](https://github.com/anamariaroman/AirBnB_clone/blob/master/models/engine/file_storage.py "file_storage.py]") - Contains the File Storage class that handles serialization and deserialization. |
| `place.py`        | [place.py](https://github.com/anamariaroman/AirBnB_clone/blob/master/models/place.py "place.py]") - Class that inherites from Base Model.                                                                       |
| `review.py`       | [review.py](https://github.com/anamariaroman/AirBnB_clone/blob/master/models/review.py "review.py]") - Class that inherites from Base Model.                                                                    |
| `user.py`         | [user.py](https://github.com/anamariaroman/AirBnB_clone/blob/master/models/user.py "user.py]") - Class that inherites from Base Model.                                                                          |
|                   |

[👆🏼](https://github.com/anamariaroman/AirBnB_clone# "Back to the top") - [Back to the top](https://github.com/anamariaroman/AirBnB_clone# "Back to the top]") - Go back to the top. [👆🏼](https://github.com/anamariaroman/AirBnB_clone# "Back to the top")

---

# 🦋 Project overview 🦋

-This is an overview of how the project is going to evolve in the future! It's quite magnifique, isn't it!?

<a href="https://github.com/anamariaroman/AirBnB_clone"><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210704%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210704T151931Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f4f6b9016e4de9eed89ae902112ed60fa91c7f3479228145e7cdeb8f3f5a0ec8" alt="edit me please :("></a>

---

# 🛠 Installation 🛠

1.  Clone this repository in your personal computer or machine with the following command:
    `git clone https://github.com/anamariaroman/AirBnB_clone.git`

2.  Go to the project s folder using the following command:
    `cd AirBnB_clone`

3.  Run the console interactively:
    `./console.py`

4.  Run the console in non interactively mode
    `echo "<command>" | ./console.py`

# 🌻 Examples 🌼

## Interactive mode

<h6 align="center">Provided you followed all the installation steps properly;
you should be able to see the console prompt as shown bellow:</h6>

```bash
$ ./console.py
```

```bash
(hbnb)help
Documented commands (type help <topic>):

(hbnb) help all
Method for printing all the objects

(hbnb)help quit
Command to exit the program.

(hbnb) create
** class name missing **

(hbnb) create BaseModel
bb545f9b-906c-41ac-be58-1a5968d90a6b

(hbnb) show BaseModel bb545f9b-906c-41ac-be58-1a5968d90a6b
[BaseModel] (bb545f9b-906c-41ac-be58-1a5968d90a6b) {'id': 'bb545f9b-906c-41ac-be58-1a5968d90a6b', 'created_at': datetime.datetime(2021, 7, 4, 16, 43, 54, 653652), 'updated_at': datetime.datetime(2021, 7, 4, 16, 43, 54, 653836)}

(hbnb) create BaseModel
1dc4df28-f144-4a79-9c57-49527aa52492
(hbnb) update BaseModel 1dc4df28-f144-4a79-9c57-49527aa52492 first_name "Betty"
(hbnb) show BaseModel 1dc4df28-f144-4a79-9c57-49527aa52492
[BaseModel] (1dc4df28-f144-4a79-9c57-49527aa52492) {'id': '1dc4df28-f144-4a79-9c57-49527aa52492', 'created_at': datetime.datetime(2021, 7, 4, 10, 38, 46, 40367), 'updated_at': datetime.datetime(2021, 7, 4, 10, 38, 46, 40374), 'first_name': '"Betty"'}

```

[👆🏼](https://github.com/anamariaroman/AirBnB_clone# "Back to the top") - [Back to the top](https://github.com/anamariaroman/AirBnB_clone# "Back to the top]") - Go back to the top. [👆🏼](https://github.com/anamariaroman/AirBnB_clone# "Back to the top")

## Non-interactive mod

```bash
$ echo "command" | ./console.py
```

```bash
echo "help" | ./console.py

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

echo "help all" | ./console.py
(hbnb) Method for printing all the objects

echo "create BaseModel" | ./console.py
(hbnb) 3ffc6992-ce66-45da-b851-f6c12f764178

echo "show BaseModel 3ffc6992-ce66-45da-b851-f6c12f764178" | ./console.py
(hbnb) [BaseModel] (3ffc6992-ce66-45da-b851-f6c12f764178) {'id': '3ffc6992-ce66-45da-b851-f6c12f764178', 'created_at': datetime.datetime(2021, 7, 4, 16, 47, 36, 653899), 'updated_at': datetime.datetime(2021, 7, 4, 16, 47, 36, 654149)}

echo "show BaseModel bb545f9b-906c-41ac-be58-1a5968d90a6b" | ./console.py
(hbnb) [BaseModel] (bb545f9b-906c-41ac-be58-1a5968d90a6b) {'id': 'bb545f9b-906c-41ac-be58-1a5968d90a6b', 'created_at': datetime.datetime(2021, 7, 4, 16, 43, 54, 653652), 'updated_at': datetime.datetime(2021, 7, 4, 16, 43, 54, 653836), 'projects_team': 'Ana Maria Roman, Helena Cortes, Luz Baza'}
```

---

# ⚰️ Bugs 🐁
```
(hbnb) create BaseModel
ccacc907-488e-40d6-96bf-130c5e93c946
(hbnb) update BaseModel ccacc907-488e-40d6-96bf-130c5e93c946 "project_team": "Helena Cortes, Ana Roman, Luz Baza"
(hbnb) show BaseModel ccacc907-488e-40d6-96bf-130c5e93c946
[BaseModel] (ccacc907-488e-40d6-96bf-130c5e93c946) {'id': 'ccacc907-488e-40d6-96bf-130c5e93c946', 'created_at': datetime.datetime(2021, 7, 4, 10, 34, 27, 285043), 'updated_at': datetime.datetime(2021, 7, 4, 10, 34, 27, 285048), '"project_team":': '"Helena'}
(hbnb)
```

- Edit me if you have got a bug on your console 😭

---

# 👩 Authors 🏴‍☠️

- Ana María Román Valencia [Github](https://github.com/anamariaroman) | [Twiter](https://twitter.com/AnaMari77939013)
- Helena Cortés Gómez [Github](https://github.com/helectron) | [Twiter](https://twitter.com/helectron)
- Ana María Román Valencia [Github](https://github.com/luzbaza) | [Twiter](https://twitter.com/baza_luz)

---

[👆🏼](https://github.com/anamariaroman/AirBnB_clone# "Back to the top") - [Back to the top](https://github.com/anamariaroman/AirBnB_clone# "Back to the top]") - Go back to the top. [👆🏼](https://github.com/anamariaroman/AirBnB_clone# "Back to the top")

<h6 align="right">04/07/2021</h6>