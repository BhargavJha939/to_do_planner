# To-Do Planner with Deadlines

A command-line to-do list that keeps track of due dates and tells you
what's overdue or coming up soon.

## Why I made this-

I just kept forgetting assignment deadlines, so I wanted
something that would actually tell me "hey this is overdue" every time I
opened it instead of me having to remember to check a calendar.

## What it does-

* Add a task with a title, due date and priority (High/Medium/Low)
* Edit a task's title or due date
* Mark a task as done
* Delete a task
* View all tasks or just the pending ones, sorted by due date then
priority
* Shows a status next to each task - DONE, OVERDUE by X days, DUE TODAY,
due in X days, or upcoming
* Prints overdue/due-soon alerts automatically when you open the program
* Summary report (how many done, pending, overdue, completion %)
* Saves to a file so tasks are still there next time

Project layout-
to\_do\_planner/
├── main.py          # run this - the menu loop
├── config.py        # file paths, priority labels, how many days counts as "due soon"
├── validators.py     # input checking
├── tasks.py          # add/edit/complete/delete tasks
├── planner.py         # status logic, sorting, the alerts
├── reports.py         # builds and saves the summary
├── tests/
│   └── test\_todo\_planner.py
└── data/
├── tasks.json   
└── todo\_report.txt

## How to run it

Just Python 3, nothing extra to install.
cd to\_do\_planner
python3 main.py
Follow the menu.

## Some things worth knowing

* Dates have to be YYYY-MM-DD, the program will keep
asking until you get the format right.
* "Due soon" is set to 2 days by default - you can change `DUE\\\_SOON\\\_DAYS`
in config.py if you want a bigger window.

## Possible improvements later

* Recurring tasks (e.g. weekly assignments)
* Sub-tasks / checklists within a task
* Maybe color output in the terminal so overdue tasks stand out more

