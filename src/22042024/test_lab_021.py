# Xpath Functions are used to handle dynamic elements
# i.e Elements that certain things changes,xpath functions are used

# if you don't have an idea of what types of tag it is, then you can use
# * i.e find all elements that corresponds e.g
# //*[@id='btn-make-wqass12132']. this simply means, find * where id=btnormakeorappointment
# //*[@id='btn-make-wqass12132']..*means all elements.from every elements find the id
#//a[@id='btn-make-wqass12132']..a is anchor tagname.this is better.from a tag,find the id
#//a[@id='btn-make-wqass12132']..fast xpath
#//*[@id='btn-make-wqass12132']..also known as wild card
# find id=btn-make-app in all TagNames. this is a  slow xpath
# another xpath function is Text
# //a [text()='Make Appointment']-> any elements where text is equal to Make Appointment
# partial text is used instead of text because text has some limitations like when
# there is a change in code, it affects the text but not in the case of partial text
# partial text used xpath function call contains
# Format of Partial Text are
# //a[contains(text(),'Make Appointment')]
# //a[contains(text(),'Appointment')]
# //a[contains(text(),'Ma')]
# //a[contains(text(),'App')]-This may fail if there is 1 or more a tags with App. so make sure the elements are unquie in nature

# another function is
# //a[starts-with(text(),'Make')]

# Xpath Attribute selectors
# //*[@id="id"]	?
# //*[@class="class"] …kinda
# //input[@type="submit"]
# //a[@id="abc"][@for="xyz"]	?
# //a[@rel] i.e relative attribute
# //a[starts-with(@href, '/')]	?
# //a[ends-with(@href, '.pdf')]
# //a[contains(@href, '://')]
# //a[contains(@rel, 'help')] …kinda
#####################################
# CSS Selector Attribute selectors
# # #id
# # .class
# # input[type="submit"]
# # a#abc[for="xyz"]
# # a[rel] i.e relative attribute
# # a[href^='/']
# # a[href$='pdf']
# # a[href*='://']
# # a[rel~='help']
