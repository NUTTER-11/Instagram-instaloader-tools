from instagrapi import Client
from datetime import datetime, timedelta

# Instagram credentials
USERNAME = ''
PASSWORD = ''

# Time period to consider a follower inactive (e.g., 30 days)
INACTIVITY_PERIOD = 60


def login_to_instagram():
    cl = Client()
    cl.login(USERNAME, PASSWORD)
    return cl


def get_followers(cl):
    return cl.user_followers(cl.user_id)


def get_recent_activity(cl, user_id, since_date):
    media = cl.user_medias(user_id, 50)  # Get up to 50 recent posts
    recent_activity = False

    for post in media:
        if post.taken_at > since_date:
            likers = cl.media_likers(post.pk)
            if cl.user_id in likers:
                recent_activity = True
                break
    return recent_activity


def unfollow_inactive_followers(cl, followers):
    since_date = datetime.now() - timedelta(days=INACTIVITY_PERIOD)
    inactive_users = []

    for user_id in followers:
        print(f"Checking activity for user {followers[user_id].username}...")
        if not get_recent_activity(cl, user_id, since_date):
            inactive_users.append(user_id)

    for user_id in inactive_users:
        print(f"Unfollowing inactive user {followers[user_id].username}...")
        cl.user_unfollow(user_id)


def main():
    cl = login_to_instagram()
    followers = get_followers(cl)
    unfollow_inactive_followers(cl, followers)
    print("Cleanup complete.")


if __name__ == '__main__':
    main()
