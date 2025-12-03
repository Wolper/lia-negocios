import passlib.handlers.bcrypt as pass_bcrypt

# força usar o backend "bcrypt" nativo
pass_bcrypt._bcrypt = __import__("bcrypt")

# injeta atributo esperado
if not hasattr(pass_bcrypt._bcrypt, "__about__"):
    class About:
        __version__ = "4.0.0"
    pass_bcrypt._bcrypt.__about__ = About()
