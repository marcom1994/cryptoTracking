from flask import Flask
from projects.cryptoTracking.src.launcher.CryptoTrackingMain import CryptoTrackingMain

app = Flask(__name__)




@app.route('/')
def home():
    cryptoTrackingLauncher = CryptoTrackingMain()
    cryptoTrackingLauncher.main()

