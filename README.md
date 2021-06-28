<h1 align="center">AirBnB clone - The console 💻</h1> <br>

![HBNB](https://raw.githubusercontent.com/anamariaroman/AirBnB_clone/master/images/hbnb.png)

## A description fot this project
For having an interactive console its important:
* Put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
* Create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* Create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* Create the first abstracted storage engine of the project: File storage.
* Create all unittests to validate all our classes and storage engine

<h3>Interactive mode</h3> <br>

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
<h3>Non-interactive mode: (like the Shell project in C)</h3> <br>

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

<h2 align="center">Authors 👩👩👩</h2> <br>

- Ana María Román Valencia | [Github](https://github.com/anamariaroman) | [Twiter](https://twitter.com/AnaMari77939013)
- Helena Cortés Gómez | [Github](https://github.com/helectron) | [Twiter](https://twitter.com/helectron)
- Luz Adriana Baza | [Github](https://) | [Twiter](https://twitter.com/baza_luz)

<div dir="rtl">27/06/2021</div>
