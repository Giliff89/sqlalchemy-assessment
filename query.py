"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# The datatype is a dictionary of key:value pairs for all of the information
# in the table where the brand name is 'Ford'.


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# An association table is an information funnel, or detangler, for a
# many-to-many relationship. It may contain little to no information of its own,
# but serves as a landing pad for keys from either connecting table where you
# can establish a 'transaction' or event that happens between elements from
# two tables that cannot be easily stored otherwise.
# For example, if we have a table of books in a library and a table of people
# who can check out books, we would need an associate table to link a book id
# with a person id under a transaction or borrow id in order to keep the data straight.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# Get the brand with the ``id`` of "ram."
q1 = Brand.query.filter_by(brand_id='ram').first()

# Get all models with the name "Corvette" and the brand_id "che."
q2 = Model.query.filter_by(name='Corvette', brand_id='che').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor."
q5 = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter_by(founded=1903, discontinued=None).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()

# Get any model whose brand_id is not "for."
q8 = Model.query.filter(Model.brand_id != 'for').all()


# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    models = db.session.query(Model.name,
                              Brand.name,
                              Brand.headquarters).join(Brand).filter(Model.year == year).all()

    print models


def get_brands_summary():
    """Prints out each brand name and each model name with year for that brand
    using only ONE database query."""

    brand_summary = db.session.query(Brand.name,
                                     Model.name,
                                     Model.year).join(Model).all()

    # I am stuck on this one, I am pulling the correct information but don't know
    # how to print out the items grouped by brand with one query.

    print brand_summary


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    brand_by_name = Brand.query.filter(Brand.name.like('%{}%'.format(mystr))).all()

    return brand_by_name


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    models_between = Model.query.filter(Model.year >= start_year, Model.year < end_year).all()

    return models_between
