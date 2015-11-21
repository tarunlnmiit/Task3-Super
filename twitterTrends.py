# https://api.twitter.com/1.1/trends/place.json/?id=1&oauth_consumer_key=mdkejxebqytj99rnkyhc1mcte&oauth_nonce=0708a4359f7a249405ccda85750a5d65&oauth_signature_method=hmac-sha1&oauth_timestamp=1448114158&oauth_token=1100686363-6jxqino5t8umpqewyah783qrxxjjrmwbljcetof&oauth_version=1.0

import twitter
import json

auth = twitter.oauth.OAuth('1100686363-6JxQIno5T8UMPQeWyaH783qrxxJJrmwbLJCEtoF', 'GqgnME3MRfOQL79TzWuH5S9fJOgXXogdAwyVDzGSk4ovD', 'mDkejxEBQYTj99RNkYhc1mCTE', 'WR2xlMAu4gRelaPRDkywDXCAGldZOZT6u4AymUBE0MpyjtooCg')

twitter_api = twitter.Twitter(auth=auth)

print twitter_api
i = 1
wt = twitter_api.trends.place(_id=i)

#print wt

print json.dumps(wt, indent=1)