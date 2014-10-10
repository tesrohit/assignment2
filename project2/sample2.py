__author__ = 'ROHIT'

from xmlutils.xml2json import xml2json

converter = xml2json("student1.xml", encoding="utf-8")

fjson = open("student.json","w")

'sorted(converter.get_json())'
fjson.write(converter.get_json(pretty=True))
fjson.close()