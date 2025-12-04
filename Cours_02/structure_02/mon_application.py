from app.factbook import app, version

print(f'version application = {version}') #APP-2 séance 1. J'affiche en premier ma version, ici 0.0.1 (voir factbook.py)

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])

