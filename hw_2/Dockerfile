FROM texlive/texlive

RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

#RUN python3 -m venv venv
#ENV PATH="/app/venv/bin:$PATH"

COPY ./task2 /app

RUN pip install --break-system-packages -r requirements.txt


RUN python3 main.py

RUN pdflatex task2.tex

#CMD ["pdflatex", "task2.tex"]
