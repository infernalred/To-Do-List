from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
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
        self.today_task = []
        self.list_menu = {1: "Today's tasks", 2: "Add task", 0: "Exit"}

    def menu(self):
        for k, v in self.list_menu.items():
            print(f"{k}) {v}")

    def print_today_task(self):
        print()
        print("Today:")
        self.today_task = session.query(Table).all()
        if len(self.today_task) == 0:
            print("Nothing to do!")
        else:
            i = 1
            for task in self.today_task:
                print(f"{i}. {task}")

    def task_add(self):
        print("Enter task")
        task = input()
        new_row = Table(task=task)
        session.add(new_row)
        session.commit()
        print("The task has been added!")

    def run(self):
        while True:
            self.menu()
            choose = input()
            if choose == "1":
                self.print_today_task()
            elif choose == "2":
                self.task_add()
            elif choose == "0":
                break


td = ToDo()
td.run()
