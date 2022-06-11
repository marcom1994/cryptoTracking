# Next 3 rows are needs for the correct import of modules
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from flask import Flask
from src.launcher.CryptoTrackingMain import CryptoTrackingMain

app = Flask(__name__)




@app.route('/')
def main():
    cryptoTrackingLauncher = CryptoTrackingMain()
    cryptoTrackingLauncher.main()

if __name__ == "__main__":
    main()