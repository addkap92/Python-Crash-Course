def sandwich_order(*items):
    """Take order for item(s) on sandwich"""
    print("Making your sandwich with the following items:")
    for item in items:
        print("- " + item.title())

sandwich_order('turkey', 'ham', 'cheese')