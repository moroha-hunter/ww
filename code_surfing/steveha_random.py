#https://stackoverflow.com/questions/14720799/how-to-get-numbers-from-dev-random-using-python
#By user https://stackoverflow.com/users/166949/steveha
import os
import struct

_random_source = open("/dev/random", "rb")

def random_bytes(len):
    return _random_source.read(len)

def unpack_uint32(bytes):
    tup = struct.unpack("I", bytes)
    return tup[0]

UINT32_MAX = 0xffffffff
def randint(low, high):
    """
    Return a random integer in the range [low, high], including
    both endpoints.
    """
    n = (high - low) + 1
    assert n >= 1
    scale_factor = n / float(UINT32_MAX + 1)
    random_uint32 = unpack_uint32(random_bytes(4))
    result = int(scale_factor * random_uint32) + low
    return result

def randint_gen(low, high, count):
    """
    Generator that yields random integers in the range [low, high],
    including both endpoints.
    """
    n = (high - low) + 1
    assert n >= 1
    scale_factor = n / float(UINT32_MAX + 1)
    for _ in range(count):
        random_uint32 = unpack_uint32(random_bytes(4))
        result = int(scale_factor * random_uint32) + low
        yield result

if __name__ == "__main__":
    # roll 3 dice individually with randint()
    result = [randint(1, 6) for _ in range(3)]
    print(result)

    # roll 3 dice more efficiently with randint_gen()
    print(list(randint_gen(1, 6, 3)))
    print(randint(1,900000000000000))
