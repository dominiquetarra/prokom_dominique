def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

#My profile
my_profile = build_profile(
    'Dominique', 
    'Winoto',
    location='Solo',
    age= 18,
    hobby='baking'
)

print(my_profile)