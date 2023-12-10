def generate_table(data):
    header = "\\begin{tabular}{" + "|c" * len(data[0]) + "|" "}\n\\hline\n"
    body = ""
    for row in data:
        body += " & ".join(map(str, row)) + " \\\\\n\\hline\n"
    footer = "\\end{tabular}"
    return header + body + footer

def generate_image(filepath, caption=""):
    return f"\\begin{{figure}}[h]\n\\centering\n\\includegraphics[width=0.5\\textwidth]{{{filepath}}}\n\\caption{{{caption}}}\n\\end{{figure}}"

