sos = []
for x in sos:
    if "щ" in x:
        a = x.replace(x[0:1], "щука")
        b = sos.index(x)
        sos.pop(b)
        sos.insert(b, a)
print(sos)
jjj = 'Птички щебечут %'
ass = jjj.find(" %")
tea = "Птички "
print(jjj[ass:])