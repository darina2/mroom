from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models import Movie, Genre
from .forms import MovieForm, UploadForm
from app import db
from flask_security import login_required
from werkzeug.utils import secure_filename


movies = Blueprint('movies', __name__, template_folder='templates')



@movies.route('/create', methods=["POST", "GET"])

def create_movie():
    if request.method == "POST":
        title = request.form['title']
        description = request.form['description']
        tagline = request.form['tagline']
        fees_in_world = request.form['fees_in_world']
        budget = request.form['budget']
        country = request.form['country']
        # poster
        premiere = request.form['premiere']
        year = request.form['year']


        try:
            movie = Movie(
                title=title, description=description, tagline=tagline, fees_in_world=fees_in_world,
                budget=budget, country=country, premiere=premiere, year=year
                )
            db.session.add(movie)
            db.session.commit()

        except:
            print('smth isnt ok')
        return redirect(url_for('movies.index'))

    form = MovieForm()
    return render_template('movies/create.html', form=form)

@movies.route('/<slug>/edit/', methods=["GET", "POST"])

def edit_movie(slug):
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()
    if request.method == 'POST':
        form = MovieForm(formdata=request.form, obj=movie)
        form.populate_obj(movie)
        db.session.commit()

        return redirect(url_for('movies.movie', slug=movie.slug))


    form = MovieForm(obj=movie)
    return render_template('movies/edit.html', movie=movie, form=form)


@movies.route('/<slug>/delete/', methods=["GET", "POST"])

def delete_movie(slug):
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()
    if request.method == 'GET':
        try:
            db.session.delete(movie)
            db.session.commit()

        except:
            print('smth isnt ok')
            return redirect(url_for('movies.index'))

    
    return render_template('movies/delete.html', movie=movie)




@movies.route('/<slug>/upload/', methods=['GET', 'POST'])
def upload(slug):
    form = UploadForm()
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()

    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        movie.img = '../../../static/img/uploads/' + filename
        db.session.commit()
        form.file.data.save('static/img/uploads/' + filename)
        return redirect(url_for('movies.movie', slug=slug))

    return render_template('movies/upload.html', form=form)




@movies.route('/')
def index():
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    q = request.args.get('q')
    if q:
        movies = Movie.query.filter(Movie.title.contains(q) | Movie.description.contains(q))#.all()
    else:
        movies = Movie.query#.all()

    pages = movies.paginate(page=page, per_page=5)
    return render_template('movies/index.html', title='Movies', movies=movies, pages=pages)




@movies.route('/<slug>', methods=["GET", "POST"])
def movie(slug):
    movie = Movie.query.filter(Movie.slug==slug).first_or_404()
    genres = movie.genres
    return render_template('movies/movie.html', movie=movie, genres=genres)

@movies.route('/genre/<slug>')
def genre(slug):
    page = request.args.get('page')

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    
    genre = Genre.query.filter(Genre.slug==slug).first()
    movies = genre.movies#.all()
    pages = movies.paginate(page=page, per_page=5)
    return render_template('movies/genre.html', genre=genre, movies=movies, title=genre.title, pages=pages)