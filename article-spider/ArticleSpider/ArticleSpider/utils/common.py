
import hashlib

def get_md5(url):
    if isinstance(url, str):
        #  如果是 unicode 就对他进行 necode
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

if __name__ == '__main__':
    print(get_md5("http://jobbole.com".encode('utf-8')))