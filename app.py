from flask import Flask, render_template
import weatherstation as weather

app = Flask(__name__)    

@app.route('/')
def index():
    return render_template('index.html',temp = weather.gettemp(),
                           humidity= weather.gethumidity(),
                           pressure= weather.getpressure(),
                           avgtemp = weather.getavgtemp(),
                           mintemp = weather.getmintemp(),
                           maxtemp = weather.getmaxtemp(),
                           minhum = weather.getminhum(),
                           maxhum = weather.getmaxhum(),
                           minpres = weather.getminpres(),
                           maxpres = weather.getmaxpres(),
                           avghum = weather.getavghum(),
                           avgpres = weather.getavgpres())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    

