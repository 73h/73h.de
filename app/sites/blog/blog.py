import datetime

from flask import Blueprint, flash, request, redirect, url_for, abort, Response, make_response, \
    render_template

from controller.blog.database import db
from controller.blog.login import user_login, user_logout, is_user_logged_in
from controller.blog.render import render
from models.blog.article import Article
from utils.config import HOSTNAME
from utils.http import Http

site_blog = Blueprint("blog", __name__)
host = f"blog.{HOSTNAME}"


@site_blog.get("/", host=host)
def index():
    db.connect()
    articles = db.get_articles(with_unpublished=is_user_logged_in())
    return render(site="index", title="A small tech blog.", articles=articles)


@site_blog.get("/article/<url>", host=host)
def get_article(url: str):
    db.connect()
    article = db.get_article(url)
    if article is not None:
        return render(site="article", title="A small tech blog.", article=article)
    abort(404)


@site_blog.post("/article/<url>", host=host)
def post_article(url: str):
    db.connect()
    article = db.get_article(url)
    if article is not None:
        if request.form.get('delete') is not None:
            db.delete_article(article)
            return redirect(url_for('blog.index'))
        article.title = request.form.get('title')
        article.update_url()
        article.content = request.form.get('content')
        article.published = request.form.get('published') is not None
        if not db.update_article(article):
            flash('Sorry, that did not work.')
            article = db.get_article(url)
            return render(site="article", title="A small tech blog.", article=article)
        return redirect(url_for('blog.get_article', url=article.url))
    abort(404)


@site_blog.post("/add-article", host=host)
def add_article():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    article = Article(title=now, content="")
    article.update_url()
    if not db.insert_article(article):
        flash('Sorry, that did not work.')
        return redirect(url_for('blog.index'))
    return redirect(url_for('blog.get_article', url=article.url))


@site_blog.get("/login", host=host)
def get_login():
    return render(site="login", title="Editor login.")


@site_blog.post("/login", host=host)
def post_login():
    if user_login(request.form.get('user'), request.form.get('password')):
        return redirect(url_for('blog.get_login'))
    flash('Sorry, this is wrong.')
    return render(site="login", title="Editor login.")


@site_blog.get("/logout", host=host)
def logout():
    user_logout()
    return redirect(url_for('blog.index'))


@site_blog.get("/impressum", host=host)
def impressum():
    return render(site="impressum", title="Impressum.")


@site_blog.get("/datenschutz", host=host)
def datenschutz():
    return render(site="datenschutz", title="Datenschutz.")


@site_blog.route("/robots.txt", host=host)
def noindex():
    http = Http()
    r = Response(response=f"User-Agent: *\nDisallow: /login\nSitemap: {http.url}/sitemap.xml\n", status=200,
                 mimetype="text/plain")
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r


@site_blog.get("/sitemap.xml", host=host)
def sitemap():
    http = Http()
    static_urls = list()
    static_urls.append({
        "loc": f"{http.url}"
    })
    static_roots = ["datenschutz", "impressum"]
    for root in static_roots:
        url = {
            "loc": f"{http.url}/{str(root)}"
        }
        static_urls.append(url)
    dynamic_urls = list()
    db.connect()
    articles = db.get_articles()
    for article in articles:
        url = {
            "loc": f"{http.url}/article/{article.url}",
            "lastmod": article.modified.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        dynamic_urls.append(url)
    xml = render_template("sitemap.xml", static_urls=static_urls, dynamic_urls=dynamic_urls, host_base=http.url)
    response = make_response(xml)
    response.headers["Content-Type"] = "application/xml"
    return response
