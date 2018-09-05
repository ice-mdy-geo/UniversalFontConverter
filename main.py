from flask import Flask , render_template, request, jsonify
import ZgToUni
import UniToWin
import WinToUni
import UniToZg


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ztou')
def ztou():
    return render_template('ztou.html')

@app.route("/convert", methods=["POST"])
def convert():
    myinput = request.form['myinput']
    myinput = ZgToUni.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Please wirte or paste text in inputtextarea"})


@app.route('/ztow')
def ztow():
    return render_template('ztow.html')
@app.route("/convert1", methods=["POST"])
def convert1():
    myinput = request.form['myinput']
    myinput = ZgToUni.convert(myinput)
    myinput = UniToWin.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Please wirte or paste text in inputtextarea"})


@app.route('/wtou')
def wtou():
    return render_template('wtou.html')
@app.route("/convert2", methods=["POST"])
def convert2():
    myinput = request.form['myinput']
    myinput = WinToUni.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Please wirte or paste text in inputtextarea"})


@app.route('/wtoz')
def wtoz():
    return render_template('wtoz.html')
@app.route("/convert3", methods=["POST"])
def convert3():
    myinput = request.form['myinput']
    myinput = WinToUni.convert(myinput)
    myinput = UniToZg.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Please wirte or paste text in inputtextarea"})


@app.route('/utow')
def utow():
    return render_template('utow.html')
@app.route("/convert4", methods=["POST"])
def convert4():
    myinput = request.form['myinput']
    myinput = UniToWin.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Please wirte or paste text in inputtextarea"})


@app.route('/utoz')
def utoz():
    return render_template('utoz.html')
@app.route("/convert5", methods=["POST"])
def convert5():
    myinput = request.form['myinput']
    myinput = UniToZg.convert(myinput)
    output = myinput
    if myinput:
        return jsonify({'output': output})
    return jsonify({'output': "Please wirte or paste text in inputtextarea"})


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/work')
def work():
    return render_template('work.html')

if __name__ == '__main__':
    app.run(debug=True)
