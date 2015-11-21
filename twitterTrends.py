# https://api.twitter.com/1.1/trends/place.json/?id=1&oauth_consumer_key=mdkejxebqytj99rnkyhc1mcte&oauth_nonce=0708a4359f7a249405ccda85750a5d65&oauth_signature_method=hmac-sha1&oauth_timestamp=1448114158&oauth_token=1100686363-6jxqino5t8umpqewyah783qrxxjjrmwbljcetof&oauth_version=1.0

import twitter
import json

auth = twitter.oauth.OAuth('1100686363-6JxQIno5T8UMPQeWyaH783qrxxJJrmwbLJCEtoF', 'GqgnME3MRfOQL79TzWuH5S9fJOgXXogdAwyVDzGSk4ovD', 'mDkejxEBQYTj99RNkYhc1mCTE', 'WR2xlMAu4gRelaPRDkywDXCAGldZOZT6u4AymUBE0MpyjtooCg')

twitter_api = twitter.Twitter(auth=auth)

world_woeid = 1
mumbai_woeid = 2295411
delhi_woeid = 2295019
pune_woeid = 2295412
jaipur_woeid = 2295401
kolkata_woeid = 2295386
chennai_woeid = 2295424
bangalore_woeid = 2295420

world_trends = twitter_api.trends.place(_id=world_woeid)
mumbai_trends = twitter_api.trends.place(_id=mumbai_woeid)
delhi_trends = twitter_api.trends.place(_id=delhi_woeid)
pune_trends = twitter_api.trends.place(_id=pune_woeid)
jaipur_trends = twitter_api.trends.place(_id=jaipur_woeid)
kolkata_trends = twitter_api.trends.place(_id=kolkata_woeid)
chennai_trends = twitter_api.trends.place(_id=chennai_woeid)
bangalore_trends = twitter_api.trends.place(_id=bangalore_woeid)

#print json.dumps(wt, indent=1)

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
mumbai_trends_set = set([trend['name'] for trend in mumbai_trends[0]['trends']])
delhi_trends_set = set([trend['name'] for trend in delhi_trends[0]['trends']])
pune_trends_set = set([trend['name'] for trend in pune_trends[0]['trends']])
jaipur_trends_set = set([trend['name'] for trend in jaipur_trends[0]['trends']])
kolkata_trends_set = set([trend['name'] for trend in kolkata_trends[0]['trends']])
chennai_trends_set = set([trend['name'] for trend in chennai_trends[0]['trends']])
bangalore_trends_set = set([trend['name'] for trend in bangaloretrends[0]['trends']])

common_world_mumbai = world_trends_set.intersection(mumbai_trends_set)
common_world_delhi = world_trends_set.intersection(delhi_trends_set)
common_world_pune = world_trends_set.intersection(pune_trends_set)
common_world_jaipur = world_trends_set.intersection(jaipur_trends_set)
common_world_kolkata = world_trends_set.intersection(kolkata_trends_set)
common_world_chennai = world_trends_set.intersection(chennai_trends_set)
common_world_bangalore = world_trends_set.intersection(bangalore_trends_set)

print 'Mumbai:', common_world_mumbai
print 'Delhi:', common_world_delhi
print 'Pune:', common_world_pune
print 'Jaipur:', common_world_jaipur
print 'Kolkata:', common_world_kolkata
print 'Chennai:', common_world_chennai
print 'Bangalore:', common_world_bangalore