import twitter

# auth = twitter.oauth.OAuth('1100686363-6JxQIno5T8UMPQeWyaH783qrxxJJrmwbLJCEtoF', 'GqgnME3MRfOQL79TzWuH5S9fJOgXXogdAwyVDzGSk4ovD', 'mDkejxEBQYTj99RNkYhc1mCTE', 'WR2xlMAu4gRelaPRDkywDXCAGldZOZT6u4AymUBE0MpyjtooCg')

auth = twitter.oauth.OAuth('1100686363-fMLVUMcRav8V9lIGWEl5P2cAXLBnsaPZN3sbF7g', '4a7YvS6syULB3xe0h4MhmzfZQag6spC0mkf936BNaLyEP', '0zBKsSyl3R3gaP99ghAPumj91', '3LUtqtVmqTTjYJBHklEIQx38HTjsbhdICldDvq18Bggv5pgRFb')

twitter_api = twitter.Twitter(auth=auth)

world_woeid = 1
mumbai_woeid = 2295411
#delhi_woeid = 2295019
pune_woeid = 2295412
jaipur_woeid = 2295401
kolkata_woeid = 2295386
chennai_woeid = 2295424
bangalore_woeid = 2295420

world_trends = twitter_api.trends.place(_id=world_woeid)
mumbai_trends = twitter_api.trends.place(_id=mumbai_woeid)
#delhi_trends = twitter_api.trends.place(_id=delhi_woeid)
pune_trends = twitter_api.trends.place(_id=pune_woeid)
jaipur_trends = twitter_api.trends.place(_id=jaipur_woeid)
kolkata_trends = twitter_api.trends.place(_id=kolkata_woeid)
chennai_trends = twitter_api.trends.place(_id=chennai_woeid)
bangalore_trends = twitter_api.trends.place(_id=bangalore_woeid)


world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
mumbai_trends_set = set([trend['name'] for trend in mumbai_trends[0]['trends']])
#delhi_trends_set = set([trend['name'] for trend in delhi_trends[0]['trends']])
pune_trends_set = set([trend['name'] for trend in pune_trends[0]['trends']])
jaipur_trends_set = set([trend['name'] for trend in jaipur_trends[0]['trends']])
kolkata_trends_set = set([trend['name'] for trend in kolkata_trends[0]['trends']])
chennai_trends_set = set([trend['name'] for trend in chennai_trends[0]['trends']])
bangalore_trends_set = set([trend['name'] for trend in bangalore_trends[0]['trends']])

common_world_mumbai = world_trends_set.intersection(mumbai_trends_set)
#common_world_delhi = world_trends_set.intersection(delhi_trends_set)
common_world_pune = world_trends_set.intersection(pune_trends_set)
common_world_jaipur = world_trends_set.intersection(jaipur_trends_set)
common_world_kolkata = world_trends_set.intersection(kolkata_trends_set)
common_world_chennai = world_trends_set.intersection(chennai_trends_set)
common_world_bangalore = world_trends_set.intersection(bangalore_trends_set)

trends = {'World': world_trends_set, 'Mumbai': mumbai_trends_set, 'Pune': pune_trends_set, 'Jaipur': jaipur_trends_set , 'Kolkata': kolkata_trends_set, 'Chennai': chennai_trends_set, 'Bangalore': bangalore_trends_set}

for key, value in trends.iteritems():
	print '\n', key+':',
	for item in value:
		if '#' in item:	print item,

print
print

key = trends.keys()

for i in xrange(len(key)):
	for j in xrange(i+1, len(key)):
		print '\nCommon trends for', key[i], 'and', key[j], ':'
		common = trends[key[i]].intersection(trends[key[j]])
		if len(common) != 0:
			for item in common:
				if '#'in item:
					print item, 
		else:
			print 'None',
		print