# Next 3 rows are needs for the correct import of modules
import os, sys
SCRIPT_DIR = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..\..\..'))
sys.path.append(os.path.dirname(SCRIPT_DIR))


from projects.cryptoTracking.src.launcher.CryptoTrackingMain import CryptoTrackingMain

#TODO: assicurarsi che non ci siano info personali nel progetto, creare un repo git e un file .gitignore con dentro configAPI.properties
# e configTelegram.properties
#TODO: Aggiungere il comando /info per ottenere informazioni sull'ultima call alle api



if __name__ == '__main__':
    cryptoTrackingLauncher = CryptoTrackingMain()
    cryptoTrackingLauncher.main()
    