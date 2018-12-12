# Partner 1: Mia
# Partner 2: Mitchell
''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''
 
''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''
if grade == A:
   print("Good Work!")
 
 
''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
if yards < 17:
   yards *= 2
 
''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''
if success == True:
   print("Congratulations!")
 
 
''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
if word[1] == 'f':
   print("fun")
 
 
''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''
if celsius:
   temp = 1.8*celsius + 32
 
 
''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
if numItems <= 0:
   print("no items")
else: 
   averageCost = totalCost/numItems
   print(averageCost)
 
''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''
if pollution < cutoff:
   print("safe condition")
else:
   print("unsafe condition")
 
''' 8. 
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69 C: 70=79 A: 90-100

''' 
if score < 60:
   grade = "F"
elif score <70: 
   grade = "D"
elif score <80:
   grade = "C"
elif score < 90:
   grade = "B"
else:
   grade = "A"
'''9:
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''
if letter.islower():
   print("lowercase")
elif letter.isupper():
   print("uppercase")
elif letter.isdigit():
   print("digit")
else:
   print("symbol")
 
 
''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''
if neighbors >= 50:
   print("city")
elif neighbors >= 25:
   print("suburbia")
elif neighbors >= 1:
   print("rural")
elif neighbors == 0:
   print("middle of nowhere")
 
 
''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''
if makesBreakthrough and doesSignificantWork:
   nobelPrizeCanidate == True
else:
   nobelPrizeCanidate == False
 
 
''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''
if Tax == True:
   price = price + (taxRate * price)

 
 
''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
if word[-1] == "y" and word[-2] == "l":
   print("adverb")
elif word[-1] == "g" and word[-2] == "n" and word[-3] == "i":
   print("gerund")
elif word[-1] == "s":
   print("plural")
else:
   print("error")
 
 
''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''
if currentNumber%2 == 1:
   currentNumber = (currentNumber+1)*3
else:
   currentNumber = int(currentNumber/2)
 
''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''
 if year%4 == 0:
   if year%100 == 0:
      if year%400 == 0:
         leapYear = True
      else:
         leapYear = False
   else:
      leapYear = True
 
 
''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
if a-b > 0:
   if b-c > 0:
      result = c
   else:
      result = b
else:
   if a-c > 0:
      result = c
   else:
      result = a
 
''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
if number%2 == 0 and number%5 == 0 and number>=(-100) and number<=100:
   special = True
else:
   special = False
 
 
''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
if letter == "a" or letter = "e" or letter == "i" or letter == "o" or letter == "u":
   code = 1
elif letter == "y":
   code = -1
else:
   code = 0

 
''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
if dayOfWeek == "Sunday" or dayOfWeek == "Saturday":
   isWeekend = True
else:
   isWeekend = False
 
 
''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
 if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
   numDays = 31
elif month == "April" or month == "September" or month == "June" or month == "September" or month == "November":
   numDays = 30
elif month =="February":
   numDays = 28
''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
if angle1 + angle2 + angle3 == 180:
   validTriangle = True
else:
   validTriangle = False
 
 
''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
if electricity <= 50:
   payment = 0.5*electricity
elif electricity <= 150:
   payment = 0.75*electricity
elif electricity <= 250:
   payment = 1.2*electricity
else:
   payment = (1.5*electricity)*1.2
 
 
''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
if language =="English":
   greeting = "Hello"
elif language == "French":
   greeting = "Bonjour"
elif language == "Spanish":
   greeting = "Hola"
else:
   greeting = ":)"
 
 
''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''
phrase = str(number)+noun
print("number: "+str(number)+"; noun: "+noun+"; phrase: "+phrase)
  
 
''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''
 if userInput == "bacon":
   print("Why did you type bacon?")
else: 
   print("I like bacon")
 
''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''
 
''' Task 1:
   If isBroken, a boolean, is true, print "Call the mechanic". If isBroken is false, print "Business as usual" 
'''
if isBroken:
   print("Call the mechanic")
else:
   print("Business as usual")
 
 
 
''' Task 2:
If integer requiredSugar is greater than integer suppliedSugar, print "I need to borrow a cup of sugar", otherwise print "perfect!"
'''
 
if requiredSugar > suppliedSugar:
   print("I need to borrow a cup of sugar")
else:
   print("perfect!")
 
 
 
''' Task 3:
 if number is a multiple of 7 and a multiple of 5, set String sevenFives to "sevens and fives". If it's only a multiple of 7, set String sevenFives to "sevens". If it's only a multiple of 5, set sevenFives to "fives". Otherwise, set sevenFives to "false"

 solution
 '''
if number%7 == 0 and number%5 == 0:
   sevenFives = "sevens and fives"
elif number%7 == 0:
   sevenFives = "sevens"
elif numebr%5 == 0:
   sevenFives = "fives"
else:
   sevenFives = "false"
 
 
''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''