# Herramienta de Verificación de Correos en BreachDirectory

**Suni** es una herramienta desarrollada en Python que permite verificar la presencia de direcciones de correo electrónico en la base de datos de BreachDirectory, una API que recopila información sobre violaciones de datos y fugas de seguridad.

## Características

- **Verificación Masiva:** Permite la verificación de múltiples direcciones de correo electrónico a través de un archivo de texto.
- **Uso Sencillo:** Con un único comando puedes verificar todas las direcciones listadas en tu archivo.
- **Integración con BreachDirectory:** Utiliza la API de BreachDirectory para acceder a información actualizada sobre violaciones de datos.

## Instalación

```bash
git clone https://github.com/jafernandezm/breachdirectory_osint
cd breachdirectory_osint
```

# Uso
```bash
python3 breachdirectory.py correos.txt
```

```js
    "correo": "exmaple.com",
    "resultados": [
        {
            "email": "exmaple.com",
            "hash_password": true,
            "password": "48048***",
            "sha1": "XXXXXXXXXXXXXXXXXXXXXXXXX",
            "hash": "XXXXXXXXXXXXX",
            "sources": "XXXXXXXXXXX"
        },
        {
            "email": "exmaple.com",
            "hash_password": true,
            "password": "alexy*******",
            "sha1": "XXXXXXXXXXXXXXXXXXXX",
            "hash": "XXXXXXXXXXXXXXXXXXXXX",
            "sources": "XXXXXXXXXXXXX"
        }
    ]
```

