__author__ = 'ROHIT'

from xmlutils.xml2json import xml2json

converter = xml2json("student.xml", encoding="utf-8")

fjson = open("student.json","w")

fjson.write(converter.get_json(pretty=True))
fjson.close()