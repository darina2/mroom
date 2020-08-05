from app import db
from datetime import datetime
import re



def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

movie_genres = db.Table('movie_genres',
                        db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
                        db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'))
)
movie_actors = db.Table('movie_actors',
                        db.Column('movie_id', db.Integer, db.ForeignKey('movie.id')),
                        db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'))
)



class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    tagline = db.Column(db.Text)
    description = db.Column(db.Text)
    img = db.Column(db.String(150))
    #slider = db.Column(db.String(150))
    #video = db.Column(db.String(150))
    year = db.Column(db.Integer)
    country = db.Column(db.String(70))
    actors = db.relationship('Actor', secondary=movie_actors, backref=db.backref('movies', lazy='dynamic'))
    premiere = db.Column(db.DateTime)
    budget = db.Column(db.Integer)
    fees_in_world = db.Column(db.Integer)
    genres = db.relationship('Genre', secondary=movie_genres, backref=db.backref('movies', lazy='dynamic'))
    movie_shots = db.relationship('MovieShots', backref='movie', lazy='dynamic')
    reviews = db.relationship('Reviews', backref='movie', lazy='dynamic')
    rating = db.relationship('Rating', backref='movie', lazy='dynamic')
   
    def __init__(self, *args, **kwargs):
        super(Movie, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'{self.title}'



class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    slug = db.Column(db.String(50), unique=True)

    def __init__(self, *args, **kwargs):
        super(Genre, self).__init__(*args, **kwargs)
        self.slug = slugify(self.title)

    def __repr__(self):
        return f'{self.title}'


class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)
    #image = db.Column(db.LargeBinary)
    age = db.Column(db.Integer)

    def __init__(self, *args, **kwargs):
        super(Actor, self).__init__(*args, **kwargs)
        self.slug = slugify(self.title)

    def __repr__(self):
        return f'{self.name}'



class MovieShots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    #slug = db.Column(db.String(100), unique=True)
    description = db.Column(db.Text)
    image = db.Column(db.LargeBinary)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))

    def __init__(self, *args, **kwargs):
        super(MovieShots, self).__init__(*args, **kwargs)
        #self.slug = slugify(self.title)

    def __repr__(self):
        return f'{self.title}'



class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    text = db.Column(db.Text)
   # parent = db.Column(db.LargeBinary)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    created = db.Column(db.DateTime, default = datetime.now())

    def __init__(self, *args, **kwargs):
        super(Reviews, self).__init__(*args, **kwargs)
        #self.slug = slugify(self.title)

    def __repr__(self):
        return f'{self.name}'



class RatingStars(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    rating = db.relationship('Rating', backref='ratingstars', lazy='dynamic')

    def __init__(self, *args, **kwargs):
        super(RatingStars, self).__init__(*args, **kwargs)
        #self.slug = slugify(self.title)

    def __repr__(self):
        return f'{self.value}'


class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    rating_stars_id = db.Column(db.Integer, db.ForeignKey('rating_stars.id'))

    def __init__(self, *args, **kwargs):
        super(Rating, self).__init__(*args, **kwargs)
        #self.slug = slugify(self.title)

    def __repr__(self):
        return f'rs id: {self.movie_id} mv id: {self.rating_stars_id}'
    
