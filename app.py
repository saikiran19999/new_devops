from flask import Flask, render_template

app = Flask(__name__)

# Sample news articles
news_articles = [
    {
        "title": "Breaking News 1",
        "content": "This is the content of the first breaking news article."
    },
    {
        "title": "Breaking News 2",
        "content": "This is the content of the second breaking news article."
    }
]

@app.route('/')
def index():
    return render_template('index.html', articles=news_articles)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
