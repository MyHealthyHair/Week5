def make_sandwich(*items):
    """Make a sandwich with the given items."""
    print("\nI'll make you a great sandwich:")
    for item in items:
        print("Adding " + item + " to your sandwich.")
    print("Your sandwich is ready!")

make_sandwich('beef')
make_sandwich('chicken')
make_sandwich('salami')
