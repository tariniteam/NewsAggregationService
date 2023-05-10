from ScrapperJob.ScrapperJob import ScrapperJob
import threading
from flask import Flask, render_template, redirect

app = Flask(__name__)


#We can render any information on any template by routing it to a particular url

@app.route('/',method = ["GET"])
def home():
    content = ScrapperJob.getContect()
    if content is None:
        return "Data is not available at present, soon it will come"
    return render_template('home.html', content = content)
    pass

@app.route('/aboutme', method = ["GET"])
def aboutme():
    pass




if __name__ == '__main__':
    nas_thread1 = threading.Thread(target = ScrapperJob.start_scrapping)
    nas_thread1.daemon = True
    nas_thread1.start()

    #Now next in the main thread we need to run  our flask server.
    app.run()