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

# Create a list to store post objects
posts_list = list(profile.get_posts())

# Display the total number of posts
total_posts = len(posts_list)
print(f"Total number of posts: {total_posts}")

# Prompt the user to enter the post number they want to explore
selected_post_number = int(input(f"Enter the post number you want to explore (1-{total_posts}): "))

# Get the selected post
selected_post = posts_list[selected_post_number - 1]

# Extract shortcode and URL
shortcode = selected_post.shortcode
post_url = selected_post.url

# Retrieve the engagement metrics for the selected post
total_likes = selected_post.likes
total_comments = selected_post.comments

# Print the metrics for the selected post
print(f"Post Number: {selected_post_number}")
print(f"Post URL: {post_url}")
print(f"Shortcode: {shortcode}")
print(f"Total likes: {total_likes}")
print(f"Total comments: {total_comments}")

# Save the metrics to a file
with open(f"{profile_name}_selected_post_engagement.txt", "w") as f:
    f.write(f"Post Number: {selected_post_number}\n")
    f.write(f"Post URL: {post_url}\n")
    f.write(f"Shortcode: {shortcode}\n")
    f.write(f"Total likes: {total_likes}\n")
    f.write(f"Total comments: {total_comments}\n")

print(f"Selected post engagement metrics have been saved to {profile_name}_selected_post_engagement.txt")
