#/usr/bin/python
#
# HTTP server with a HTML form that allows to upload files to the server.
# Files are stored in a folder named "files" inside the current directory.

from os import curdir
from os.path import join as pjoin

from http.server import BaseHTTPRequestHandler, HTTPServer

from cgi import FieldStorage


upload_form = """
<html><body>
<form enctype="multipart/form-data" method="post">
<p>File: <input type="file" name="file"></p>
<p><input type="submit" value="Upload"></p>
</form>
</body></html>
"""


class StoreHandler(BaseHTTPRequestHandler):
    target_folder = pjoin(curdir, "files")

    def do_GET(self):
        if self.path == "/":
            self.display_form()

    def do_POST(self):
        if self.path == "/":
            form = FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={
                    "REQUEST_METHOD": "POST",
                    "CONTENT_TYPE": self.headers["Content-Type"],
                }
            )
            filename = form["file"].filename
            data = form["file"].file.read()
            fpath = pjoin(self.target_folder, filename)
            open(fpath, "wb").write(data)

            self.display_form()

    def display_form(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(upload_form.encode())


server = HTTPServer(("", 1337), StoreHandler)
print("listening on 0.0.0.0:1337")
server.serve_forever()
