def build_profile(first, last, **user_info):
      """Build a dictionary containing everything we know about a user."""
      user_info['first_name'] = first  
      user_info['last_name'] = last  
      return user_info  

user_profile1 = build_profile('albert', 'einstein',  location='princeton',  field='physics')
user_profile2 = build_profile('chris', 'slusher',  location='san diego',  field='computer science', interests=["AI Engineering", "Making money"])
user_profile3 = build_profile('leah', 'slusher',  location='ensenada',  field='student', favorite_music="pop", interests=["dancing", "drawing"], age=12)

print(user_profile1) 
print(user_profile2) 
print(user_profile3) 
