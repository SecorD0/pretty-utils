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

<h3><p align="center">DB</p></h3>

⠀It's a class to interact with a MySQL database via SQL queries.

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

<h3><p align="center">DB</p></h3>

⠀It's a class that simplifies working with the SQLAlchemy library.

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