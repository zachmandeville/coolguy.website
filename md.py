import markdown
from sys import argv

script,title, path = argv
print "<!doctype html>\n<head>"
print "    <title>%s</title>" % title
print """\
    <link rel="stylesheet" type="text/css" href="/stylesheet.css">
    <link rel="stylesheet" media="screen" href="https://fontlibrary.org/face/interval" type="text/css"/>
</head>
<body>
"""
post = markdown.markdownFromFile(path);
print "</body>"

