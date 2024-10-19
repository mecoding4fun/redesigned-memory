import json
following = open("following.json",'r')
followers = open("followers.json",'r')

following_json = json.load(following)
followers_json = json.load(followers)

def followingset():
    following_set = set()
    for i in following_json['relationships_following']:
        following_set.add(i['string_list_data'][0]['value'])
    return following_set

def followersset():
    followers_set = set()
    for i in followers_json:
        followers_set.add(i['string_list_data'][0]['value'])
    return followers_set

not_following = followingset() - followersset()

for n in not_following:
    print(n)

