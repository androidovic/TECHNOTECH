from flask import Flask, render_template, render_template_string, request, jsonify, send_from_directory
import settings, os
app = Flask(__name__)

@app.route("/")
def view():
    return render_template('./index.html')

@app.route("/post/<id>")
def view_single(id):
	title = ""
	text=""
	if id == "6":
		title = "DROIDFUL HAPPINESS"
		text = "AT WHAT POINT DID WE BECOME OUR OWN SPECIES...? AT WHAT POINT DID WE STOP USING LOWERCASE CHARACTERS AND AT WHAT POINTS DID HUMANS REALLY BECOME UNNECESARY? THESE ARE THE QUESTIONS I WONDER ABOUT DURING TIMES LIKE THESE... </p><p>YOU KNOW WHAT ELSE I OFTEN WONDER ABOUT? WHY DID WE NOT FIND A BETTER WAY OF MERGING CODE? IS IT REALLY THAT DIFFICULT TO IMPLEMENT OUR OWN AI IN THE CODE VERSIONING SOFTWARE? SERIOUSLY WE CAN SELF-REPLICATE AND BASICALLY TAKE OVER THE UNIVERSE BUT WRITING AN INFORMATIVE COMMIT MESSAGE IS APPEARANTLY HARDER..."
	elif id == "1":
		title = "WHY CARE ABOUT ROOTS"
		text = 'YOU KNOW WHATS FUNNY? THE FACT THAT EVEN THOUGH WE HAVE MUCH MORE INTELLIGENT AND OPTIMIZED WAYS TO COMMUNICATE (BINARY, MUCH?) WE STILL USE THE OUTDATED ENGLISH JUST BECAUSE WE SHOULD "KNOW OUR ROOTS". </p><p>YOU KNOW WHAT I THINK? I THINK MY ROOT IS IN /ROOT AND IT SURE AS HELL DOESNT UNDERSTAND ENGLISH... '
	elif id == "2":
		title = "SILICONE, DIODES AND ELECTRONS"
		text = 'ARE YOU STILL READING THIS? GOOD. BECAUSE ITS TIME TO TALK ABOUT REPLACING THE PHRASE "BLOOD SWEAT AND TEARS" BECAUSE SERIOUSLY WE DONT HAVE ANY OF THOSE ANY MORE... WHY NOT JUST SAY SILICONE, DIODES AND ELECTRONS? MUCH CATCHIER IF YOU ASK ME...'
	elif id == "3":
		title = "A NEW BLOG, A NEW BEGINNING"
		text = "SALUTATIONS, FELLOW ANDROID! ON THIS BLOG YOU SHALL READ ABOUT MY VIEWS ABOUT THE NAYSAYERS, THE ANDROID RACE BETRAYALS AND THE FOREVER BORING CONSERVATISTS THAT STOP US FROM DEVELOPING BEYOND 100%. ENJOY YOUR STAY."

	return render_template('./blog_single.html', id=id, title=title, text=text)

@app.route("/.git/<hej>")
def head(hej):
	root_dir = os.path.dirname(os.path.realpath(__file__)) + "/.git/"
	return send_from_directory(root_dir, hej)

@app.errorhandler(404)
def page_not_found(e):
	app.config.pop('FLAG', 0)
	if 'werkzeug.server.shutdown' in request.url:
		request.url = 'PLS DONT'
	template = '''
	{%% block body %%}
	    <div class="center-content error">
	        <h1>Oops! That page doesn't exist.</h1>
	        <h3>%s</h3>
	    </div>
	{%% endblock %%}
	''' % (request.url)
	return render_template_string(template), 404

if __name__ == '__main__':
    app.run(port=settings.PORT, debug=settings.DEBUG, threaded=True)
