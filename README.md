README.md Capital - Test task
=============================

Task
---------------------------

Using Python 3.6+, Django 2+, JSON, ...

Some Python Task - Python Test Assignmment

Implementation
---------------------------

Run 
python manage.py runserver

Visit 
http://localhost:8000/categories...
accordign to the task,

or run 
    /examples/run-all-tests.sh
and see results in corresponding .out files,
or run
    /examples/example1.sh
etc
to see results on the screen.

Details
-------------------------

The task did not specify if we can load data to the database once or more.

- To use it once, comment out in cap1/views.py
dropdata()
numer.restart()

- To add data to DB, comment out the variant with
numer.rebase()

The system sqlite3 database in root directory is used,
it is not good generally, but works well for single-time test task.

Python module json.tools is used to pretty-print output.

Renumeration of records in DB from last() or max() is possible.

We respect PEP8, except for placing of spaces:
we must always put a space between any word and subsequent opening
paren,
for humans read texts word after word, and long sequences like
goodfunction1(otherfunction2(anothernewfunction3(testfunction4(withparameter1), 2, 3), 4))
are unreadable, untestable, upsupportable.

