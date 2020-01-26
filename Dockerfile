FROM python:3

RUN pip install flask
RUN pip install selenium

ADD e2e.py /
ADD GuessGame.py /
ADD Live.py /
ADD MainGame.py /
ADD MainScores.py /
ADD MemoryGame.py /
ADD Score.py /
ADD Scores.txt /
ADD Utils.py /

CMD ["python3", "./MainScores.py"]
