# selenium-stackoverflow-login
A Selenium script written in Python to log onto Stackoverflow everyday

## Why the script?
Why create a script to log onto a website every day and only go to the profile page? The same reason we do anything really - dopamine.
There is a gold badge on the programming website Stackoverflow that is given for logging onto the website every day for 100 days in a row.
Now logging on every day is a problem, but if there's anything I love more than solving problems, it's automating their solutions.

## How to run it?

1. Create a premium pythonanywhere account (needed to run Selenium)
2. Create a file called 'so-login.py' in your user folder (home/yourusername/so-login.py)
3. Click 'Tasks' on the top right, and add a daily task to run the above file

## How to check that it's working?
1. Stackover counts days as UTC, so run your script soon after then (It is not recommended to run on the hour, as most people set this time and therefore it can be delayed. Rather test fate and go at 13 minutes passed.)
2. Go to your profile and pin the Fanatic badge progress to it.
3. The next day, on a browser that is not logged in to Stackoverflow, go to your profile and the consequtive days should be increased by one.

## What to do if it's not working?
1. Go to the tasks page on Pythonanywhere and check the task log after it has run one. A successful output will look like below:

```
Got Stackoverflow homepage
Submitted email and password
Got Stackoverflow profile page
Successfully logged in
Got profile activity page
Completed

2022-11-24 02:28:22 -- Completed task, took 17.08 seconds, return code was 0.
```