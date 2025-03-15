import zipfile
nen=zipfile.ZipFile('D:\\UNIVERSITY\\PY\\hello.zip','w')
nen.write('D:\\UNIVERSITY\\PY\\Chapter 2. Python Basics.pdf', compress_type=zipfile.ZIP_DEFLATED)
nen.close()