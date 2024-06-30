import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Log in to Instagram
username = ''
password = ''
L.login(username, password)

# Prompt the user to enter the target profile's username
profile_name = input("Enter the Instagram username of the profile: ")

# Load the profile
profile = instaloader.Profile.from_username(L.context, profile_name)

# Check if the profile is private
if profile.is_private:
    print(f"{profile_name} is a private profile.")

    # Check if you are following the private profile
    if profile.followed_by_viewer:
        print(f"You are following {profile_name}.")

        # Fetch the lists of followers and followees
        followers = {follower.username for follower in profile.get_followers()}
        followees = {followee.username for followee in profile.get_followees()}

        # Find people who are in the following list but not in the followers list
        not_following_back = followees - followers

        # Print the number of people not following back
        num_not_following_back = len(not_following_back)
        print(f"Number of people {profile_name} is following but are not following back: {num_not_following_back}")

        # Print the list of people who are in the following list but not in the followers list
        print(f"People who {profile_name} is following but are not following back:")
        for user in not_following_back:
            print(user)

        # Save the list to a file
        with open(f"{profile_name}_not_following_back.txt", "w") as f:
            for user in not_following_back:
                f.write(f"{user}\n")

        print(f"The list of people who are not following back has been saved to {profile_name}_not_following_back.txt")
    else:
        print(f"You are not following {profile_name}. Cannot fetch followers or following.")
else:
    # Fetch the lists of followers and followees for a public profile
    followers = {follower.username for follower in profile.get_followers()}
    followees = {followee.username for followee in profile.get_followees()}

    # Find people who are in the following list but not in the followers list
    not_following_back = followees - followers

    # Print the number of people not following back
    num_not_following_back = len(not_following_back)
    print(f"Number of people {profile_name} is following but are not following back: {num_not_following_back}")

    # Print the list of people who are in the following list but not in the followers list
    print(f"People who {profile_name} is following but are not following back:")
    for user in not_following_back:
        print(user)

    # Save the list to a file
    with open(f"{profile_name}_not_following_back.txt", "w") as f:
        for user in not_following_back:
            f.write(f"{user}\n")

    print(f"The list of people who are not following back has been saved to {profile_name}_not_following_back.txt")
