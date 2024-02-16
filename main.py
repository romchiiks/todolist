class BD():   #аналог бд
    categories = [{'id': 0, 'name': 'homework'},
                      {'id': 1, 'name': 'pisiwork'},
                      {'id': 2, 'name': 'romaworks'},
                      {'id': 3, 'name': 'penisworks'}]
    task = [{'name': 'make app', 'category': 2, 'sost': 0},
            {'name': 'make app1', 'category': 0, 'sost': 1},
            {'name': 'make app2', 'category': 1, 'sost': 0},
            {'name': 'make app3', 'category': 3, 'sost': 1},
            {'name': 'make app4', 'category': 1, 'sost': 1}]

class Main():
    def main(self):
        #заглушка вместо бд
        self.editcategories(BD.categories)#вызов функции редактирования категорий

    def editcategories(self, list1):#функция редактирования категорий
            if list1 != []:#если список категорий не пустой(используется заглушка)
                for cats in list1:#вывод названий категорий (cats) через ключ (name)
                    print(f"({cats['id'] + 1}) {cats['name']}")
                print(f'\n(+) Add Category')#выбор дальнейшего действия
                selecter = input()
                if selecter != '+':
                    if int(selecter) in range(len(list1)):
                        self.tasksShow(int(selecter))#здесь передается селектер, который является id категории в цикле
                else:
                    self.inputCat(list1)

            else: #в случае, если бд пустая (т.е. при первом запуске программы/после удаления всего)
                n = input('1. Add Category' + '\n')#доступно только добавить категорию, позже надо будет реализовать с запросом и бдшкой
                if n == '1':
                    self.inputCat(list1)

    def inputCat(self, list1):#внесение категории в бд путем добавления в лист, в дальнейшем просто запросы INSERT
        new = input('Category name?' + '\n')
        list1.append(new)#(вот тут INSERT)
        self.editcategories(list1)
        
    def tasksShow(self, id):
        for i in BD.task:
            if i['category'] == id:
                print(i['name'])
            else:
                pass       

    def killCat(self, list1):#удаление категории(не работает)
        counter = 1
        print('Existing categories: ')
        for cats in list1:
            print(f'{counter}. {cats}') 
        catkiller = input('Which one?' + '\n')
        try:
            list1.pop(int(catkiller)-1)
            self.editcategories(list1)
        except:
            print('Wrong values')
            self.editcategories(list1)

    def inputTasks(dict):
        k = 0
        print('input tasks')
        while True:
            task = input()
            if task != 'break':
                dict[k] = task
                k+=1
            else:
                break 

if __name__ == "__main__":
    a = Main()
    a.main()