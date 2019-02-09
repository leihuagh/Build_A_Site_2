# Build a Site

## Resources

- Tutorial: [YouTube Aarav Tech](https://www.youtube.com/watch?v=IBpclPsLgA0&list=PL1WVjBsN-_NIdlnACz0Mxuq8VcuxER-is&index=1)

## Packages

### Global Level

- Python 3.7.2
- virturalenv 6.3.0

### Project Level

- Django 2.1.5
- mysqlclient: download `mysqlclient‑1.4.1‑cp37‑cp37m‑win_amd64.whl` from [https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient)
- pillow

## File System Structure

### Project Name:

- config

### Apps

- core
- employees: extends Django User
- polls

## Commands

### Create a Project

```shell
django-admin startproject config .
```

### Create the apps

```shell
python manage.py startapp core
python manage.py startapp employees
python manage.py startapp polls
```

### Make Migrations

```shell
python manage.py makemigrations
```

### Migrate

```shell
python manage.py migrate
```

### Dump Database Tables

```shell
python manage.py dumpdata auth.User --format json --indent 4 > texture/users.json
python manage.py dumpdata employees.Profile --format json --indent 4 > texture/profiles.json
python manage.py dumpdata polls.Question --format json --indent 4 > texture/questions.json
python manage.py dumpdata polls.Choice --format json --indent 4 > texture/choices.json
```

### Seed Database Tables

```shell
python manage.py loaddata texture/users.json
python manage.py loaddata texture/profiles.json
python manage.py loaddata texture/questions.json
python manage.py loaddata texture/choices.json
```

## Pagination Variables

```python
<ul>
    <li>{{ questions.has_previous}}</li>
    <li>{{ questions.number }}</li>
    <li>{{ questions.paginator.count }}</li>
    <li>{{ questions.paginator.page_range }}</li>
    <li>{{ questions.has_next }}</li>
</ul>
```
