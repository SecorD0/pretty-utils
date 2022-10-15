<h1><p align="center">Pretty Utils</p></h1>

<p align="center"><img src="images/icon.ico" width="400"></p>



<h1><p align="center">Content</p></h1>

- [Short description](#Short-description)
- [Useful links](#Useful-links)
- [File structure](#File-structure)
- [How to run](#How-to-run)
    - [Windows](#Windows)
    - [Source code](#Source-code)
- [Functions](#Functions)
    - [Find maFiles by account logins and/or SteamID64s](#Find-maFiles-by-account-logins-andor-SteamID64s)
    - [Name maFiles as logins](#Name-maFiles-as-logins)
    - [Name maFiles as SteamID64s](#Name-maFiles-as-SteamID64s)
    - [Add maFiles to the manifest](#Add-maFiles-to-the-manifest)
    - [Exclude non-existent maFiles from the manifest](#Exclude-non-existent-maFiles-from-the-manifest)
- [Report a bug or suggest an idea](#Report-a-bug-or-suggest-an-idea)
- [Express your gratitude](#Express-your-gratitude)

<h1><p align="center">Short description</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀Convenient Python functions in one package.



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

⠀It's a class to interact with a MySQL database via SQL queries.

<h3><p align="center">DB</p></h3>

⠀Initializes a class.

⠀Accepted arguments:
- database (str) — a database name
- host (str) — IP:port for connection to DB
- user (str) — a username for connection
- passwd (str) — a password for connection
- **kwargs — other arguments for connecting

⠀Usage:
```py
import os

from pretty_utils.databases.mysql import DB

db = DB(database='bot', passwd=str(os.getenv('DB_PASSWORD')))
```

<h3><p align="center">execute</p></h3>

⠀Executes SQL queries.

⠀Accepted arguments:
- query (str) — a query
- data (tuple) — a data for query
- ret1 (bool) — if `True` uses `fetchone`, otherwise uses `fetchall` in SELECT queries

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
res = db.execute('SELECT * FROM users', ret1=True)
print(res)
# (1, 33, 'new_username')
```


<h2><p align="center">sqlalchemy_</p></h2>

⠀It's a class that simplifies working with the SQLAlchemy library.

<h3><p align="center">DB</p></h3>

⠀Initializes a class.

⠀Accepted arguments:
- db_url (str) — a URL containing all the necessary parameters to connect to a DB
- **kwargs — other arguments for connecting

⠀Usage:
```py
from pretty_utils.databases.sqlalchemy_ import DB

db = DB('sqlite:///users.db', pool_recycle=3600, connect_args={'check_same_thread': False})
```

<h3><p align="center">create_database</p></h3>

⠀Creates a database if it doesn't exist. Used automatically during initialization.

⠀Accepted arguments:
- database (str) — a database name

<h3><p align="center">create_tables</p></h3>

⠀Creates tables.

⠀Accepted arguments:
- base — a base class for declarative class definitions

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
- entities — an ORM entity
- criterion — criterion for rows filtering

⠀Returns list — the list of rows.

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
- entities — an ORM entity
- criterion — criterion for rows filtering
- from_the_end — get the row from the end

⠀Returns list — found row or None.

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
- query — the query
- args — any additional arguments

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
- row — an ORM entity or list of entities

⠀Usage:
```py
...

users = [User(u_id=33, username='username'), User(u_id=102, username='gok')]
db.insert(users)

db.insert(User(u_id=903, username='penny'))
```


<h2><p align="center">sqlite</p></h2>

⠀Deprecated, use SQLAlchemy.



<h1><p align="center">miscellaneous</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀Various functions for different purposes.


<h2><p align="center">files</p></h2>

⠀Functions for working with files.

<h3><p align="center">touch</p></h3>

⠀Create an object (file or directory) if it doesn't exist.

⠀Accepted arguments:
- path (str) — path to the object
- file (bool) — is it a file? (false)

⠀Returns bool — True if the object was created.

⠀Usage:
```py
from pretty_utils.miscellaneous.files import touch

resp = touch('images')
print(resp)
# True
resp = touch('images')
print(resp)
# False
resp = touch('text.txt', True)
print(resp)
# True
```

<h3><p align="center">write_json</p></h3>

⠀Write Python list or dictionary to a JSON file.

⠀Accepted arguments:
- path (str) — path to the JSON file
- obj (list or dict) — the Python list or dictionary

⠀Usage:
```py
from pretty_utils.miscellaneous.files import write_json

users = [{'id': 33, 'username': 'username'}, {'id': 102, 'username': 'gok'}]
write_json('users.json', users)
```

<h3><p align="center">read_lines</p></h3>

⠀Read a file and return a list of lines.

⠀Accepted arguments:
- path (str) — path to the file
- skip_empty_rows (bool) — if True it doesn't include empty rows to the list

⠀Returns list — the list of lines.

⠀Usage:
```py
from pretty_utils.miscellaneous.files import read_lines

with open('text.txt', 'w') as f:
    f.write('Hello,\n\nWorld!')

lines = read_lines('text.txt')
print(lines)
# ['Hello,', '', 'World!']

lines = read_lines('text.txt', True)
print(lines)
# ['Hello,', 'World!']
```

<h3><p align="center">read_json</p></h3>

⠀Read a JSON file and return a Python list or dictionary.

⠀Accepted arguments:
- path (str) — path to the JSON file

⠀Returns list or dict — the Python list or dictionary.

⠀Usage:
```py
from pretty_utils.miscellaneous.files import write_json, read_json

users = [{'id': 33, 'username': 'username'}, {'id': 102, 'username': 'gok'}]
write_json('users.json', users)

resp = read_json('users.json')
print(resp)
# [{'id': 33, 'username': 'username'}, {'id': 102, 'username': 'gok'}]
```

<h3><p align="center">resource_path</p></h3>

⠀Get absolute path to resource, works for dev and for PyInstaller.

⠀Accepted arguments:
- relative_path (str) — a relative path to the resource

⠀Returns str — an absolute path to the resource.

⠀Usage:
```py
from pretty_utils.miscellaneous.files import resource_path

absolute_path = resource_path('images')
print(absolute_path)
# C:\python\my_project\images
```


<h2><p align="center">generators</p></h2>

⠀Functions for generating certain strings.

<h3><p align="center">username</p></h3>

⠀Generate a username.

⠀Accepted arguments:
- len (str) — length of a username (9)
- capital (bool) — capitalize the first letter (False)

⠀Returns str — the generated username.

⠀Usage:
```py
from pretty_utils.miscellaneous import generators

username = generators.username()
print(username)
# kuganurah

username = generators.username(15)
print(username)
# xohosyzinehucus

username = generators.username(6, True)
print(username)
# Asexop
```

<h3><p align="center">password</p></h3>

⠀Generate a password.

⠀Accepted arguments:
- len (str) — length of a password (16)
- use_capitals (bool) — use capitals letters (True)
- use_digits (bool) — use digits (True)
- use_specials (bool) — use special symbols (False)

⠀Returns str — the generated password.

⠀Usage:
```py
from pretty_utils.miscellaneous import generators

password = generators.password()
print(password)
# bz7drWwcqK3AcI2h

password = generators.password(8, use_digits=False)
print(password)
# FuRbgKlA

password = generators.password(12, use_specials=True)
print(password)
# Lx1M7ph*Ytu=
```


<h2><p align="center">selenium_</p></h2>

⠀It's a class that simplifies working with the Selenium library.

<h3><p align="center">Sel</p></h3>

⠀Initializes a class.

⠀Accepted arguments:
- browser (webdriver) — instance of WebDriver (Ie, Firefox, Chrome or Remote)

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
- find_it (str) — a string to search for the element
- sec (int) — the element waiting time (10)
- by (str) — find the element by ... (XPATH)

⠀Returns WebElement — the founded element.

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
- find_it (str) — a string to search for the element
- sec (int) — the element waiting time (10)
- by (str) — find the element by ... (XPATH)

⠀Returns str — the parsed text.

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
- find_it (str) — a string to search for the element
- sec (int) — the element waiting time (10)
- by (str) — find the element by ... (XPATH)

⠀Returns WebElement — the founded element.

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

<h3><p align="center">clear</p></h3>

⠀Explicit waits of an element appearing and clear its contents.

⠀Accepted arguments:
- find_it (str) — a string to search for the element
- sec (int) — the element waiting time (10)
- by (str) — find the element by ... (XPATH)

⠀Returns WebElement — the founded element.

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
- find_it (str) — a string to search for the element
- text (str) — a text to write
- sec (int) — the element waiting time (10)
- by (str) — find the element by ... (XPATH)
- clear (bool) — clear the element before writing (True)

⠀Returns WebElement — the founded element.

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
- find_it (str) — a string to search for the element
- sec (int) — the element waiting time (10)
- by (str) — find the element by ... (XPATH)

⠀Returns WebElement — the founded element.

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
- find_it (str) — a string to search for the element
- sec (int) — the element waiting time (10)
- by (str) — find the element by ... (XPATH)

⠀Returns WebElement — the founded element.

⠀Usage similar to that in the [click](#click) function.

<h3><p align="center">click_when_clicable</p></h3>

⠀Explicit waits of an element appearing and click it when clickable.

⠀Accepted arguments:
- find_it (str) — a string to search for the element
- sec (int) — the element waiting time (10)
- by (str) — find the element by ... (XPATH)

⠀Returns WebElement — the founded element.

⠀Usage similar to that in the [click](#click) function.

<h3><p align="center">click_with_coord</p></h3>

⠀Explicit waits of an element appearing and click it via coordinates.

⠀Accepted arguments:
- find_it (str or WebElement) — a string or WebElement to interact
- sec (int) — the element waiting time (10)
- by (str) — find the element by ... (XPATH)
- x_off (int) — x coordinate (1)
- y_off (int) — y coordinate (1)

⠀Returns WebElement — the founded element.

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
- strtime (str) — a string time
- utc_offset (int) — hour offset from UTC (0)
- format (str) — format for string time parsing (%d.%m.%Y %H:%M)

⠀Returns int — the unix time.

⠀Usage:
```py
from pretty_utils.miscellaneous.time_and_date import strtime_to_unix

str_time = '27.06.2022 12:35'

print(strtime_to_unix(str_time, 0))  # 12:35 UTC
# 1656333300
print(strtime_to_unix(str_time, -4))  # 16:35 UTC
# 1656347700
print(strtime_to_unix(str_time, 3))  # 09:35 UTC
# 1656322500
```

<h3><p align="center">unix_to_strtime</p></h3>

⠀Convert unix to string time. In particular return the current time.

⠀Accepted arguments:
- strtime (int or float or str) — a unix time (current)
- utc_offset (int) — hour offset from UTC (None)
- format (str) — format for string time output (%d.%m.%Y %H:%M)

⠀Returns str — the string time.

⠀Usage:
```py
from pretty_utils.miscellaneous.time_and_date import unix_to_strtime

print(unix_to_strtime(1665831600))  # 11:00 UTC
# 15.10.2022 11:00
print(unix_to_strtime(1665831600.0, 2))  # 11:00 -> 13:00 UTC+2
# 15.10.2022 13:00
print(unix_to_strtime('1665831600', -4))  # 11:00 -> 07:00 UTC-4
# 15.10.2022 07:00
print(unix_to_strtime(utc_offset=3, format="%d.%m.%Y %H:%M:%S"))
# 15.10.2022 16:34:48
```



<h1><p align="center">Report a bug or suggest an idea</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀If you found a bug or have an idea, go to [the link](https://github.com/SecorD0/mafiles-toolkit/issues/new/choose),
select the template, fill it out and submit it.



<h1><p align="center">Express your gratitude</p></h1>
<p align="right"><a href="#Content">To the content</a></p>

⠀You can express your gratitude to the developer by sending fund to crypto wallets!

- Ethereum-like address (Ethereum, BSC, Moonbeam, etc.): `0x900649087b8D7b9f799F880427DacCF2286D8F20`
- USDT TRC-20: `TNpBdjcmR5KzMVCBJTRYMJp16gCkQHu84K`
- SOL: `DoZpXzGj5rEZVhEVzYdtwpzbXR8ifk5bajHybAmZvR4H`
- BTC: `bc1qs4a0c3fntlhzn9j297qdsh3splcju54xscjstc`