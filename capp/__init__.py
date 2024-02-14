from flask import Flask

application = Flask(__name__)

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.display_media_query.routes import display_media_query
from capp.box_block_inline.routes import box_block_inline
from capp.weekly_challenge.routes import weekly

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(display_media_query)
application.register_blueprint(box_block_inline)
application.register_blueprint(weekly)
