from flask import Flask
import Utils

app = Flask(__name__)


@app.route('/')
# The method open the score file and return an HTML file showing the score of the user.
def score_server():
    try:
        score = open("/Users/DorZohar 1/PycharmProjects/WorldOfGames/Scores.txt", "r")
    except BaseException as e:
        return """<html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
        <body>
            <h1><div id="score" style="color:red">""" + Utils.ERROR_MESSAGE + str(e) + """</div></h1>
        </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>Scores Game</title>
        </head>
        <body>
            <h1>The score is <div id="score">""" + str(score.readline()) + """</div></h1>
        </body>
    </html>"""


if __name__ == '__main__':
    app.run(host='localhost', debug=True, threaded=True, port=8777)
