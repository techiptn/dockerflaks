from app import app
import os

# checks if the run.py file has executed directly and not improted
# Run this command run the application in DEBUG mode
# Docker run -p 5000:5000 -e DEBUG=1 <image-name>
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=os.environ.get('DEBUG') == '1')
    # app.run(host='0.0.0.0', port=5000, debug=True)
