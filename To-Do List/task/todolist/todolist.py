from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///todo.db?check_same_thread=False')


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


class ToDo:
    def __init__(self):
        self.list_menu = {1: "Today's tasks", 2: "Week's tasks", 3: "All tasks", 4: "Add task", 0: "Exit"}

    def menu(self):
        for k, v in self.list_menu.items():
            print(f"{k}) {v}")

    def print_tasks(self, tasks, date=datetime.now().date()):
        print()
        print(f"{date.strftime('%A %d %b')}:")
        if len(tasks) == 0:
            print("Nothing to do!")
            print()
        else:
            i = 1
            for task in tasks:
                print(f"{i}. {task.task}")
                i += 1
            print()

    def print_all_tasks(self, tasks):
        print("All tasks:")
        i = 1
        for task in tasks:
            print(f"{i}. {task.task}. {task.deadline.strftime('%d %b')}")
            i += 1
        print()

    def today_task(self):
        today = datetime.now().date()
        row = session.query(Table).filter(Table.deadline == today).all()
        self.print_tasks(row, today)

    def week_tasks(self):
        today = datetime.now().date()
        for x in range(0, 7):
            select_day = today + timedelta(days=x)
            row = session.query(Table).filter(Table.deadline == select_day).all()
            self.print_tasks(row, select_day)

    def all_tasks(self):
        row = session.query(Table).all()
        self.print_all_tasks(row)

    def task_add(self, task, deadline):
        new_row = Table(task=task, deadline=deadline)
        session.add(new_row)
        session.commit()
        return 0

    def run(self):
        while True:
            self.menu()
            choose = input()
            if choose == "1":
                self.today_task()
            elif choose == "2":
                self.week_tasks()
            elif choose == "3":
                self.all_tasks()
            elif choose == "4":
                print("Enter task")
                task = input()
                print("Enter deadline")
                dead = input()
                deadline = datetime.strptime(dead, '%Y-%m-%d').date()
                if self.task_add(task, deadline) == 0:
                    print("The task has been added!")
            elif choose == "0":
                print("Bye!")
                break


td = ToDo()
td.run()
