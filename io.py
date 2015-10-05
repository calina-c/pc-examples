# -*- coding: utf-8 -*-

# ~~~~~~~~~~ 3.3 ~~~~~~~~~~ #
# >>> chr(77)
# 'M'
# observe that it is a letter
# >>> chr(22222)
# '囎'
# in Python, chr() acts also as unichr and extends to Unicode characters
# what happens in C?

# ~~~~~~~~~~ 3.4 ~~~~~~~~~~ #
for i in range(65, 90):
    print(chr(i)),
for i in range(97, 122):
    print(chr(i)),
# OUTPUTS:
# A B C D E F G H I J K L M N O P Q R S T U V W X Y a b c d e f g h i j k l m n o p q r s t u v w x y

# # ~~~~~~~~~~ 3.5 ~~~~~~~~~~ #
# for i in range(32, 126):
    print(chr(i)),
# OUTPUTS:
#   ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | }

# # ~~~~~~~~~~ 3.6 ~~~~~~~~~~ #
arr = ['a', 'b', 'a', 'j', 'u', 'r', '\n', 'p', 'e', '\n', 'm', 'a', 's', 'a']
print("".join(arr))
# in Python, lists of characters are not automatically represented as strings
# OUTPUTS:
# abajur
# pe
# masa

# # ~~~~~~~~~~ 3.7 ~~~~~~~~~~ #
arr = ['a', 'b', 'a', 'j', 'u', 'r', '2', 'A']
# reading left as an exercise to the reader
d = ord('a') - ord('A')
for i in arr:
    if ord(i) in range(97, 122):
        print(chr(ord(i) - d)),
# OUTPUTS:
# A B A J U R

# # ~~~~~~~~~~ 3.8 ~~~~~~~~~~ #
arr = ['A', 'B', 'A', 'J', 'U', 'R', '2', 'a']
# reading left as an exercise to the reader
d = ord('a') - ord('A')
for i in arr:
    if ord(i) in range(65, 90):
        print(chr(ord(i) + d)),
# OUTPUTS:
# a b a j u r

# # ~~~~~~~~~~ 3.9 ~~~~~~~~~~ #
x = 12
y = 4
# reading left as exercise to the reader
print '{0:5} {1:5} {2:10} {3:10} {4:10} {5:10}'.format(
    'x',
    'y',
    'x + y',
    'x - y',
    'x * y',
    'x // y',
)
print '{0} {1:5} {2:10} {3:10} {4:10} {5:10}'.format(
    x,
    y,
    x + y,
    x - y,
    x * y,
    x / y
)
# OUTPUTS:
# x     y     x + y      x - y      x * y      x // y
# 12     4         16          8         48          3


# # ~~~~~~~~~~ 3.10 ~~~~~~~~~~ #
import math
print 'The value of PI is approximately {0:.3f}.'.format(math.pi)
# OUTPUTS:
# The value of PI is approximately 3.142.

# # ~~~~~~~~~~ 3.11 ~~~~~~~~~~ #
x = 255
# reading left as exercise to the reader
print(hex(x))
print(oct(x))
# OUTPUTS:
# 0xff
# 0377
