name ="Data Engineering"
sprint="first sprint"

print(name)
print(name.lower())
print(name.upper())
print(name.count('e'))
print(name.find('ring'))
print(name.replace('Data','Software'))

version=name+' '+sprint
version='{}  ,{}'.format(name,sprint)
version =f'{name}  ,{sprint}'
print(version)


print(dir(name))
