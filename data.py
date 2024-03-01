# Python is Loosely Typed. 
# Artinya, Anda tidak perlu mendeklarasikan tipe data variabel secara eksplisit.

age = 17 
salary = 30000.0

print(type(age))
print(type(salary))

"""
Output:
<class "int">
<class "float">
"""

# Dynamic Typing
# Artinya, Python adalah bahasa pemrograman yang hanya mengetahui tipe variabel saat program berjalan dan melakukan proses assignment. 
# Hal ini memungkinkan kita untuk mengubah tipe data dari suatu variabel seiring berjalannya program.

x = 6 
print(type(x))

x = "6"
print(type(x))


"""
Output:
<class "int">
<class "str">
"""
# Tipe Data
# Data Primitif
# Tipe data primitif pertama, yakni numbers adalah tipe data angka berupa bilangan bulat, riil, dan kompleks.

x = 6
print(type(x))

x = 6.0
print(type(x))

x = 1+2j
print(type(x))


"""
Output:
<class 'int'>
<class 'float'>
<class 'complex'>
"""

# Perlu diperhatikan bahwa tipe data numbers bersifat immutable yang artinya nilai di dalamnya tidak dapat diubah.

var = 10
print(var)
print(id(var))
var = 11
print(var)
print(id(var))

"""
Output:
10
<memory address>
11
<memory address>
"""

# Boolean
# Tipe data primitif kedua adalah boolean, yakni tipe data yang hanya bernilai TRUE atau FALSE. Tipe data ini merepresentasikan nilai kebenaran (truth values). 
# Sebenarnya, setiap variabel yang memiliki nilai bisa dievaluasi dan menghasilkan nilai true. Hanya ada beberapa nilai yang akan dianggap bernilai false sebagai berikut.

x = True
print(type(x))

x = False
print(type(x))

"""
Output:
<class 'bool'>
<class 'bool'>
"""

# String
# String merupakan karakter yang berurutan. Ketika Anda membuat variabel bernilai string tentu diawali dengan single quote (‘’) atau double quote (“”).

x = 'Dicoding'
print(type(x))

"""
Output: 
<class 'str'>
"""


# Anda dapat menggunakan tiga single quote atau double quote untuk menyimpan string yang lebih dari satu baris (multi-line).
multi_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.
"""

# String merupakan urutan karakter yang setiap karakternya memiliki indeks. 
# Anda dapat mengakses setiap karakter dari string (substring) dengan menggunakan metode indexing.

x = 'Dicoding'
print(x[0])

""" 
Output:
D
"""

# Anda dapat mengakses beberapa substring dengan menggunakan metode indexing dan slicing.

x = 'Dicoding'
print(x[2:])

"""
Output:
coding
"""

# Formatted String 

name = "Ikhdanul Joban"
print(f"Hello, nama saya {name}")
 
"""
Output: 
Hello, nama saya Ikhdanul Joban
"""

# %-Formatting
name = "Joban"
print("Nama saya %s" % (name))
 
"""
Output: 
Nama saya Joban
"""

# str.format()
name = "Ikhdan"
print("Nama saya {}".format(name))
 
"""
Output: 
Nama saya Ikhdan
"""

# Tipe Data Collection
# List
# List merupakan jenis kumpulan data terurut (ordered sequence) dan salah satu tipe data yang sering digunakan pada Python

x = [1, 2.2, 'Dicoding']
print(type(x))

"""
Output: 
<class "list">
"""

# Anda dapat mengakses setiap indeks pada list dengan metode indexing. 

x = [1, 'Dicoding', True, 1.0]

print(x[2])

""" 
Output:
True
"""

# List bersifat mutable (dapat diubah)
x = [1, 2.2, 'Dicoding']
x[0] = 'Indonesia'
print(x)

"""
Output:
['Indonesia', 2.2, 'Dicoding']
"""

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])


"""
Output:
laptop
mouse
microphone
keyboard
"""


x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']

"""


# Tuple
# Tuple adalah jenis dari list yang tidak dapat diubah elemennya.
x = (1, "Dicoding", 1+3j)
print(type(x))

"""
Output:
<class 'tuple'>
"""

# Tuple bersifat immutable yang artinya tidak dapat diubah.
x = (5, 'program', 1+3j)
# x[1] = 'Dicoding'

"""
Output:
'tuple' object does not support item assignment
"""

# Set 
# Set adalah kumpulan item bersifat unik, tanpa urutan (unordered collection), dan dapat diinisialisasikan dengan kurawal “{}” di mana setiap elemennya dipisahkan dengan koma.

x = {1,2,7,2,3,13,3}
# print(x[0])

"""
Output:
'set' object is not subscriptable
"""

x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>
"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1.union(set2)
print("Union:", union)

intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}

"""

# Dictionary
# Dictionary pada Python merupakan kumpulan pasangan key-value yang bersifat tidak berurutan.

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(type(x))

"""
Output:
<class 'dict'>
"""

# Kode akan menghasilkan error jika mencoba mengakses data pada dictionary dengan menggunakan metode indexing.

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

# print(x[0])

""" 
Output:
KeyError: 0
"""

# yang benar

x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }

print(x ['name'])

""" 
Output:
Perseus Evans
"""

# Menambah data pada Dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
x ['Job'] = "Web Developer"

print(x)

"""
Output:
{'name': 'Perseus Evans', 'age': 20, 'isMarried': False, 'Job': 'Web Developer'}
"""

# Menghapus data pada Dictionary
x = { 'name': 'Perseus Evans', 'age': 20, 'isMarried': False }
del x['isMarried']

print(x)

"""
Output:
{'name': 'Perseus Evans', 'age': 20}
"""