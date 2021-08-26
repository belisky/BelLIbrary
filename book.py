class Book:
    def __init__(self,id,name,description,isbn,page_content,issued,author,year):
        self.id=id
        self.description=description
        self.isbn=isbn
        self.name=name
        self.page_content=page_content
        self.issued=issued
        self.author=author
        self.year=year

    # To_dict method
    def to_dict(self):
        dictionary= {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'isbn': self.isbn,
            'page_content': self.page_content,
            'issued': self.issued,
            'author': self.author,
            'year': self.year,
        }

        return dictionary
book1=Book(32,'atomic things','build things','213--52--325--23',342,True,'bello bel',2018)
print(book1.to_dict())