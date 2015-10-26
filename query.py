"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.filter(Brand.id == 8).all()
# [<Brand id=8 name=Austin founded=1905 headquarters=Longbridge, England discontinued1987>]

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == "Corvette", Model.brand_name == "Chevrolet").all()
# SELECT models.id AS models_id, models.year AS models_year, models.brand_name
# AS models_brand_name, models.name AS models_name
# FROM models
# WHERE models.name = ? AND models.brand_name = ?

# [<Model id=5 year=1953 brand_name=Chevrolet name=Corvette>,
#  <Model id=6 year=1954 brand_name=Chevrolet name=Corvette>,
#  <Model id=8 year=1955 brand_name=Chevrolet name=Corvette>,
#  <Model id=10 year=1956 brand_name=Chevrolet name=Corvette>,
#  <Model id=11 year=1957 brand_name=Chevrolet name=Corvette>,
#  <Model id=13 year=1958 brand_name=Chevrolet name=Corvette>,
#  <Model id=17 year=1959 brand_name=Chevrolet name=Corvette>,
#  <Model id=20 year=1960 brand_name=Chevrolet name=Corvette>,
#  <Model id=26 year=1961 brand_name=Chevrolet name=Corvette>,
#  <Model id=28 year=1962 brand_name=Chevrolet name=Corvette>,
#  <Model id=38 year=1963 brand_name=Chevrolet name=Corvette>,
#  <Model id=39 year=1964 brand_name=Chevrolet name=Corvette>]

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()
# SELECT models.id AS models_id, models.year AS models_year, models.brand_name
# AS models_brand_name, models.name AS models_name
# FROM models
# WHERE models.year > ?
# [<Model id=23 year=1961 brand_name=Austin name=Mini Cooper>,
 # <Model id=24 year=1961 brand_name=Studebaker name=Avanti>,
 # <Model id=25 year=1961 brand_name=Pontiac name=Tempest>,
 # <Model id=26 year=1961 brand_name=Chevrolet name=Corvette>,
 # <Model id=27 year=1962 brand_name=Pontiac name=Grand Prix>,
 # <Model id=28 year=1962 brand_name=Chevrolet name=Corvette>,
 # <Model id=29 year=1962 brand_name=Studebaker name=Avanti>,
 # <Model id=30 year=1962 brand_name=Buick name=Special>,
 # <Model id=31 year=1963 brand_name=Austin name=Mini>,
 # <Model id=32 year=1963 brand_name=Austin name=Mini Cooper S>,
 # <Model id=33 year=1963 brand_name=Rambler name=Classic>,
 # <Model id=34 year=1963 brand_name=Ford name=E-Series>,
 # <Model id=35 year=1963 brand_name=Studebaker name=Avanti>,
 # <Model id=36 year=1963 brand_name=Pontiac name=Grand Prix>,
 # <Model id=37 year=1963 brand_name=Chevrolet name=Corvair 500>,
 # <Model id=38 year=1963 brand_name=Chevrolet name=Corvette>,
 # <Model id=39 year=1964 brand_name=Chevrolet name=Corvette>,
 # <Model id=40 year=1964 brand_name=Ford name=Mustang>,
 # <Model id=41 year=1964 brand_name=Ford name=Galaxie>,
 # <Model id=42 year=1964 brand_name=Pontiac name=GTO>,
 # <Model id=43 year=1964 brand_name=Pontiac name=LeMans>,
 # <Model id=44 year=1964 brand_name=Pontiac name=Bonneville>,
 # <Model id=45 year=1964 brand_name=Pontiac name=Grand Prix>,
 # <Model id=46 year=1964 brand_name=Plymouth name=Fury>,
 # <Model id=47 year=1964 brand_name=Studebaker name=Avanti>,
 # <Model id=48 year=1964 brand_name=Austin name=Mini Cooper>]

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()
# SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded
# AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued
# AS brands_discontinued
# FROM brands
# WHERE brands.founded > ?

# [<Brand id=2 name=Chrysler founded=1925 headquarters=Auburn Hills, Michigan discontinuedNone>,
# <Brand id=9 name=Fairthorpe founded=1954 headquarters=Chalfont St Peter, Buckinghamshire discontinued1976>,
# <Brand id=11 name=Pontiac founded=1926 headquarters=Detroit, MI discontinued2010>,
# <Brand id=14 name=Plymouth founded=1928 headquarters=Auburn Hills, Michigan discontinued2001>,
# <Brand id=15 name=Tesla founded=2003 headquarters=Palo Alto, CA discontinuedNone>]

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like("%Cor%" )).all()
# SELECT models.id AS models_id, models.year AS models_year, models.brand_name
# AS models_brand_name, models.name AS models_name
# FROM models
# WHERE models.name LIKE ?

