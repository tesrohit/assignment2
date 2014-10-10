__author__ = 'ROHIT'

fr = open("student.csv","r")
fw = open("student.xml","w")

str = "\""
str1 = ","
fw.write("<Students>" + "\n")


for line in fr:
    line = line.split(str)
    fw.write("<student>" + "\n")
    fw.write("<id>" + "\n")
    words = line[1]
    words = words.split(str1)
    if words.__len__() == 5:
        fw.write("<year>" + " ")
        fw.write(words[0])
        fw.write("</year>" + "\n")
        fw.write("<branch1>" + " ")
        fw.write(words[1])
        fw.write("</branch1>" + "\n")
        fw.write("<branch2>" + " ")
        fw.write(words[2])
        fw.write("</branch2>" + "\n")
        fw.write("<ps_ts>" + " ")
        fw.write(words[3])
        fw.write("</ps_ts>" + "\n")
        fw.write("<no>" + " ")
        fw.write(words[4])
        fw.write("</no>" + "\n")

    elif words.__len__() == 4:
        fw.write("<year>" + " ")
        fw.write(words[0])
        fw.write("</year>" + "\n")
        fw.write("<branch1>" + " ")
        fw.write(words[1])
        fw.write("</branch1>" + "\n")
        fw.write("<ps_ts>" + " ")
        fw.write(words[2])
        fw.write("</ps_ts>" + "\n")
        fw.write("<no>" + " ")
        fw.write(words[3])
        fw.write("</no>" + "\n")
    else:
        print "Incorrect file format"
        fr.close()
        fw.close()
        exit(0)
    fw.write("</id>" + "\n")

    words = line[3]
    words = words.split(str1)
    fw.write("<Name>" + "\n")
    if words.__len__() == 2:
        fw.write("<first_name>" + " ")
        fw.write(words[0])
        fw.write("</first_name>" + "\n")
        fw.write("<last_name>" + " ")
        fw.write(words[1])
        fw.write("</last_name>" + "\n")
    elif words.__len__() == 3:
        fw.write("<first_name>" + " ")
        fw.write(words[0])
        fw.write("</first_name>" + "\n")
        fw.write("<middle_name>" + " ")
        fw.write(words[1])
        fw.write("</middle_name>" + "\n")
        fw.write("<last_name>" + " ")
        fw.write(words[2])
        fw.write("</last_name>" + "\n")
    fw.write("</Name>" + "\n")

    fw.write("<dob>" + "\n")
    fw.write(line[5])
    fw.write("</dob>" + "\n")

    fw.write("<cgpa>" + "\n")
    fw.write(line[7])
    fw.write("</cgpa>" + "\n")

    words = line[9]
    words = words.split(str1)
    fw.write("<contacts>" + "\n")
    fw.write("<Address>" + "\n")
    for i in range(words.__len__() -2):
        fw.write(words[i])
    fw.write("</Address>" + "\n")
    fw.write("<Emails>" + "\n")
    fw.write("<primary>")
    fw.write(words[words.__len__() - 2])
    fw.write("</primary>" + "\n")
    fw.write("</Emails>" + "\n")
    fw.write("<mobile>")
    fw.write(words[words.__len__() - 1])
    fw.write("</mobile>" + "\n")
    fw.write("</contacts>" + "\n")

    words = line[11]
    words = words.split(str1)
    fw.write("<pre_requisites>" + "\n")
    fw.write("<courses>" + "\n")
    fw.write("<c_programming>")
    fw.write(words[0])
    fw.write("</c_programming>" + "\n")
    fw.write("<OOP>")
    fw.write(words[1])
    fw.write("</OOP>" + "\n")
    fw.write("<machine_learning>")
    fw.write(words[2])
    fw.write("</machine_learning>" + "\n")
    fw.write("<data_mining>")
    fw.write(words[3])
    fw.write("</data_mining>" + "\n")
    fw.write("<no_sql>")
    fw.write(words[4])
    fw.write("</no_sql>" + "\n")
    fw.write("<xml>")
    fw.write(words[5])
    fw.write("</xml>" + "\n")
    fw.write("<json>")
    fw.write(words[6])
    fw.write("</json>" + "\n")
    fw.write("</courses>" + "\n")

    fw.write("<tools>" + "\n")
    fw.write("<pycharm>")
    fw.write(words[7])
    fw.write("</pycharm>" + "\n")
    fw.write("<git_hub>")
    fw.write(words[8])
    fw.write("</git_hub>" + "\n")
    fw.write("<mongo_db>")
    fw.write(words[9])
    fw.write("</mongo_db>" + "\n")
    fw.write("</tools>" + "\n")
    fw.write("</pre_requisites>" + "\n")

    fw.write("</student>" + "\n")

'for words in line:'
'print words'
fw.write("</Students>")
fr.close()
fw.close()
