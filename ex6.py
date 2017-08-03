x = "There are %d types of people in the world."%10
binary="binary"
do_not="do_not"
y="Those who knows %s and those who %s" %(binary,do_not)

print x
print y

print "I said %r," %x
print "I also said : '%s'."%y

hilarious =False
joke_evaluation="Isn't that joke so funny ?! %r"

print joke_evaluation %hilarious
w= "This is the left side of the..."
e= "a string with a rigth side."

print w+e