# [<Model id=5 year=1953 brand_name=Chevrolet name=Corvette>,
# <Model id=6 year=1954 brand_name=Chevrolet name=Corvette>,
# <Model id=8 year=1955 brand_name=Chevrolet name=Corvette>,
# <Model id=10 year=1956 brand_name=Chevrolet name=Corvette>,
# <Model id=11 year=1957 brand_name=Chevrolet name=Corvette>,
# <Model id=13 year=1958 brand_name=Chevrolet name=Corvette>,
# <Model id=17 year=1959 brand_name=Chevrolet name=Corvette>,
# <Model id=19 year=1960 brand_name=Chevrolet name=Corvair>,
# <Model id=20 year=1960 brand_name=Chevrolet name=Corvette>,
# <Model id=26 year=1961 brand_name=Chevrolet name=Corvette>,
# <Model id=28 year=1962 brand_name=Chevrolet name=Corvette>,
# <Model id=37 year=1963 brand_name=Chevrolet name=Corvair 500>,
# <Model id=38 year=1963 brand_name=Chevrolet name=Corvette>,
# <Model id=39 year=1964 brand_name=Chevrolet name=Corvette>]

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()
# SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded
# AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued
# AS brands_discontinued
# FROM brands
# WHERE brands.founded = ? AND brands.discontinued IS NULL

# [<Brand id=1 name=Ford founded=1903 headquarters=Dearborn, MI discontinuedNone>,
#  <Brand id=12 name=Buick founded=1903 headquarters=Detroit, MI discontinuedNone>]

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter((Brand.founded < 1950) | (Brand.discontinued != None)).all()
# SELECT brands.id AS brands_id, brands.name AS brands_name, brands.founded 
# AS brands_founded, brands.headquarters AS brands_headquarters, brands.discontinued 
# AS brands_discontinued 
# FROM brands 
# WHERE brands.founded < ? OR brands.discontinued IS NOT NULL
 # [<Brand id=1 name=Ford founded=1903 headquarters=Dearborn, MI discontinuedNone>,
 # <Brand id=2 name=Chrysler founded=1925 headquarters=Auburn Hills, Michigan discontinuedNone>,
 # <Brand id=3 name=Citro?n founded=1919 headquarters=Saint-Ouen, France discontinuedNone>, 
 # <Brand id=4 name=Hillman founded=1907 headquarters=Ryton-on-Dunsmore, England discontinued1981>,
 # <Brand id=5 name=Chevrolet founded=1911 headquarters=Detroit, Michigan discontinuedNone>,
 # <Brand id=6 name=Cadillac founded=1902 headquarters=New York City, NY discontinuedNone>,
 # <Brand id=7 name=BMW founded=1916 headquarters=Munich, Bavaria, Germany discontinuedNone>,
 # <Brand id=8 name=Austin founded=1905 headquarters=Longbridge, England discontinued1987>,
 # <Brand id=9 name=Fairthorpe founded=1954 headquarters=Chalfont St Peter, Buckinghamshire discontinued1976>,
 # <Brand id=10 name=Studebaker founded=1852 headquarters=South Bend, Indiana discontinued1967>,
 # <Brand id=11 name=Pontiac founded=1926 headquarters=Detroit, MI discontinued2010>,
 # <Brand id=12 name=Buick founded=1903 headquarters=Detroit, MI discontinuedNone>,
 # <Brand id=13 name=Rambler founded=1901 headquarters=Kenosha, Washington discontinued1969>,
 # <Brand id=14 name=Plymouth founded=1928 headquarters=Auburn Hills, Michigan discontinued2001>]

# Get any model whose brand_name is not Chevrolet.
not_chevy = Model.query.filter(Model.brand_name != "Chevrolet").all()
# SELECT models.id AS models_id, models.year AS models_year, models.brand_name
# AS models_brand_name, models.name AS models_name
# FROM models
# WHERE models.brand_name != ?

#  len(not_chevy)
# 34

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    # by_year = Model.query.filter(Model.year == year).all()
    # # is very slow because it will have to make a new SQL query for every item in the list
    # return [obj.brand.headquarters for obj in by_year]
    # use .join to make this faster -
    by_year = Model.query.filter(Model.year == year).options(db.joinedload('brand')).all()
    return [(obj.name, obj.brand_name, obj.brand.headquarters) for obj in by_year]

    # for 1950 returns: [(u'Minx Magnificent', u'Hillman', u'Ryton-on-Dunsmore, England')]

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    b_summary = db.session.query(Model.name, Brand.name).join(Brand).all()
    # SELECT models.name AS models_name, brands.name AS brands_name
    # FROM models JOIN brands ON brands.name = models.brand_name
    brand_dict = {}
    # key is Brand.name: value is [Model.name]
    for model_name, brand_name in b_summary:
        if brand_name in brand_dict:
            brand_dict[brand_name].append(model_name)
        # don't think this is correct
        else:
            brand_dict[brand_name] = [model_name]
    return brand_dict

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
    # class object? instance of the class Brand
# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
    # visulization tool to look at many-to-one or one-to-one relationships between
    # table fields
