def exportMajors(majors, fileName):
  with open(fileName, 'w') as f:
    f.write("{\n")
    for item in majors:
      key, spelled = item.split("-", 1)
      spelled = spelled.strip()
      key = key.strip()
      f.write("\t%s\n" % f'"{spelled}": "{key}",')
    f.write("}")

