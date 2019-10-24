import instaloader

# Get instance
L = instaloader.Instaloader()
USER = "self_user"
PROFILE = "user"
# Login or load session
#L.login(USER, PASSWORD)        # (login)
L.interactive_login(USER)      # (ask password on terminal)
#L.load_session_from_file(USER) # (load session created w/
                               #  `instaloader -l USERNAME`)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, PROFILE)
# Print list of followees
followers = []
for followee in profile.get_followees():
     followers.append(followee.username)
#    print("written\n")
followers.sort()
file = open(f"{PROFILE}.txt","a+")
for i in followers:
    file.write(i + '\n')
file.close()
print("numbers of followees  = ")
