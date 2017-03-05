import random

def Political():
	stories = [" new laws regarding ", " the muslim ban.", " recent developments in ", " develpoments in "]
	places = ["", " the White House", " Buckingham Palace", " Moscow", " Beijing",  " in the South China Sea", " in Palistine", " in Greece", " in the EU"]
	issues = ["", " education issues.", " the economy", " the wage gap", " climate change"]
	nouns_political = ["", "Trump ", "The Queen of England ", "Putin ", "Xi Jinping "]
	verbs = ["attacks ", "invites ", "calls out ", "requests ", "mentions "]
	First_person= random.randint(1,len(nouns_political)-1)
	action = random.randint(0,len(verbs)-1)
	z = ""
	placeRan = 0
	location = ""
	Second_Person= random.randint(1,len(nouns_political)-1)
	while Second_Person is First_person:
		Second_Person= random.randint(1, len(nouns_political)-1)
	time = 0
	timeStr = ""
	issueRan = random.randint(1, len(issues)-1)

	if action is 0 :
		z = " over"
		if issueRan is 1:
			 place =0
		else:
			placeRan = random.randint(len(nouns_political), len(places)-1)
			location = "working"
	if action is 1:
		z = "to"
		dis = random.randint(0,1)
		if dis is 1:
			z+= " discuss"
			if issueRan is 1:
			 		place =0
			else:
					placeRan = random.randint(1, len(places)-1)
					location = "working"
		if dis is 0:
			issueRan = 0
			placeRan = First_person

	if action is 2:
		placeRan = 0;
		reason = random.randint(0,2)
		if reason is 0 and First_person is 1:
			z = "on Twitter over"
			time = random.randint(1,4)
			timeStr = " at " + str(time) + ":00 am"
	if action is 3:
		z = "to visit"
	if action is 4:
		z = "in press confrence about"
	return (nouns_political[First_person] + verbs[action] + nouns_political[Second_Person] + z + issues[issueRan] + places[placeRan] + timeStr)

print(Main())