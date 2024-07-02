title = input("Title: ").strip()
director = input("Director: ").strip().title()
release_year = input("Release (year): ").strip()

print(f"{title} published {release_year} and directed by {director}!".capitalize())