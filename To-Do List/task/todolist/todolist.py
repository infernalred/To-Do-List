from sqlalchemy import create_engine

engine = create_engine('sqlite:///file_name?check_same_thread=False')


class ToDo:
    def __init__(self):
        self.today_list = ["Do yoga", "Make breakfast",
                           "Learn basics of SQL", "Learn what is ORM"]

    def run(self):
        i = 1
        print("Today:")
        for task in self.today_list:
            print(f"{i}) {task}")
            i += 1

td = ToDo()
td.run()
