from application import app, db
from flask import render_template, url_for, redirect,flash, get_flashed_messages
from application.form import UserInputForm
from application.models import IncomeExpenses

from application import app, db
db.create_all()


@app.route("/")
def index():
    entries = IncomeExpenses.query.order_by(IncomeExpenses.date.desc()).all()
    return render_template('index.html', title='index', entries=entries)

@app.route('/add', methods=["GET", "POST"])
def add_expense():
    form = UserInputForm()
    if form.validate_on_submit():
        entry = IncomeExpenses(type=form.type.data, category=form.category.data, amount=form.amount.data)
        db.session.add(entry)
        db.session.commit()
        flash("Successful entry", 'success')
        return redirect(url_for('index'))
    return render_template('add.html', title="add", form=form)

@app.route('/delete-post/<int:entry_id>')
def delete(entry_id):
    entry = IncomeExpenses.query.get_or_404(int(entry_id))
    db.session.delete(entry)
    db.session.commit()
    flash("Entry deleted", "success")
    return redirect(url_for("index"))
