# Importando __init__.py
from todor import create_app

# Validación de la función create_app
if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
