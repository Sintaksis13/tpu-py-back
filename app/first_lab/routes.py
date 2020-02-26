routes = dict()

def __init__():
    routes[Red] = '/color/red'
    routes[Blue] = '/color/blue'
    routes[Green] = '/color/green'
    routes[Yellow] = '/color/yellow'
    routes[White] = '/color'


class Red:
    def get(self):
        return jsonify({'color': 'red'})

class Blue:
    def get(self):
        return jsonify({'color': 'blue'})

class Green:
    def get(self):
        return jsonify({'color': 'green'})

class Yellow:
    def get(self):
        return jsonify({'color': 'yellow'})

class White:
    def get(self):
        return jsonify({'color': 'white'})