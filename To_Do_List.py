class todolist:
    def __init__(self):
        self.tasks=[]
    def addtasks(self,task):
        self.tasks.append(task)
    def deletetask(self,index):
        if index>0 and index<=len(self.tasks):
            self.tasks.pop(index-1)
        else:
            print("Invalid task index")
    def showtasks(self):
        for i,task in enumerate(self.tasks):
            print(f'{i+1}.{task}')
    def markascomplete(self,index):
        if 0 < index <= len(self.tasks):
            self.tasks[index-1] += " (Completed)"
        else:
            print("Invalid task index")
def main():
    obj=todolist()
    while True:
        print('choose the optoins below')
        print("1.Add a task \n2.Delete a task \n3.Mark as Completed \n4.Show the tasks\n5.Exit\n")
        ch=int(input())
        if ch==1:
            print()
            task=input('Enter the task : ')
            obj.addtasks(task)
            print('Task added.')
        elif ch==2:
            print()
            if not obj.tasks:
                print('No tasks available to delete')
                continue
            else:
                obj.showtasks()
                index=int(input('Enter the index of the task that you want to delete = '))
                obj.deletetask(index)
        elif ch==3:
            print()
            if not obj.tasks:
                print('No tasks available')
                continue
            obj.showtasks()
            index=int(input('Enter the index of the task that you want to Mark as completed = '))
            obj.markascomplete(index)
        elif ch==4:
            print()
            if not obj.tasks:
                print('No tasks available')
                continue
            obj.showtasks()
        elif ch==5:
            print()
            print('Exiting.....')
            break
        else:
            print()
            print('Choose the correct option')
    main()