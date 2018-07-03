# simply EX 16 from around page 59
# I've expanded the program myself to taken in
# however many lines the user wants
# this is of course done with a simple while loop
# and makes the program much more useful than the 
# hard coded 3 lines the book wanted me to type...

# run like this: python ex16_improved.py  test.txt
# and in your pwd you'll have a test.txt file with 
# your work in it!

from sys import argv

script, filename = argv

print "The file %r is going to be overwritten..." % filename
print "Back out now with: CTRL-C (^C)..."
print "Or onwards and upwards with: ENTER/RETURN..."

raw_input("?")

print "Loading the file..."
target = open(filename, 'w')

print "Truncating the file."
target.truncate()

#mod for asking how many lines are needed

num_of_lines = input("Enter number of lines you want: ")

i = 1

while i < num_of_lines + 1:
	#what I want looped
	s = str(i)
	line = raw_input("line %s : " % s) 
	target.write(line)
	target.write("\n")

	#debug statement
	#print(i)

	#increment with plus assgin 
	i += 1

print "Saving data...do not turn off the power"
print "Sucess!"

target.close()


