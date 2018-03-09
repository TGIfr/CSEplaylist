from urllib import request, error
from functools import reduce
from io import BytesIO
from mutagen.mp3 import MP3


def get_genre(song_url):

    def get_n_bytes(song_url, byte_len):
        req = request.Request(song_url)
        req.headers["Range"] = "bytes=%s-%s" % (0, byte_len - 1)
        response = request.urlopen(req)
        return response.read()

    data = ""
    try:
        data = get_n_bytes(song_url, 10)
    except (error.HTTPError, error.URLError):
        print("OOps! Doesn't seem to exist")
        return "Unknown"
    if "ID3" not in data[0:3].decode("ascii"):
        print(data)
        raise Exception("ID3 not in front of mp3 file")

    size_encoded = bytearray(data[-4:])
    size = reduce(lambda a, b: a * 128 + b, size_encoded, 0)

    header = BytesIO()
    # mutagen needs one full frame in order to function. Add max frame size
    data = get_n_bytes(song_url, size + 2881)
    header.write(data)
    header.seek(0)
    f = MP3(header)
    # print(data)
    # print(f.tags)

    if f.tags and "TCON" in f.tags.keys():
        return f.tags["TCON"].text
    return "Unknown"
