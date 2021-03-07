from http.server import HTTPServer
from argparse import ArgumentParser

from .server import SkiRequestHandler


def get_args():
    parser = ArgumentParser()
    parser.add_argument('-p', "--port", help="Specify alternate port [default: 8000]", type=int, default=8000)

    return parser.parse_args()


def main():
    args = get_args()

    server = HTTPServer(("localhost", args.port), SkiRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
