from flask import Blueprint, render_template, url_for, request, redirect, session

home = Blueprint('home',__name__)

# Change this variable to True/False every time you want to
# switch between index page with conference or without conference
there_is_pycon = True

@home.route('/')
@home.route('/home')
def home_page():
	if session.get('lang') == None:
		session['lang'] = 'fr'

	if there_is_pycon:
		if session['lang'] == 'en':
			return render_template('index2.html')
		return render_template('index2-fr.html')

	if session['lang']=='en':
		return render_template('index.html')

	return render_template('index-fr.html')



# @home.route('/home2')
# def home2_page():
	
# 	return render_template('index2.html')


# ------About----------
@home.route('/about-pycon')
def about_pycon():
	title = "À propos de PyCon Niger"
	if session.get('lang') == None:
		session['lang'] = 'fr'

	if session['lang'] == 'en':
		title = "About PyCon Niger"
		return render_template('about-pycon.html', title=title)
	return render_template('about-pycon-fr.html', title=title)


@home.route('/about-coc')
def about_coc():
	title = "Code of Conduct"
	if session.get('lang') == None:
		session['lang'] = 'fr'

	if session['lang'] == 'en':
		return render_template('about-coc.html', title=title)
	return render_template('about-coc-fr.html', title=title)


@home.route('/about-health')
def about_health():
	title = "Directives de Santé et de Sécurité"
	if session.get('lang') == None:
		session['lang'] = 'fr'

	if session['lang'] == 'en':
		title = "Health and Safety guidance"
		return render_template('about-health.html', title=title)
	return render_template('about-health-fr.html', title=title)

# --------End-About----------



# ----------If-There-is-PyCon-----------
@home.route('/sponsorship')
def sponsorship_page():
	title = "Sponsor"
	if session.get('lang') == None:
		session['lang'] = 'fr'

	if session['lang'] == 'en':
		title = "Sponsor"
		return render_template('sponsorship.html', title=title)
	return render_template('sponsorship-fr.html', title=title)


@home.route('/speaking')
def speaking_page():
	title = "Devenez conférencier à PyCon Niger"
	if session.get('lang') == None:
		session['lang'] = 'fr'

	if session['lang'] == 'en':
		title = "Speaking at PyCon Niger"
		return render_template('speaking.html', title=title)
	return render_template('speaking-fr.html', title=title)


@home.route('/attending')
def attending_page():
	title = "Assister à PyCon Niger"
	if session.get('lang') == None:
		session['lang'] = 'fr'

	if session['lang'] == 'en':
		title = "Attend PyCon Niger"
		return render_template('attending.html', title=title)
	return render_template('attending-fr.html', title=title)


@home.route('/events')
def events_page():
	title = "Événements à PyCon Niger"
	if session.get('lang') == None:
		session['lang'] = 'fr'

	if session['lang'] == 'en':
		title = "Events at PyCon Niger"
		return render_template('events.html', title=title)
	return render_template('events-fr.html', title=title)


@home.route('/schedule')
def schedule_page():
	title = "Programme des événements"
	if session.get('lang') == None:
		session['lang'] = 'fr'

	if session['lang'] == 'en':
		title = "Events Schedules"
		return render_template('schedule.html', title=title)
	return render_template('schedule-fr.html', title=title)

# ------------End-if-------------------



@home.route('/internationalize', methods=['GET', 'POST'])
def lang_btn():
	lang = request.args.get('lang')
	session['lang'] = lang
	return redirect(url_for('home.home_page'))



@home.route('/sampling')
def sampling_page():
	
	return render_template('sampling.html')