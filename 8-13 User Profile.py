def build_user(first, last, **other):
    profile = {'first_name'.title(): first.title(), 'last_name'.title(): last.title()}
    for key, value in other.items():
        profile[key.title()] = value.title()
    return profile
user_profile = build_user('adam', 'kap', hobby='guitar', career='programmer', favorite_tvshow='scrubs')
print(user_profile)