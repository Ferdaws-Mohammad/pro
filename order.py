class order:
    book_list =['java','Ai','ML','py']
    list_order=[]
    id_order=0
    status='active'
    def __init__(self,name_book):

     def borrow_book(self, name_book):
         if name_book in book_list:
             statue='active'
             id_order +=1
             book_list.remove(name_book)
             list_order.append(name_book)