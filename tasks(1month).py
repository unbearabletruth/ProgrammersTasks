class Task:
    id = 0

    def __init__(self, description, programmer, workload):
        Task.id += 1
        self.id = Task.id
        self.description = description
        self.programmer = programmer
        self.workload = workload
        self.finished = "Not Finished"

    def coder(self):
        return self.programmer

    def get_id(self):
        return self.id

    def work_hours(self):
        return self.workload

    def is_finished(self):
        if self.finished == "Not Finished":
            return False

        elif self.finished == "Finished":
            return True

    def mark_finished(self):
        self.finished = "Finished"
        return self.finished

    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.finished}"


class OrderBook:

    def __init__(self):
        self.orders = []

    def add_order(self, description, programmer, workload):
        self.orders.append(Task(description, programmer, workload))

    def all_orders(self):
        return self.orders

    def programmers(self):
        coders = []
        for task in self.orders:
            coders.append(task.coder())

        return list(set(coders))

    def id(self):
        ids = []
        for task in self.orders:
            ids.append(task.get_id())

        return list(set(ids))

    def mark_finished(self, id: int):
        for order in self.orders:
            if order.id == id:
                Task.mark_finished(order)

    def finished_orders(self):
        finished = []
        for order in self.orders:
            if order.is_finished():
                finished.append(order)
        return finished

    def unfinished_orders(self):
        unfinished = []
        for order in self.orders:
            if order.is_finished() is False:
                unfinished.append(order)
        return unfinished

    def status_of_programmer(self, programmer: str):
        #if programmer not in self.programmers():
            #raise ValueError("No coder with such name")
        finished_count = 0
        unfinished_count = 0
        f_workload = 0
        uf_workload = 0
        for finished in self.finished_orders():
            if finished.coder() == programmer:
                finished_count += 1
                f_workload += finished.work_hours()

        for unfinished in self.unfinished_orders():
            if unfinished.coder() == programmer:
                unfinished_count += 1
                uf_workload += unfinished.work_hours()

        return finished_count, unfinished_count, f_workload, uf_workload


class Interface:

    def __init__(self):
        self.order = OrderBook()

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def add(self):
        description = input("tasks description:")
        try:
            programmer, workload = input("programmer and workload estimate separated by space:").split()
            self.order.add_order(description, programmer, int(workload))
            print("added!")
        except:
            print("erroneous input")

    def finished(self):
        if len(OrderBook.finished_orders(self.order)) == 0:
            print("no such tasks")
        for task in OrderBook.finished_orders(self.order):
            print(task)

    def unfinished(self):
        if len(OrderBook.unfinished_orders(self.order)) == 0:
            print("no such tasks")
        for task in OrderBook.unfinished_orders(self.order):
            print(task)

    def mark_finished(self):
        try:
            id = int(input("at what id? "))
        except:
            print("erroneous input")
        else:
            OrderBook.mark_finished(self.order, id)
            print("marked as finished")

    def get_coders(self):
        for coder in OrderBook.programmers(self.order):
            print(coder)

    def status(self):
        coder = input("Whose status do you want to see? ")
        if coder not in OrderBook.programmers(self.order):
            print("erroneous input")
        else:
            print(f"finished {OrderBook.status_of_programmer(self.order, coder)[0]}"
                  f" not finished {OrderBook.status_of_programmer(self.order, coder)[1]},"
                  f" hours: done {OrderBook.status_of_programmer(self.order, coder)[2]}"
                  f" scheduled {OrderBook.status_of_programmer(self.order, coder)[3]}")

    def execute(self):
        self.help()
        while True:
            command = input("what to do? ")
            if command == "0":
                break
            elif command == "1":
                self.add()
            elif command == "2":
                self.finished()
            elif command == "3":
                self.unfinished()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.get_coders()
            elif command == "6":
                self.status()
            else:
                print("No such command")


app = Interface()
Interface.execute(app)