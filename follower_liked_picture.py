import instaloader
from instaloader.exceptions import BadResponseException, QueryReturnedBadRequestException, \
    PrivateProfileNotFollowedException, ConnectionException

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Login to Instagram
username = ''
password = ''
L.login(username, password)


# Function to get followers
def get_followers(profile):
    followers = set()
    for follower in profile.get_followers():
        followers.add(follower.username)
    return followers


# Function to get likers of a post
def get_likers(post):
    likers = set()
    try:
        for liker in post.get_likes():
            likers.add(liker.username)
    except QueryReturnedBadRequestException as e:
        print("Query returned bad request:", e)
    return likers


# Load target user's profile
target_user = input("Enter the Instagram username of the profile: ")
profile = instaloader.Profile.from_username(L.context, target_user)

# Get followers of the target user
followers = get_followers(profile)

# Load the post by its shortcode (last part of the URL)
post_shortcode = 'C8yrAhUv_Pt9AN4OzpxDmyX_g-_rNBh7mFOp5A0'  # e.g., 'CPfppLRF68x'

try:
    post = instaloader.Post.from_shortcode(L.context, post_shortcode)
    # Get likers of the post
    likers = get_likers(post)

    # Compare followers and likers
    liked_by_followers = followers & likers
    not_liked_by_followers = followers - likers

    print("Followers who liked the post:", liked_by_followers)
    print("Followers who did not like the post:", not_liked_by_followers)

except PrivateProfileNotFollowedException:
    print("The profile or post is private and cannot be accessed.")
except ConnectionException:
    print("Network issue or Instagram might be down.")
except BadResponseException as e:
    print("Failed to fetch post metadata:", e)
except QueryReturnedBadRequestException as e:
    print("Bad request error while querying post metadata:", e)
except Exception as e:
    print("An unexpected error occurred:", e)