# Upper
kata = 'dicoding'
kata = kata.upper()
print(kata)

"""
Output:
DICODING
"""

# Lower
kata = 'DICODING'
kata = kata.lower()
print(kata)

"""
Output:
dicoding
"""

#rstrip
print("Dicoding          ".rstrip())

"""
Output:
Dicoding
"""

#lstrip
print("           Dicoding".lstrip())

"""
Output:
Dicoding
"""

#strip
print("         Dicoding          ".strip())

"""
Output:
Dicoding
"""

#Jika ingin menghilangkan karakter selain whitespace, Anda bisa mengikuti contoh berikut.
kata = 'CodeCodeDicodingCodeCode'
print(kata.strip("Code"))

"""
Output:
Dicoding
"""

# startswith()
print('Dicoding Indonesia'.startswith('Dicoding'))

"""
Output:
True
"""