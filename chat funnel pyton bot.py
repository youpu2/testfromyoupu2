# Ask for user's name
try:
    name = input("Hey there, what's your name? ")
    if not name.strip():
        raise ValueError("Name cannot be empty!")

    # Say hello
    print(f"Nice to meet you, {name}. I am your assistant during your journey here.")

    # Ask for interest
    interest = input(f"What are you interested in, {name}? ").strip()
    if not interest:
        raise ValueError("Interest cannot be empty!")

    # Inform about unavailable courses
    print(f"{interest} is a very good thing to learn nowadays! We have great courses about that which are really going to help you, {name}. "
          "But I am sorry to say we are under heavy development right now. I will let you know when we are available if you can tell me your email.")

    # Ask for email
    user_email = input("Type your email so I can let you know as soon as possible when we are open for use: ").strip()
    if not user_email or "@" not in user_email or "." not in user_email:
        raise ValueError("Invalid email address!")

    # Thank the user
    print(f"Thank you so much for understanding, {name}. We will let you know at {user_email} as soon as {interest} courses are available on our platform.")

except ValueError as e:
    print(f"Error: {e}")