# 새로 import 하는 모듈
from django.db import connection

"""
def BookListView(request):
    # books = Book.objects.all()
    try:
        cursor = connection.cursor()

        strSql = "SELECT code, name, author FROM bookstore_book"
        result = cursor.execute(strSql)
        books = cursor.fetchall()

        connection.commit()
        connection.close()

    except:
        connection.rollback()
        print("Failed selecting in BookListView")


    return render(request, 'book_list.html', {'books': books}

"""