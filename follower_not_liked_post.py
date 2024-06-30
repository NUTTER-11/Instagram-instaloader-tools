import instaloader
import time
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Log in to Instagram
username = ''
password = ''
L.login(username, password)

# Function to get likes with retry logic
def get_likes_with_retry(post, max_retries=3, delay=5):
    for attempt in range(max_retries):
        try:
            return {like.username for like in post.get_likes()}
        except instaloader.exceptions.QueryReturnedBadRequestException as e:
            logging.warning(f"Attempt {attempt + 1}: Error retrieving likes - {e}")
            time.sleep(delay)
    raise Exception("Failed to retrieve likes after multiple attempts")

def main():
    try:
        # Prompt the user to enter the target profile's username
        profile_name = input("Enter the Instagram username of the profile: ")

        # Load the profile
        profile = instaloader.Profile.from_username(L.context, profile_name)

        # Retrieve followers
        followers = {follower.username for follower in profile.get_followers()}

        # Create a list to store post objects
        posts_list = list(profile.get_posts())

        # Display the total number of posts
        total_posts = len(posts_list)
        print(f"Total number of posts: {total_posts}")

        # Prompt the user to enter the post number they want to explore
        selected_post_number = int(input(f"Enter the post number you want to explore (1-{total_posts}): "))

        # Get the selected post
        selected_post = posts_list[selected_post_number - 1]

        # Retrieve the users who liked the selected post
        likes = get_likes_with_retry(selected_post)

        # Find followers who liked the selected post
        followers_who_liked = followers.intersection(likes)

        # Retrieve engagement metrics for the selected post
        total_likes = selected_post.likes
        total_comments = selected_post.comments

        # Print the metrics for the selected post
        print(f"Post Number: {selected_post_number}")
        print(f"Post URL: {selected_post.url}")
        print(f"Total likes: {total_likes}")
        print(f"Total comments: {total_comments}")

        # Print the followers who liked the post
        print(f"Followers who liked the post:")
        for follower in followers_who_liked:
            print(follower)

        # Save the metrics and followers who liked the post to a file
        with open(f"{profile_name}_selected_post_engagement.txt", "w") as f:
            f.write(f"Post Number: {selected_post_number}\n")
            f.write(f"Post URL: {selected_post.url}\n")
            f.write(f"Total likes: {total_likes}\n")
            f.write(f"Total comments: {total_comments}\n")
            f.write(f"\nFollowers who liked the post:\n")
            for follower in followers_who_liked:
                f.write(f"{follower}\n")

        print(f"Selected post engagement metrics and followers who liked the post have been saved to {profile_name}_selected_post_engagement.txt")

    except instaloader.exceptions.QueryReturnedBadRequestException as e:
        logging.error(f"QueryReturnedBadRequestException: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
