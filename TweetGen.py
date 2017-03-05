import random

def Main():
	articleSelect = random.randint(0,1)
	if articleSelect is 0:
		return (getPolitical())
	if articleSelect is 1:
		return (getFunny())
def getFunny():
	animals = [" badger", " snake", " racoon", " squirrel", " Bigfoot?", " eagle", " shark!?!?!"]
	loc_connect = [ " into", " in", " into", " into", " onto"]
	location_funny= [" neighbor's house", " local pond", " ", " local elementary school", " the beach"]
	vehicles = [" drone", " car", " pickup truck", " bike"]
	funny = ""
	nationality = ["Florida", "Russian", "Utah", "New Jersey", "French", "Boston", "Ukrainian", "Trump supporter", "Indian", "Isreal"]
	nationalityRan = random.randint(0,len(nationality)-1)
	funny += nationality[nationalityRan]
	gender = [ " man", " woman"]
	genderRan = random.randint(0,len(gender)-1)
	funny += gender[genderRan]
	funny_action = [" arrested", " attacked by", " attacks", " crashes", " banned from"]
	funny_actionRan = random.randint(0,len(funny_action)-1)
	funny += funny_action[funny_actionRan]
	if funny_actionRan is 0:
		arrested1 = random.randint(0,1)
		if arrested1 is 0:
			funny += " for"
		if arrested1 is 1:
			funny += " after"
	if funny_actionRan is 1:	
		funny += animals[random.randint(0,len(animals)-1)]
	if funny_actionRan is 2:	
		funny += animals[random.randint(0,len(animals)-1)]
	if funny_actionRan is 3:
		funny += vehicles[random.randint(0,len(vehicles)-1)]
		locationRan = random.randint(0,len(location_funny)-1)
		funny += loc_connect[locationRan] + location_funny[locationRan]
	if funny_actionRan is 4:
		funny+= location_funny[random.randint(0,len(location_funny)-1)]


	return funny
def getPolitical():
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