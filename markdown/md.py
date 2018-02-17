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
    <section>
        <p style="text-align: right; font-size: 11px;"> you are on <a href="/index.html" class="cool-link">coolguy.website</a> enjoy more <a href="index.html" class="cool-link">writing</a></p>
    </section>
    <div style="width: 85%; margin: 70px 0 40px 40px;">
        <div class="titlebox-entry">
            <div class="titlebox-left-entry">
            </div>
            <div class="titlebox-right-entry">
"""
print "            <p class=\"subtitle\">%s</p>" % title
print """\
            </div>
        </div>
        <div class="thepiece">
"""
post = markdown.markdownFromFile(path);
print """\ 
        </div>
    </div>
</body>
"""
