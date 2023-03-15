<h1><p align="center">Pretty Utils</p></h1>

<p align="center"><img src="images/icons/app.png" width="400"></p>



<h1><p align="center">Content</p></h1>

- [Short description](#Short-description)
- [Useful links](#Useful-links)
- [Installation](#Installation)
- [databases](#databases)
    - [mysql](#mysql)
      - [DB](#DB)
      - [execute](#execute)
    - [sqlalchemy_](#sqlalchemy_)
      - [DB](#DB-1)
      - [create_database](#create_database)
      - [create_tables](#create_tables)
      - [all](#all)
      - [one](#one)
      - [execute](#execute-1)
      - [commit](#commit)
      - [insert](#insert)
    - [sqlite](#sqlite)
      - [DB](#DB-2)
      - [execute](#execute-2)
      - [dynamic_class](#dynamic_class)
      - [make_sql](#make_sql)
- [miscellaneous](#miscellaneous)
    - [files](#files)
      - [join_path](#join_path)
      - [touch](#touch)
      - [write_json](#write_json)
      - [read_lines](#read_lines)
      - [read_json](#read_json)
      - [resource_path](#resource_path)
    - [generators](#generators)
      - [username](#username)
      - [password](#password)
    - [http](#http)
      - [aiohttp_params](#aiohttp_params)
    - [inputting](#inputting)
      - [timeout_input](#timeout_input)
    - [selenium_](#selenium_)
      - [Sel](#Sel)
      - [get_element](#get_element)
      - [get_text](#get_text)
      - [wait_for_clickability](#wait_for_clickability)
      - [clear](#clear)
      - [write](#write)
      - [click](#click)
      - [click_js](#click_js)
      - [click_when_clicable](#click_when_clicable)
      - [click_with_coord](#click_with_coord)
    - [time_and_date](#time_and_date)
      - [strtime_to_unix](#strtime_to_unix)
      - [unix_to_strtime](#unix_to_strtime)
- [type_functions](#type_functions)
  - [bools](#bools)
    - [randbool](#randbool)
  - [classes](#classes)
    - [AutoRepr](#AutoRepr)
    - [Singleton](#Singleton)
    - [SingletonThreading](#SingletonThreading)
    - [SingletonMultiprocessing](#SingletonMultiprocessing)
    - [SingletonAsyncio](#SingletonAsyncio)
  - [dicts](#dicts)
    - [update_dict](#update_dict)
  - [floats](#floats)
    - [randfloat](#randfloat)
    - [float_range](#float_range)
  - [lists](#lists)
    - [split_list](#split_list)
    - [replace_to_null](#replace_to_null)
  - [strings](#strings)
    - [text_between](#text_between)
    - [del_ws](#del_ws)
    - [format_number](#format_number)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)



<h1><p align="center">Short description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀The library contains convenient functions that are designed to replace routine actions. The library was created by the author to simplify personal work with the tools he uses, such as:
- Regular Python objects;
- MySQL;
- SQLAlchemy;
- Selenium, etc.

⠀After a while, he decided to publish the library, so if you find something useful for yourself, be sure to use it!



<h1><p align="center">Useful links</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀[pretty-utils](https://github.com/SecorD0/pretty-utils)

⠀[MySQL](https://www.mysql.com/)

⠀[SQLAlchemy](https://www.sqlalchemy.org/)

<h1><p align="center">Installation</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You need execute the command below to install or update the library:
```sh
pip install --force-reinstall git+https://github.com/SecorD0/pretty-utils
```



<h1><p align="center">databases</p></h1>
<p align="right"><a href="#Content">To the content</a></p>


<h2><p align="center">mysql</p></h2>

<h3><p align="center">DB</p></h3>

⠀It's a class to interact with a MySQL database via SQL queries. `__init__` initializes a class.

⠀Accepted arguments:
- `database (str)` — a database name
- `host (str)` — IP:port for connection to DB
- `user (str)` — a username for connection
- `passwd (str)` — a password for connection
- `**kwargs` — other arguments for connecting

⠀Usage:
```py
import os

from pretty_utils.databases.mysql import DB

db = DB(database='bot', passwd=str(os.getenv('DB_PASSWORD')))
```

<h3><p align="center">execute</p></h3>

⠀Executes SQL queries.

⠀Accepted arguments:
- `query (str)` — a query
- `data (tuple)` — a data for query
- `fetchone (bool)` — if `True` uses `fetchone`, otherwise uses `fetchall` in SELECT queries

⠀Usage:
```py
import os

from pretty_utils.databases.mysql import DB

db = DB(database='bot', passwd=str(os.getenv('DB_PASSWORD')))
db.execute('CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, u_id INT, username VARCHAR(255))')
db.execute('INSERT INTO users (u_id, username) VALUES (%s, %s)', (33, 'username',))
db.execute('INSERT INTO users (u_id, username) VALUES (%s, %s)', (102, 'gok',))
res = db.execute('SELECT * FROM users')
print(res)
# [(1, 33, 'username'), (2, 102, 'gok')]

db.execute('UPDATE users SET username = %s WHERE u_id = %s', ('new_username', 33,))
res = db.execute('SELECT * FROM users', fetchone=True)
print(res)
# (1, 33, 'new_username')

```


<h2><p align="center">sqlalchemy_</p></h2>

<h3><p align="center">DB</p></h3>

⠀It's a class that simplifies working with the SQLAlchemy library. `__init__` initializes a class.

⠀Accepted arguments:
- `db_url (str)` — a URL containing all the necessary parameters to connect to a DB
- `**kwargs` — other arguments for connecting

⠀Usage:
```py
from pretty_utils.databases.sqlalchemy_ import DB

db = DB('sqlite:///users.db', pool_recycle=3600, connect_args={'check_same_thread': False})
```

<h3><p align="center">create_database</p></h3>

⠀Creates a database if it doesn't exist. Used automatically during initialization.

⠀Accepted arguments:
- `database (str)` — a database name

<h3><p align="center">create_tables</p></h3>

⠀Creates tables.

⠀Accepted arguments:
- `base` — a base class for declarative class definitions

⠀Usage:
```py
from pretty_utils.databases.sqlalchemy_ import DB
from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    u_id = Column(Integer)
    username = Column(Text)


db = DB('sqlite:///users.db', pool_recycle=3600, connect_args={'check_same_thread': False})
db.create_tables(Base)
```

<h3><p align="center">all</p></h3>

⠀Fetches all rows.

⠀Accepted arguments:
- `entities` — an ORM entity
- `criterion` — criterion for rows filtering

⠀Returns `list` — the list of rows.

⠀Usage:
```py
...

users: List[User] = db.all(User)
print(users)
# [User(...), User(...), ...]
```

<h3><p align="center">one</p></h3>

⠀Fetches one row.

⠀Accepted arguments:
- `entities` — an ORM entity
- `criterion` — criterion for rows filtering
- `from_the_end` — get the row from the end

⠀Returns `list` — found row or None.

⠀Usage:
```py
...

user: User = db.one(User, (User.u_id == 33) & (User.username == 'username'))
print(user)
# User(id=1, u_id=33, username='username')
```

<h3><p align="center">execute</p></h3>

⠀Executes SQL query.

⠀Accepted arguments:
- `query` — the query
- `args` — any additional arguments

⠀Usage:
```py
...

temp_users: List[User] = db.execute('SELECT * FROM temp').fetchall()
print(temp_users)
# [User(...), User(...), ...]

db.execute('DROP TABLE temp')
```

<h3><p align="center">commit</p></h3>

⠀Commits changes.

⠀Usage:
```py
...

user: User = db.one(User, (User.u_id == 33) & (User.username == 'username'))
user.username = 'new_username'
db.commit()
```

<h3><p align="center">insert</p></h3>

⠀Inserts rows.

⠀Accepted arguments:
- `row` — an ORM entity or list of entities

⠀Usage:
```py
...

users = [User(u_id=33, username='username'), User(u_id=102, username='gok')]
db.insert(users)

db.insert(User(u_id=903, username='penny'))
```


<h2><p align="center">sqlite</p></h2>

<h3><p align="center">DB</p></h3>

⠀It's a class to interact with a SQLite3 database via SQL queries. `__init__` initializes a class.

⠀Accepted arguments:
- `database_file (str)` — a path to the database
- `**kwargs` — other arguments for connecting

⠀Usage:
```py
import os

from pretty_utils.databases.sqlite import DB

db = DB(os.path.join('databases', 'database.db'))
```

<h3><p align="center">execute</p></h3>

⠀Executes SQL queries.

⠀Accepted arguments:
- `query (str)` — a query
- `data (tuple)` — a data for query
- `fetchone (bool)` — if `True` uses `fetchone`, otherwise uses `fetchall` in SELECT queries
- `with_column_names (bool)` — if `True` returns column names in SELECT queries (False)
- `return_class (bool)` — if `True` returns dynamic class, otherwise returns tuple (True)

⠀Usage:
```py
from pretty_utils.databases.sqlite import DB

db = DB('database.db')
db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, u_id INTEGER, username TEXT)')
db.execute('INSERT INTO users (u_id, username) VALUES (?, ?)', (33, 'username',))
db.execute('INSERT INTO users (u_id, username) VALUES (?, ?)', (102, 'gok',))
res = db.execute('SELECT * FROM users')
print(res)
# [data(id=1, u_id=33, username='username'), data(id=2, u_id=102, username='gok')]

res = db.execute('SELECT * FROM users', return_class=False)
print(res)
# [(1, 33, 'username'), (2, 102, 'gok')]

db.execute('UPDATE users SET username = ? WHERE u_id = ?', ('new_username', 33,))
res = db.execute('SELECT * FROM users', fetchone=True)
print(res)
# data(id=1, u_id=33, username='new_username')
```

<h3><p align="center">dynamic_class</p></h3>

⠀Dynamically creates a class for received data similar to the one in SQLAlchemy, but without explicitly specifying instance variables.

⠀Accepted arguments:
- `class_name (str)` — a class name
- `variables (Union[list, tuple])` — variables of the class
- `values (Union[list, tuple])` — values of the specified variables

⠀Returns `object` — a created class.

⠀Usage:
```py
from pretty_utils.databases.sqlite import dynamic_class

print(dynamic_class('my_class', ('u_id', 'username'), (33, 'username')))
# my_class(u_id=33, username='username')
```

<h3><p align="center">make_sql</p></h3>

⠀Function was deprecated, use [DB class](#DB-2).



<h1><p align="center">miscellaneous</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀Various functions for different purposes.


<h2><p align="center">files</p></h2>

⠀Functions for working with files.

<h3><p align="center">join_path</p></h3>

⠀Join the path passed in the list or tuple.

⠀Accepted arguments:
- `path (Union[str, tuple, list])` — path to the object

⠀Returns `str` — the joined path.

⠀Usage:
```py
from pretty_utils.miscellaneous.files import join_path

path = join_path('data/images/1.png')
print(path)
# data/images/1.png

path = join_path(('data', 'images', '1.png'))
print(path)
# data\images\1.png

path = join_path(['data', 'images', '1.png'])
print(path)
# data\images\1.png
```

<h3><p align="center">touch</p></h3>

⠀Create an object (file or directory) if it doesn't exist.

⠀Accepted arguments:
- `path (Union[str, tuple, list])` — path to the object
- `file (bool)` — is it a file? (false)

⠀Returns `bool` — True if the object was created.

⠀Usage:
```py
from pretty_utils.miscellaneous.files import touch

resp = touch(path='images')
print(resp)
# True

resp = touch(path='images')
print(resp)
# False

resp = touch(path='text.txt', file=True)
print(resp)
# True
```

<h3><p align="center">write_json</p></h3>

⠀Write Python list or dictionary to a JSON file.

⠀Accepted arguments:
- `path (Union[str, tuple, list])` — path to the JSON file
- `obj (Union[list, dict])` — the Python list or dictionary
- `indent (Optional[int])` — the indent level (None)
- `encoding (Optional[str])` — the name of the encoding used to decode or encode the file (None)

⠀Usage:
```py
from pretty_utils.miscellaneous.files import write_json

users = [{'id': 33, 'username': 'username'}, {'id': 102, 'username': 'gok'}]
write_json(path='users.json', obj=users, indent=2)
```

<h3><p align="center">read_lines</p></h3>

⠀Read a file and return a list of lines.

⠀Accepted arguments:
- `path (Union[str, tuple, list])` — path to the file
- `skip_empty_rows (bool)` — if True it doesn't include empty rows to the list
- `encoding (Optional[str])` — the name of the encoding used to decode or encode the file (None)

⠀Returns `list` — the list of lines.

⠀Usage:
```py
from pretty_utils.miscellaneous.files import read_lines

with open('text.txt', 'w') as f:
    f.write('Hello,\n\nWorld!')

lines = read_lines(path='text.txt')
print(lines)
# ['Hello,', '', 'World!']

lines = read_lines(path='text.txt', skip_empty_rows=True, encoding='utf-8')
print(lines)
# ['Hello,', 'World!']
```

<h3><p align="center">read_json</p></h3>

⠀Read a JSON file and return a Python list or dictionary.

⠀Accepted arguments:
- `path (Union[str, tuple, list])` — path to the JSON file
- `encoding (Optional[str])` — the name of the encoding used to decode or encode the file (None)

⠀Returns `Union[list, dict]` — the Python list or dictionary.

⠀Usage:
```py
from pretty_utils.miscellaneous.files import write_json, read_json

users = [{'id': 33, 'username': 'username'}, {'id': 102, 'username': 'gok'}]
write_json(path='users.json', obj=users)

resp = read_json(path='users.json')
print(resp)
# [{'id': 33, 'username': 'username'}, {'id': 102, 'username': 'gok'}]
```

<h3><p align="center">resource_path</p></h3>

⠀Get absolute path to resource, works for dev and for PyInstaller.

⠀Accepted arguments:
- `relative_path (str)` — a relative path to the resource

⠀Returns `str` — an absolute path to the resource.

⠀Usage:
```py
from pretty_utils.miscellaneous.files import resource_path

absolute_path = resource_path(relative_path='images')
print(absolute_path)
# C:\python\my_project\images
```


<h2><p align="center">generators</p></h2>

⠀Functions for generating certain strings.

<h3><p align="center">username</p></h3>

⠀Generate a username.

⠀Accepted arguments:
- `len (int)` — length of a username (9)
- `capital (bool)` — capitalize the first letter (False)

⠀Returns `str` — the generated username.

⠀Usage:
```py
from pretty_utils.miscellaneous import generators

username = generators.username()
print(username)
# kuganurah

username = generators.username(len=15)
print(username)
# xohosyzinehucus

username = generators.username(len=6, capital=True)
print(username)
# Asexop
```

<h3><p align="center">password</p></h3>

⠀Generate a password.

⠀Accepted arguments:
- `len (int)` — length of a password (16)
- `use_capitals (bool)` — use capitals letters (True)
- `use_digits (bool)` — use digits (True)
- `use_specials (bool)` — use special symbols (False)

⠀Returns `str` — the generated password.

⠀Usage:
```py
from pretty_utils.miscellaneous import generators

password = generators.password()
print(password)
# bz7drWwcqK3AcI2h

password = generators.password(len=8, use_digits=False)
print(password)
# FuRbgKlA

password = generators.password(len=12, use_specials=True)
print(password)
# Lx1M7ph*Ytu=
```


<h2><p align="center">http</p></h2>

⠀Functions related to sending requests via `requests` or `aiohttp` libraries.

<h3><p align="center">aiohttp_params</p></h3>

⠀Convert requests params to aiohttp params.

⠀Accepted arguments:
- `params (Optional[Dict[str, Any]])` — requests params

⠀Returns `Optional[Dict[str, Union[str, int, float]]]` — aiohttp params.

⠀Usage:
```py
from pretty_utils.miscellaneous.http import aiohttp_params

params = {
    'a': True,
    'b': 1,
    'c': 1.0,
    'd': 'hello',
    'e': 'world',
    'f': None,
    'g': b'agsdgha==',
    'h': False,
    'i': None

}

print(aiohttp_params(params))
# {
# 	'a': 'true',
# 	'b': 1,
# 	'c': 1.0,
# 	'd': 'hello',
# 	'e': 'world',
# 	'g': 'agsdgha==',
# 	'h': 'false'
# }
```


<h2><p align="center">inputting</p></h2>

⠀Functions for data inputting.

<h3><p align="center">timeout_input</p></h3>

⠀Ask a user to enter a string, and if he doesn't do so in a certain amount of time, return the default value. Works only in `if __name__ == '__main__'` construction.

⠀Accepted arguments:
- `prompt (str)` — a prompt that will be displayed before the input request
- `timeout (Union[int, float])` — a timeout after which the default value will be returned (60)
- `default_value (str)` — a default value that will be returned after the timeout expires

⠀Returns `str` — the inputted or default value.

⠀Usage:
```py
from pretty_utils.miscellaneous.inputting import timeout_input

if __name__ == '__main__':
    name = timeout_input(prompt='Enter your name: ', default_value='John')  # Input 'Michael'
    print(f'Your name is {name}.\n')
    # Your name is Michael.

    print('''Select the action:
1) Do nothing;
2) Causing rain;
3) Causing an earthquake.''')
    action = timeout_input(prompt='> ', timeout=5, default_value='1')  # Just wait
    print(f'{name}, you select {action}!')
    # Michael, you select 1!
```


<h2><p align="center">selenium_</p></h2>

⠀It's a class that simplifies working with the Selenium library.

<h3><p align="center">Sel</p></h3>

⠀Initializes a class.

⠀Accepted arguments:
- `browser (webdriver)` — instance of WebDriver (Ie, Firefox, Chrome or Remote)

⠀Usage:
```py
from pretty_utils.miscellaneous.selenium_ import Sel
from selenium import webdriver

browser = webdriver.Chrome()
sel = Sel(browser)
```

<h3><p align="center">get_element</p></h3>

⠀Explicit waits of an element appearing.

⠀Accepted arguments:
- `find_it (str)` — a string to search for the element
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)

⠀Returns `WebElement` — the founded element.

⠀Usage:
```py
from pretty_utils.miscellaneous.selenium_ import Sel
from selenium import webdriver

browser = webdriver.Chrome()
sel = Sel(browser)
browser.get('https://www.google.com/')
element = sel.get_element('/html/body/div[1]/div[5]/div[2]/div[3]/span/span/g-popup/div[1]')
print(element)
# <selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>

browser.quit()
```

<h3><p align="center">get_text</p></h3>

⠀Explicit waits of an element appearing and get its text.

⠀Accepted arguments:
- `find_it (str)` — a string to search for the element
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)

⠀Returns `str` — the parsed text.

⠀Usage:
```py
from pretty_utils.miscellaneous.selenium_ import Sel
from selenium import webdriver

browser = webdriver.Chrome()
sel = Sel(browser)
browser.get('https://www.google.com/')
text = sel.get_text('/html/body/div[1]/div[5]/div[2]/div[3]/span/span/g-popup/div[1]')
print(text)
# Settings

browser.quit()
```

<h3><p align="center">wait_for_clickability</p></h3>

⠀Waiting for an element to become clickable.

⠀Accepted arguments:
- `find_it (str)` — a string to search for the element
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)

⠀Returns `WebElement` — the founded element.

⠀Usage:
```py
from pretty_utils.miscellaneous.selenium_ import Sel
from selenium import webdriver

browser = webdriver.Chrome()
sel = Sel(browser)
browser.get('https://www.google.com/')
element = sel.wait_for_clickability('/html/body/div[1]/div[5]/div[2]/div[3]/span/span/g-popup/div[1]')
print(element)
# <selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>

browser.quit()
```

<h3><p align="center">wait_for_visibility</p></h3>

⠀Waiting for an element to become visible.

⠀Accepted arguments:
- `find_it (str)` — a string to search for the element
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)

⠀Returns `WebElement` — the founded element.

⠀Usage:
```py
from pretty_utils.miscellaneous.selenium_ import Sel
from selenium import webdriver

browser = webdriver.Chrome()
sel = Sel(browser)
browser.get('https://www.google.com/')
element = sel.wait_for_visibility('/html/body/div[1]/div[5]/div[2]/div[3]/span/span/g-popup/div[1]')
print(element)
# <selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>

browser.quit()
```

<h3><p align="center">clear</p></h3>

⠀Explicit waits of an element appearing and clear its contents.

⠀Accepted arguments:
- `find_it (str)` — a string to search for the element
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)

⠀Returns `WebElement` — the founded element.

⠀Usage:
```py
import time
from pretty_utils.miscellaneous.selenium_ import Sel
from selenium import webdriver

browser = webdriver.Chrome()
sel = Sel(browser)
browser.get('https://www.google.com/')
sel.write('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', 'google')
time.sleep(5)
element = sel.clear('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
print(element)
# <selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>

time.sleep(5)
browser.quit()
```

<h3><p align="center">write</p></h3>

⠀Explicit waits of an element appearing and write a text to it.

⠀Accepted arguments:
- `find_it (str)` — a string to search for the element
- `text (str)` — a text to write
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)
- `clear (bool)` — clear the element before writing (True)

⠀Returns `WebElement` — the founded element.

⠀Usage:
```py
import time

from pretty_utils.miscellaneous.selenium_ import Sel
from selenium import webdriver

browser = webdriver.Chrome()
sel = Sel(browser)
browser.get('https://www.google.com/')
sel.write('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', 'google')
time.sleep(5)
element = sel.write('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', 'google')
print(element)
# <selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>

time.sleep(5)
browser.quit()
```

<h3><p align="center">click</p></h3>

⠀Explicit waits of an element appearing and click it.

⠀Accepted arguments:
- `find_it (str)` — a string to search for the element
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)

⠀Returns `WebElement` — the founded element.

⠀Usage:
```py
import time

from pretty_utils.miscellaneous.selenium_ import Sel
from selenium import webdriver

browser = webdriver.Chrome()
sel = Sel(browser)
browser.get('https://www.google.com/')
sel.click('/html/body/div[1]/div[5]/div[2]/div[3]/span/span/g-popup/div[1]')
sel.wait_for_clickability('//*[@id="lb"]/div/g-menu/g-menu-item[1]/div')
element = sel.click('//*[@id="lb"]/div/g-menu/g-menu-item[1]/div')
print(element)
# <selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>

time.sleep(5)
browser.quit()
```

<h3><p align="center">click_js</p></h3>

⠀Explicit waits of an element appearing and click it using JS script. Use it if simple click has no effect.

⠀Accepted arguments:
- `find_it (str)` — a string to search for the element
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)

⠀Returns `WebElement` — the founded element.

⠀Usage similar to that in the [click](#click) function.

<h3><p align="center">click_when_clicable</p></h3>

⠀Explicit waits of an element appearing and click it when clickable.

⠀Accepted arguments:
- `find_it (str)` — a string to search for the element
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)

⠀Returns `WebElement` — the founded element.

⠀Usage similar to that in the [click](#click) function.

<h3><p align="center">click_with_coord</p></h3>

⠀Explicit waits of an element appearing and click it via coordinates.

⠀Accepted arguments:
- `find_it (Union[str, WebElement])` — a string or WebElement to interact
- `sec (int)` — the element waiting time (10)
- `by (str)` — find the element by ... (XPATH)
- `x_off (int)` — x coordinate (1)
- `y_off (int)` — y coordinate (1)

⠀Returns `WebElement` — the founded element.

⠀Usage:
```py
import time

from pretty_utils.miscellaneous.selenium_ import Sel
from selenium import webdriver

browser = webdriver.Chrome()
sel = Sel(browser)
browser.get('https://www.google.com/')
sel.click_with_coord('/html/body/div[1]/div[5]/div[2]/div[3]/span/span/g-popup/div[1]', x_off=10, y_off=5)
time.sleep(5)
element = sel.click_when_clicable('//*[@id="lb"]/div/g-menu/g-menu-item[1]/div')
print(element)
# <selenium.webdriver.remote.webelement.WebElement (session="...", element="...")>

time.sleep(5)
browser.quit()
```


<h2><p align="center">time_and_date</p></h2>

⠀Functions for working with time and date.

<h3><p align="center">strtime_to_unix</p></h3>

⠀Convert string time to unix.

⠀Accepted arguments:
- `strtime (str)` — a string time
- `utc_offset (int)` — hour offset from UTC (0)
- `format (str)` — format for string time parsing (%d.%m.%Y %H:%M)

⠀Returns `int` — the unix time.

⠀Usage:
```py
from pretty_utils.miscellaneous.time_and_date import strtime_to_unix

str_time = '27.06.2022 12:35'

print(strtime_to_unix(strtime=str_time, utc_offset=0))  # 12:35 UTC
# 1656333300

print(strtime_to_unix(strtime=str_time, utc_offset=-4))  # 16:35 UTC
# 1656347700

print(strtime_to_unix(strtime=str_time, utc_offset=3))  # 09:35 UTC
# 1656322500
```

<h3><p align="center">unix_to_strtime</p></h3>

⠀Convert unix to string time. In particular return the current time.

⠀Accepted arguments:
- `unix_time (Union[int, float, str])` — a unix time (current)
- `utc_offset (int)` — hour offset from UTC (None)
- `format (str)` — format for string time output (%d.%m.%Y %H:%M)

⠀Returns `str` — the string time.

⠀Usage:
```py
from pretty_utils.miscellaneous.time_and_date import unix_to_strtime

print(unix_to_strtime(unix_time=1665831600))  # 11:00 UTC
# 15.10.2022 11:00:00

print(unix_to_strtime(unix_time=1665831600.0, utc_offset=2))  # 11:00 -> 13:00 UTC+2
# 15.10.2022 13:00:00

print(unix_to_strtime(unix_time='1665831600', utc_offset=-4))  # 11:00 -> 07:00 UTC-4
# 15.10.2022 07:00:00

print(unix_to_strtime(utc_offset=3, format="%d.%m.%Y %H:%M"))
# 15.10.2022 16:34
```



<h1><p align="center">type_functions</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀Functions for working with certain Build-in Python data types.


<h2><p align="center">bools</p></h2>

⠀Functions for working with `bool` data type.

<h3><p align="center">randbool</p></h3>

⠀Returns a random bool.

⠀Usage:
```py
from pretty_utils.type_functions.bools import randbool

print(randbool())
# True

print(randbool())
# False
```


<h2><p align="center">classes</p></h2>

⠀Classes with various implemented functions to be inherited by other classes.

<h3><p align="center">AutoRepr</p></h3>

⠀Contains a `__repr__` function that automatically builds the output of a class using all its variables.

⠀Usage:
```py
from pretty_utils.type_functions.classes import AutoRepr


class UnreadablePerson:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class ReadablePerson(AutoRepr):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


person = UnreadablePerson(name='John', age=32)
print(person)
# <__main__.UnreadablePerson object at 0x...>

person = ReadablePerson(name='John', age=32)
print(person)
# ReadablePerson(name='John', age=32)
```

<h3><p align="center">Singleton</p></h3>

⠀A class that implements the singleton pattern.

⠀Usage:
```py
from pretty_utils.type_functions.classes import AutoRepr, Singleton


class SettingsS(Singleton):
    def __init__(self, a: int):
        self.a = a


class SettingsSA(Singleton, AutoRepr):
    def __init__(self, a: int):
        self.a = a


class Settings:
    def __init__(self, a: int):
        self.a = a


settings_s = SettingsS(a=1)
print(id(settings_s), settings_s.a, settings_s)
# 1622951686000 1 <__main__.SettingsS object at 0x00000179DF756F70>

settings_s = SettingsS(a=2)
print(id(settings_s), settings_s.a, settings_s)
# 1622951686000 2 <__main__.SettingsS object at 0x00000179DF756F70>

settings_sa = SettingsSA(a=1)
print(id(settings_sa), settings_sa)
# 1622951752704 SettingsSA(a=1)

settings_sa = SettingsSA(a=2)
print(id(settings_sa), settings_sa)
# 1622951752704 SettingsSA(a=2)

settings = Settings(a=1)
print(id(settings), settings.a, settings)
# 1622951753664 1 <__main__.Settings object at 0x00000179DF7677C0>

settings = Settings(a=2)
print(id(settings), settings.a, settings)
# 1622951753712 2 <__main__.Settings object at 0x00000179DF7677F0>
```

<h3><p align="center">SingletonThreading</p></h3>

⠀A class that implements the singleton pattern with the threading lock.

⠀Usage similar to that in the [Singleton](#Singleton) function.

<h3><p align="center">SingletonMultiprocessing</p></h3>

⠀A class that implements the singleton pattern with the multiprocessing lock.

⠀Usage similar to that in the [Singleton](#Singleton) function.

<h3><p align="center">SingletonAsyncio</p></h3>

⠀A class that implements the singleton pattern with the asyncio lock.

⠀Usage similar to that in the [Singleton](#Singleton) function.


<h2><p align="center">dicts</p></h2>

⠀Functions for working with `dict` data type.

<h3><p align="center">update_dict</p></h3>

⠀Update the specified dictionary with any number of dictionary attachments based on the template without changing the values already set.

⠀Accepted arguments:
- `modifiable (dict)` — a dictionary for template-based modification
- `template (dict)` — the dictionary-template
- `rearrange (bool)` — make the order of the keys as in the template, and place the extra keys at the end (True)
- `remove_extra_keys (bool)` — whether to remove unnecessary keys and their values (False)

⠀Returns `dict` — the modified dictionary.

⠀Usage:
```py
from pretty_utils.type_functions.dicts import update_dict

a = {
    'custom': 'world',  # extra key
    'bool': True,
    'list': [0, 1, 2, 3],  # edited list
    'float': 10.4,
    'dict': {
        'bool': False,  # edited bool
        'dict': {
            'list': [0, 3],  # edited list
            'custom': 'bye',  # extra key
            'int': 10
        }
    }
}

b = {
    'bool': True,
    'dict': {
        'bool': True,
        'dict': {
            'int': 10,
            'list': [0, 1, 2, 3]
        }
    },
    'float': 10.4,
    'int': 100,
    'list': [0, 1],
    'str': 'hello'
}

print(update_dict(modifiable=a, template=b))
# {
# 	'bool': True,
# 	'dict': {
# 		'bool': False,
# 		'dict': {
# 			'int': 10,
# 			'list': [0, 3],
# 			'custom': 'bye'
# 		}
# 	},
# 	'float': 10.4,
# 	'int': 100,
# 	'list': [0, 1, 2, 3],
# 	'str': 'hello',
# 	'custom': 'world'
# }

print(update_dict(modifiable=a, template=b, rearrange=False))
# {
# 	'custom': 'world',
# 	'bool': True,
# 	'list': [0, 1, 2, 3],
# 	'float': 10.4,
# 	'dict': {
# 		'bool': False,
# 		'dict': {
# 			'list': [0, 3],
# 			'custom': 'bye',
# 			'int': 10
# 		}
# 	},
# 	'int': 100,
# 	'str': 'hello'
# }

print(update_dict(modifiable=a, template=b, rearrange=False, remove_extra_keys=True))
# {
# 	'bool': True,
# 	'list': [0, 1, 2, 3],
# 	'float': 10.4,
# 	'dict': {
# 		'bool': False,
# 		'dict': {
# 			'list': [0, 3],
# 			'int': 10
# 		}
# 	},
# 	'int': 100,
# 	'str': 'hello'
# }
```

<h2><p align="center">floats</p></h2>

⠀Functions for working with `float` data type.

<h3><p align="center">randfloat</p></h3>

⠀Return a random float from the range.

⠀Accepted arguments:
- `from_ (Union[int, float])` — the minimum value
- `to_ (Union[int, float])` — the maximum value
- `step (Union[int, float])` — the step size (calculated based on the number of decimal places)

⠀Returns `float` — the random float.

⠀Usage:
```py
from pretty_utils.type_functions.floats import randfloat

print(randfloat(5.3, 6.2))
# 5.3

print(randfloat(1.05, 1.1))
# 1.07

print(randfloat(0.6, 1.7, 0.3))
# 1.5

print(randfloat(0.6, 0.7, 0.02))
# 0.7
```

<h3><p align="center">float_range</p></h3>

⠀Return a float range.

⠀Accepted arguments:
- `from_ (Union[int, float])` — a range start value
- `to_ (Union[int, float])` — the range stop value, not included
- `step (Union[int, float])` — the step size (calculated based on the number of decimal places)

⠀Returns `list` — the range list.

⠀Usage:
```py
from pretty_utils.type_functions.floats import float_range

print(float_range(5.3, 6.2))
# [5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1]

print(float_range(1.05, 1.1))
# [1.05, 1.06, 1.07, 1.08, 1.09]

print(float_range(0.6, 1.7, 0.3))
# [0.6, 0.9, 1.2, 1.5]

print(float_range(0.6, 0.7, 0.02))
# [0.6, 0.62, 0.64, 0.66, 0.68]

print(float_range(7.25, 6.91, -0.05))
# [7.25, 7.2, 7.15, 7.1, 7.05, 7.0, 6.95]
```

<h2><p align="center">lists</p></h2>

⠀Functions for working with `list` data type.

<h3><p align="center">split_list</p></h3>

⠀Split a list to several lists.

⠀Accepted arguments:
- `s_list (list)` — a list to split
- `n (int)` — split the list into parts of N elements (100)
- `parts (bool)` — split the list into N parts (False)

⠀Returns `list` — the split list.

⠀Usage:
```py
from pretty_utils.type_functions.lists import split_list

l = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]

for sl in split_list(l, 2):
    print(sl)
# [[1, 2], [3, 4]]
# [[5, 6], [7, 8]]
# [[9, 10], [11, 12]]
    
print()

for sl in split_list(l, 2, True):
    print(sl)
# [[1, 2], [3, 4], [5, 6]]
# [[7, 8], [9, 10], [11, 12]]
```

<h3><p align="center">replace_to_null</p></h3>

⠀Replace all None in a list with 0.

⠀Accepted arguments:
- `r_list (list)` — a list to replace

⠀Returns `list` — the processed list.

⠀Usage:
```py
from pretty_utils.type_functions.lists import replace_to_null

print(replace_to_null([22, None, 84, None, None, 1, 0]))
# [22, 0, 84, 0, 0, 1, 0]
```


<h2><p align="center">strings</p></h2>

⠀Functions for working with `str` data type.

<h3><p align="center">text_between</p></h3>

⠀Extract a text between strings.

⠀Accepted arguments:
- `text (str)` — a source text
- `begin (str)` — a string from the end of which to start the extraction
- `end (str)` — a string at the beginning of which the extraction should end

⠀Returns `str` — the extracted text or empty string if nothing is found.

⠀Usage:
```py
from pretty_utils.type_functions.strings import text_between

text = '''
Well done is better than well said.
Save when you can and not when you have to.
Don't slay dragons that aren't in your way.
'''

print(text_between(text, 'when ', ' slay') + '\n---')
# you can and not when you have to.
# Don't
# ---

print(text_between(text, end='when') + '\n---')
#
# Well done is better than well said.
# Save 
# ---

print(text_between(text, 'dragons ') + '\n---')
# that aren't in your way.
#
# ---

print(text_between(text, 'another') + '\n---')
#
# ---

print(text_between(text, 'you ', ' you'))
# can and not when
```

<h3><p align="center">del_ws</p></h3>

⠀Delete whitespaces.

⠀Accepted arguments:
- `text (str)` — a source text

⠀Returns `str` — the text without whitespaces.

⠀Usage:
```py
from pretty_utils.type_functions.strings import del_ws

text = 'Well done is better than well said.'

print(del_ws(text))
# Welldoneisbetterthanwellsaid.
```

<h3><p align="center">format_number</p></h3>

⠀Return formatted number like 3 392 233.9420.

⠀Accepted arguments:
- `number (Union[int, float])` — a number for formatting

⠀Returns `str` — the formatted number.

⠀Usage:
```py
from pretty_utils.type_functions.strings import format_number

print(format_number(14_386_730))
# 14 386 730

print(format_number(8401.6047))
# 8 401.6047

print(format_number(24_801_302.0192, thousands_separator=','))
# 24,801,302.0192

print(format_number(1_000_922.3905, thousands_separator="'"))
# 1'000'922.3905
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/pretty-utils/issues/new/choose),
select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!

- Ethereum-like address (Ethereum, BSC, Moonbeam, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`