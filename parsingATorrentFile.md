# Parsing a .torrent file 

The first thing a client needs to do is to find out what it is supposed to download and from whre. This information is what is stored in the `.torrent` file, a.k.a _meta-info_. There is a number of properties stored i nthe _meta-info_ that we need in order to successfully implement a client.

Things like: 
	- The name of the file to download
	- The size of the file to download
	- The URL to the tracker to connect to 

All these properties are stored in a binary format called _Bencoding_.

Bencoding supports four different data types, dictionaries, lists, intergers and _strings_ it is fairly easy to translate to Python's _object literals_ or JSON. 

Below is bencoding described in *Augmented Back-naur Form* courtesey of the *Haskell library*.

```json
<BE>    ::= <DICT> | <LIST> | <INT> | <STR>

<DICT>  ::= "d" 1 * (<STR> <BE>) "e"
<LIST>  ::= "l" 1 * <BE>         "e"
<INT>   ::= "i"     <SNUM>       "e"
<STR>   ::= <NUM> ":" n * <CHAR>; where n equals the <NUM>

<SNUM>  ::= "-" <NUM> / <NUM>
<NUM>   ::= 1 * <DIGIT>
<CHAR>  ::= %
<DIGIT> ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"
```

In _pieces_ the encoding and decoding of _bencoded_ data is implementes in the _pieces.bencoding_ module

Here are a few examples decoding bencoded data into a Python representation using that module. 

```python
>>> from pieces.bencoding import Decoder

# An integer value starts with an 'i' followed by a series of
# digits until terminated with a 'e'.
>>> Decoder(b'i123e').decode()
123

# A string value, starts by defining the number of characters
# contained in the string, followed by the actual string.
# Notice that the string returned is a binary string, not unicode.
>>> Decoder(b'12:Middle Earth').decode()
b'Middle Earth'

# A list starts with a 'l' followed by any number of objects, until
# terminated with an 'e'.
# As in Python, a list may contain any type of object.
>>> Decoder(b'l4:spam4:eggsi123ee').decode()
[b'spam', b'eggs', 123]

# A dict starts with a 'd' and is terminated with a 'e'. objects
# in between those characters must be pairs of string + object.
# The order is significant in a dict, thus OrderedDict (from
# Python 3.1) is used.
>>> Decoder(b'd3:cow3:moo4:spam4:eggse').decode()
OrderedDict([(b'cow', b'moo'), (b'spam', b'eggs')])
```
