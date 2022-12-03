from flask import Blueprint, render_template, Response, make_response

from utils.config import HOSTNAME
from utils.http import Http

site_home = Blueprint("home", __name__)


@site_home.get("/", host=HOSTNAME)
@site_home.get("/", host=f"www.{HOSTNAME}")
def index():
    return render_template("home/index.html")


@site_home.route("/robots.txt", host=HOSTNAME)
@site_home.route("/robots.txt", host=f"www.{HOSTNAME}")
def noindex():
    http = Http()
    r = Response(response=f"User-Agent: *\nDisallow: /\nSitemap: {http.url}/sitemap.xml\n", status=200,
                 mimetype="text/plain")
    r.headers["Content-Type"] = "text/plain; charset=utf-8"
    return r


@site_home.get("/sitemap.xml", host=HOSTNAME)
@site_home.get("/sitemap.xml", host=f"www.{HOSTNAME}")
def sitemap():
    http = Http()
    static_urls = list()
    static_urls.append({
        "loc": f"{http.url}"
    })
    xml = render_template("sitemap.xml", static_urls=static_urls, dynamic_urls=list(), host_base=http.url)
    response = make_response(xml)
    response.headers["Content-Type"] = "application/xml"
    return response
