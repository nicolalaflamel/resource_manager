from flask import Flask, render_template, request, redirect, url_for
from models.models import EntryContent
from models.database import db_session
from sqlalchemy import or_
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    resources = EntryContent.query.all()
    text_input = request.args.get('search')
    if text_input is None or len(text_input) == 0:
        resources = EntryContent.query.all()
    else:
        resources = EntryContent.query.filter(or_(EntryContent.tag.like(text_input), EntryContent.title.like(text_input))).all()
    return render_template("index.html", resources=resources)

@app.route("/add",methods=["POST"])
def add():
    title = request.form.get("title")
    tag = request.form.get("tag")
    url = request.form.get("url")
    content = EntryContent(title, url, tag, datetime.now())
    db_session.add(content)
    db_session.commit()
    print(title)
    print(tag)
    print(url)
    return redirect(url_for('index'))

@app.route("/delete",methods=["POST"])
def delete():
    resource_id = request.form.get("resource_id")
    if resource_id:
        content_to_delete = EntryContent.query.get(resource_id)
        db_session.delete(content_to_delete)
        db_session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
