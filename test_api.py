""" Entire API - needs refactoring """
from flask import Flask
from flask_restful import abort, Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

# Temp data
episodes = {
    1: {"title": "Star Trek: The Original Series", "date": "1979-09-23"},
    2: {"title": "Star Trek: The Next Generation", "date": "1987-09-23"},
    3: {"title": "Star Trek: Voyager", "date": "1995-09-23"},
    # 4: {"title": "Star Trek: Deep Space Nine", "date": "1999-09-23"},
}

# Define required arguments for post
ep_post_args = reqparse.RequestParser()
ep_post_args.add_argument('title', type=str, required=True,
                          help='Episode title required')
ep_post_args.add_argument('date', type=str, required=True,
                          help='Date of episode\'s first air date required')

# Define possible arguments for put
ep_put_args = reqparse.RequestParser()
ep_put_args.add_argument('title', type=str)
ep_put_args.add_argument('date', type=str)


class AllEpisodes(Resource):
    """ Class defining methods for all episodes endpoint """

    def get(self):
        """ Define GET request made to /episodes endpoint """
        return episodes


class OneEpisode(Resource):
    """ Class defining methods for specific episode endpoint """

    def get(self, ep_id):
        """ Define GET request made to endpoint including ep_id """
        return episodes[ep_id]

    def post(self, ep_id):
        """ Define POST (add) request made to endpoint including ep_id """
        # Define arguments
        args = ep_post_args.parse_args()
        if ep_id in episodes:
            # If episode already exists, abort with 409 (conflict)
            abort(409, message="Episode {} already exists".format(ep_id))
        # Add episode to episodes dict
        episodes[ep_id] = {"title": args['title'], "date": args['date']}
        # Return episode with 201 (created)
        return episodes[ep_id], 201

    def put(self, ep_id):
        """ Define PUT (update) request made to endpoint including ep_id """
        args = ep_put_args.parse_args()
        if ep_id not in episodes:
            # If episode doesn't exist, abort with 404 (not found)
            abort(404, message="Episode {} doesn't exist".format(ep_id))
        # Update episode (only these fields allowed)
        if args['title']:
            episodes[ep_id]['title'] = args['title']
        if args['date']:
            episodes[ep_id]['date'] = args['date']
        return episodes[ep_id], 200

    def delete(self, ep_id):
        """ Define DELETE request made to endpoint including ep_id """
        if ep_id not in episodes:
            abort(404, message="Episode {} doesn't exist".format(ep_id))
        del episodes[ep_id]
        return '', 204


# Define endpoints matched to classes - routes essentially
api.add_resource(OneEpisode, '/api/v1/episodes/<int:ep_id>')
api.add_resource(AllEpisodes, '/api/v1/episodes')


if __name__ == '__main__':
    app.run(debug=True)
