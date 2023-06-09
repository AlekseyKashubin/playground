from flask import Flask, render_template

app = Flask(__name__)





@app.route('/play')
def lel1():
    return render_template('index.html')

@app.route('/play/<int:num>')
def lel2(num):
    return render_template("index2.html", num=num )

@app.route('/play/<int:num>/<color_change>')
def lel3(num, color_change):
    
    return render_template('index3.html', num=num, color = color_change)





if __name__=="__main__":
    app.run(debug=True, port=5000)

