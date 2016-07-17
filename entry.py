"""Entry point for the server"""

from best_conferences import app

app.run(host='0.0.0.0', port=9090, debug=True)
