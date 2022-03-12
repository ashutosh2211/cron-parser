# Cron Expression Parser

Write a command line application or script which parses a cron string and expands each field to show the times at which it will run. You may use whichever language you feel most comfortable with.
You should only consider the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command, and you do not need to handle the special time strings such as "@yearly". The input will be on a single line.

The cron string will be passed to your application as a single argument.

```angular2html
~$ your-program "*/15 0 1,15 * 1-5 /usr/bin/find"
```

The output should be formatted as a table with the field name taking the first 14 columns and
the times as a space-separated list following it. For example, the following input argument:

`*/15 0 1,15 * 1-5 /usr/bin/find`

Should yield the following output:

```angular2html
minutes        0 15 30 45
hours          0
day of month   1 15
month          1 2 3 4 5 6 7 8 9 10 11 12
day of week    1 2 3 4 5
command        /usr/bin/find
```
---
## How to run
```
➜  cd cron-parser
➜ [cron-parser] pip install poetry==1.1.13
➜ [cron-parser] poetry install
➜ [cron-parser] poetry run python parser.py "<cron_expression>"
```
### Example
```shell
➜ [cron-parser] poetry run python parser.py "10-49/10 6-10/2 * 1-10/2 3,4 /usr/bin/find"
minute                   10 20 30 40
hour                     6 8 10
day of month             1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31
month                    1 3 5 7 9
day of week              3 4
command                  /usr/bin/find
```
---
### Run tests
```
➜  cd cron-parser
➜ [cron-parser] poetry run pytest
```

### Run coverage
```
➜  cd cron-parser
➜ [cron-parser] poetry run coverage run -m pytest
➜ [cron-parser] poetry run coverage report
```

---
## Cases not covered
- We have not considered the month and day of week names such as `jan`, `feb` or `mon` while building the parser.
- Currently, there is no special handling to show dates only till 28, as of now 31 is the upper range for all months  