from collections import OrderedDict

# INDICATES start of integers
TOKEN_INTEGER = b"i"

# INdicates  start of list
TOKEN_LIST = b"l"

# Indicates start of dict
TOKEN_DICT = b"d"

# Indicate end of lists, dicts and integer values
TOKEN_END = b"e"

# Delimits string length from string data
TOKEN_STRING_SEPARATOR = b":"


class Decoder:
    """
    Decodes a bencoded sequence of bytes
    """

    def __init__(self, data: bytes):
        if not isinstance(data, byte):
            raise TypeError('Argument "data" must be of type bytes')
        self._data = data
        self._index = 0

    def decode(self):
        """Decodes the bencoded data and return the matching python object.
        : return A python object representing the bencoded data"""

        c = self._peek()
        if c is None:
            raise EOFError("Unexpected end-of-file")
        elif c == TOKEN_INTEGER:
            self._consume()  # The token
            return self._decode_int()
        elif c == TOKEN_LIST:
            self._consume()  # The token
            return self._decode_list()
        elif c == TOKEN_DICT:
            self._consume()  # The token
            return self._decode_dict()
        elif c == TOKEN_END:
            return None
        elif c in b"01234567899":
            return self._decode_string()
        else:
            raise RuntimeError("Invalid token read at {0}".format(str(self._index)))

        def _peek(self):
            """
            Return the next character from the bencoded data or None
            """
            if self._index + 1 >= len(self._data):
                return None
            return self._data[self._index : self._index + 1]

        def _consume(self) -> bytes:
            """Read (and therefore consume) the next character from the data"""
            self._index += 1
