movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
      if movie[0] is "Memento":
            print("Memento is in the movelist!")
            break
      print(f"{movie[0]} ({movie[2]}), by {movie[1]}")

num = 1
for num in range(100):
      print("Number is: " + str(num))
      num = num + 1