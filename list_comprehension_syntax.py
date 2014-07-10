####################################################
### List comprehension syntax exercises          ###
### Exercises from Codecademy Python track.      ###
### http://www.codecademy.com/en/tracks/python   ###
####################################################

# List including doubles of numbers between 1-5 divisible by three
doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0]

# List including squares of even numbers between 1-11
even_squares = [x**2 for x in range(1,12) if x % 2 == 0]

# List including all numbers between 1-100 divisible by 2 and 3
by_two_three = [x for x in range(1,101) if x % 2 == 0 and x % 3 == 0]

# List including all numbers between 1-100 not divisible by 5
no_five = [x for x in range(1,101) if x % 5 != 0]

# List including cubes of the numbers between 1-10 only if the cube is evenly divisible by four.
cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0 ]


print "Doubles by 3 (1-5)"
print doubles_by_3
print "\n"
print "Even squares (1-11)"
print even_squares
print "\n"
print "Divisible by 2 and 3 (1-100)"
print by_two_three
print "\n"
print "Not divisible by 5 (1-100)"
print no_five
print "\n"
print "Cubes divisible by 4 (1-10)"
print cubes_by_four
print "\n"


garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"

message = garbled[::-2]

print message