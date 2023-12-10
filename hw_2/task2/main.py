from andrew55516_latex import latex

if __name__ == "__main__":
    data = [
        ["a", "b", "c"],
        [1, 2, 3],
        [4, 5, 6]
    ]

    table = latex.generate_table(data)

    img = latex.generate_image("img.jpg")

    with open("task2.tex", "w") as file:
        document = '\\documentclass{article}\n\\usepackage{graphicx}\n\\begin{document}\n' + table + '\n' + img + '\n\\end{document}'
        file.write(document)