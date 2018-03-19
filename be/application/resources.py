from flask_restful import Resource


class MainPageResource(Resource):

    def get(self):
        return {'hello':'world'}
