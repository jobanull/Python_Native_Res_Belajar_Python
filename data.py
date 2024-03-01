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