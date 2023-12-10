from hw_2.andrew55516_latex.latex import generate_table

if __name__ == "__main__":
    data = [
        ["a", "b", "c"],
        [1, 2, 3],
        [4, 5, 6]
    ]

    table = generate_table(data)

    with open("task1.tex", "w") as file:
        file.write(table)