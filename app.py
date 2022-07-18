from meine import app
from meine.models import Board, Posts, Users
from meine.views import *

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True)
    
