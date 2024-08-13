import instaloader
import pandas as pd


def authenticate(username, password):
    L = instaloader.Instaloader()
    L.login(username, password)
    return L


def get_followers(L, username):
    profile = instaloader.Profile.from_username(L.context, username)
    followers = [follower.username for follower in profile.get_followers()]
    return followers


def get_recent_posts(L, username, num_posts=5):
    profile = instaloader.Profile.from_username(L.context, username)
    posts = []
    for post in profile.get_posts():
        posts.append(post)
        if len(posts) >= num_posts:
            break
    return posts


def get_likers(post):
    return [like.username for like in post.get_likes()]


def find_non_engaged_followers(L, followers, recent_posts):
    engaged_users = set()
    for post in recent_posts:
        likers = get_likers(post)
        engaged_users.update(likers)
    non_engaged_followers = [follower for follower in followers if follower not in engaged_users]
    return non_engaged_followers


def save_non_engaged_followers_to_excel(non_engaged_followers):
    df = pd.DataFrame(non_engaged_followers, columns=["Username"])
    df.to_excel("non_engaged_followers.xlsx", index=False)
    print("List saved to non_engaged_followers.xlsx")


if __name__ == "__main__":
    username = "parbhakar_n"
    password = "Sonyphone@5"

    L = authenticate(username, password)
    followers = get_followers(L, username)
    recent_posts = get_recent_posts(L, username)
    non_engaged_followers = find_non_engaged_followers(L, followers, recent_posts)
    save_non_engaged_followers_to_excel(non_engaged_followers)
