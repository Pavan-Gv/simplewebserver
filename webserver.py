from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My webserver</title>
</head>
<body>
<h1>Top 5 programming languages.</h1>
<h2>1. Python program</h2>
<h3>Python is a dynamically semantic, interpreted, object-oriented high-level programming language. Its high-level built-in data structures, together with dynamic typing and dynamic binding, making it ideal for Rapid Application Development and as a scripting or glue language for connecting existing components.</h3>
<br>
<h2>2. C programming language.</h2>
<h3>C is a widely used general-purpose programming language that is easy to learn and use. It is a machine-independent structured programming language that is widely used to create a variety of applications, operating systems such as Windows, and other complicated programmes such as the Oracle database, Git, Python interpreter, and others.</h3>
<br>
<h2>3. JAVA programming language.</h2>
<h3>Sun Microsystems first published Java in 1995 as a programming language and computing platform. It has grown from humble origins to power a significant portion of today's digital world by offering a secure platform on which many services and applications are built. Java is still used in new, innovative goods and digital services that are being developed for the future.</h3>
<br>
<h2>4. R language.</h2>
<h3>R is a statistical computing and graphics programming language and free software environment. The R Core Team and the R Foundation for Statistical Computing back it up. For designing statistical software and data analysis, it is commonly utilised by statisticians and data miners.</h3>
<br>
<h2>5. Javascript.</h2>
<h3>JavaScript is a cross-platform, object-oriented scripting language for creating dynamic web pages. There are also complex server-side JavaScript versions, such as Node.js, that allow you to add more functionality to a website than simply downloading files (such as realtime collaboration between multiple computers).</h3>
</body>
</html>
 """
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8080)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()