from flask import Flask, render_template, redirect, request
import sys
app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=["GET"])
def hello():
	return '<a href="/about">about me</a><a href="/clock">clock</a>'

@app.route('/', methods=['POST'])
def comment():
	print request.form
	sys.stdout.flush()
	return redirect('/')

@app.route("/about")
def about():
	return render_template("ABeautifulShortLine.html")

@app.route("/clock")
def clock():
	return '<iframe src="http://free.timeanddate.com/clock/i41xuo8b/n43/szw110/szh110/hocfff/hbw0/hfc000/cf100/hgr0/fav0/fiv0/mqc0f0/mqs2/mql4/mqw4/mqd86/mhc0f0/mhs2/mhl4/mhw4/mhd86/mmc0f0/mml2/mmd88/hhc00f/hhs3/hhl50/hhw11/hmc00f/hms3/hml80/hmw11/hsc00f/hsl90/hsw6" frameborder="0" width="112" height="112"></iframe>'

if __name__ == "__main__":
	app.run()
