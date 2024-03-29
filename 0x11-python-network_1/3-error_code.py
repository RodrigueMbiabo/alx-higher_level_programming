#!/usr/bin/python3
""" Script that takes in a URL, sends a request to the URL and
displays the body of the response """
if __name__ == "__main__":
    from urllib import request, error
    import sys
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
