class book:
    book_list =['java','Ai','ML','py']
    def __init__(self,title,description,author,status):
        self.title = title
        self.description = description
        self.author = author
        self.status = status
    def displayAvaliableBook(self):
        print:('Books present in thi library are :')
        for title in book_list:
            print(title)