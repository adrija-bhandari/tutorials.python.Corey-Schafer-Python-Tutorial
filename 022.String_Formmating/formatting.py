#person = {'name': 'Jenn', 'age': 23}

#l = ['Jenn', 23]

#sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
#print(sentence)

#--------------------------------------------------------------------------

#sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
#print(sentence)

#----------------------------------------------------------------

#sentence = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
#print(sentence)

#-----------------------------------------------------------------------

#tag = 'h1'
#text = 'This is a headline'

#sentence = '<{0}>{1}</{0}>'.format(tag, text)
#print(sentence)

#-----------------------------------------------------------------

#sentence = 'My name is {0[name]} and I am {1[age]} years old'.format(person, person)
#print(sentence)

#------------------------------------------------------------

#sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
#print(sentence)

#--------------------------------------------------------------------

#sentence = 'My name is {0[0]} and I am {0[1]} years old'.format(l)
#print(sentence)

#-----------------------------------------------------------

#my big pranking plan for my parents

#class Person():

    #def __init__(self, name, age):
        #self.name = name
        #self.age = age

#p1 = Person('Swati', '90')
#p2 = Person('Nitesh', '100')

#sentence1 = 'My name is {0.name} and I am {0.age} years old'.format(p2)
#print(sentence1)

#sentence = 'My name is {0.name} and I am {0.age} years old'.format(p1)
#print(sentence)

#-----------------------------------------------------

#class Person():

    #def __init__(self, name, age):
        #self.name = name
        #self.age = age

#p1 = Person('Jack', '33')

#sentence = 'My name is {0.name} and I am {0.age} years old'.format(p1)
#print(sentence)

#---------------------------------------------------------------

#sentence = 'My name is {name} and I am {age} years old.'.format(name="Jenn", age="23")
#print(sentence)

#----------------------------------------------------------------

#sentence = 'My name is {name} and I am {age} years old.'.format(**person)
#print(sentence)

#------------------------------------------------------

#for i in range(1, 11):
    #sentence = 'The value is {:02}'.format(i)
    #print(sentence)

#---------------------------------------------------

#pi = 3.1415925

#sentence = 'Pi is equal to {:.2f}'.format(pi)
#print(sentence)

#------------------------------------------------

#sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
#print(sentence)

#--------------------------------------------------

#import datetime

#my_date = datetime.datetime(2020, 10, 7, 6, 31, 16)

#sentence = '{:%B %d, %Y}'.format(my_date)
#print(sentence)

#sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
#print(sentence)

#-------------------------------------------------------------------------------