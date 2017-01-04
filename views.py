from flask import Flask, flash, redirect, render_template, request, session,\
 url_for
from flask_sqlalchemy import SQLAlchemy
from forms import NewMenuItem, EditMenuItem

# config
app = Flask(__name__)
app.config.from_object('_config')
db = SQLAlchemy(app)
from models import Restaurant, MenuItem

@app.route('/')
@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).first()
    items = db.session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    return render_template('items.html',
            items=items, restaurant=restaurant)

@app.route('/restaurant/<int:restaurant_id>', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).first()
    form = NewMenuItem()
    if request.method == 'POST':
        if form.validate_on_submit():
            newItem = MenuItem(
                form.name.data,
                form.description.data,
                form.price.data,
                restaurant
            )
            db.session.add(newItem)
            db.session.commit()
            return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    return render_template('newmenuitem.html', form=form, restaurant_id=restaurant_id)


@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    form = EditMenuItem()
    restaurant = db.session.query(Restaurant).filter_by(id=restaurant_id).first()
    editItem = db.session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        editItem.name = form.name.data
        editItem.description = form.description.data
        editItem.price = form.price.data
        editItem.restaurant_id = restaurant.id

        db.session.add(editItem)
        db.session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', form=form,\
                        restaurant_id=restaurant_id, item=editItem)

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/', methods=['POST', 'GET'])
def deleteMenuItem(restaurant_id, menu_id):
    deleteItem = db.session.query(MenuItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        db.session.delete(deleteItem)
        db.session.commit()
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deletemenuitem.html',\
            item=deleteItem, restaurant_id=restaurant_id)
