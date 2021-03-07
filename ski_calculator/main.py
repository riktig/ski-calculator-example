from http.server import HTTPServer

from .server import SkiRequestHandler


def main():
    server = HTTPServer(("localhost", 8000), SkiRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
