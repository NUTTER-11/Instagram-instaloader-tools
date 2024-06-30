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

        # Print the number of followers and following
        num_followers = profile.followers
        num_following = profile.followees
        print(f"{profile_name} has {num_followers} followers and is following {num_following} accounts.")

        # Ask the user if they want to see the list of followers
        show_followers = input("Do you want to see the list of followers? (yes/no): ").strip().lower()
        if show_followers == 'yes':
            print(f"Fetching followers of {profile_name}...")

            # Get the list of followers
            followers = profile.get_followers()

            # Print the list of followers
            print(f"Followers of {profile_name}:")
            for follower in followers:
                print(follower.username)

            # Save the followers to a file
            with open(f"{profile_name}_followers.txt", "w") as f:
                for follower in followers:
                    f.write(f"{follower.username}\n")

            print(f"Followers have been saved to {profile_name}_followers.txt")
        else:
            print("Not displaying the list of followers.")

        # Ask the user if they want to see the list of following
        show_following = input("Do you want to see the list of following? (yes/no): ").strip().lower()
        if show_following == 'yes':
            print(f"Fetching following of {profile_name}...")

            # Get the list of following
            following = profile.get_followees()

            # Print the list of following
            print(f"{profile_name} is following:")
            for followee in following:
                print(followee.username)

            # Save the following to a file
            with open(f"{profile_name}_following.txt", "w") as f:
                for followee in following:
                    f.write(f"{followee.username}\n")

            print(f"Following list has been saved to {profile_name}_following.txt")
        else:
            print("Not displaying the list of following.")
    else:
        print(f"You are not following {profile_name}. Cannot fetch followers or following.")
else:
    # Print the number of followers and following for a public profile
    num_followers = profile.followers
    num_following = profile.followees
    print(f"{profile_name} has {num_followers} followers and is following {num_following} accounts.")

    # Ask the user if they want to see the list of followers
    show_followers = input("Do you want to see the list of followers? (yes/no): ").strip().lower()
    if show_followers == 'yes':
        print(f"Fetching followers of {profile_name}...")

        # Get the list of followers
        followers = profile.get_followers()

        # Print the list of followers
        print(f"Followers of {profile_name}:")
        for follower in followers:
            print(follower.username)

        # Save the followers to a file
        with open(f"{profile_name}_followers.txt", "w") as f:
            for follower in followers:
                f.write(f"{follower.username}\n")

        print(f"Followers have been saved to {profile_name}_followers.txt")
    else:
        print("Not displaying the list of followers.")

    # Ask the user if they want to see the list of following
    show_following = input("Do you want to see the list of following? (yes/no): ").strip().lower()
    if show_following == 'yes':
        print(f"Fetching following of {profile_name}...")

        # Get the list of following
        following = profile.get_followees()

        # Print the list of following
        print(f"{profile_name} is following:")
        for followee in following:
            print(followee.username)

        # Save the following to a file
        with open(f"{profile_name}_following.txt", "w") as f:
            for followee in following:
                f.write(f"{followee.username}\n")

        print(f"Following list has been saved to {profile_name}_following.txt")
    else:
        print("Not displaying the list of following.")
