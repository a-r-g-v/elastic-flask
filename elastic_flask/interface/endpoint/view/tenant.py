from flask_classful import FlaskView
from webargs.flaskparser import use_args


class TenantView(FlaskView):

    def get(self, id):
        return id

