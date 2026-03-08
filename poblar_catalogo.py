import os
import django

# Asegúrate de cambiar 'biblioteca_project' por el nombre real de la carpeta principal de tu proyecto (donde está el settings.py)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'biblioteca_project.settings')
django.setup()

# --- AQUÍ DEBAJO VA EL RESTO DEL CÓDIGO QUE YA TIENES ---
from decimal import Decimal
from libros.models import Categoria, Autor, Libro

from decimal import Decimal
from libros.models import Categoria, Autor, Libro

def poblar_catalogo():
    print("📚 Iniciando carga de datos...")

    # ==========================================
    # 1. CREAR CATEGORÍAS (3)
    # ==========================================
    cat_ficcion, _ = Categoria.objects.get_or_create(
        nombre='Ficción', 
        defaults={'descripcion': 'Obras literarias basadas en la imaginación y narrativa.'}
    )
    cat_ciencia, _ = Categoria.objects.get_or_create(
        nombre='Ciencia Ficción', 
        defaults={'descripcion': 'Historias con elementos tecnológicos y científicos futuros.'}
    )
    cat_software, _ = Categoria.objects.get_or_create(
        nombre='Desarrollo de Software', 
        defaults={'descripcion': 'Libros técnicos sobre programación y arquitectura de software.'}
    )
    print("✅ 3 Categorías listas.")

    # ==========================================
    # 2. CREAR AUTORES (6)
    # ==========================================
    autores_data = [
        ('Gabriel', 'García Márquez'),
        ('Isaac', 'Asimov'),
        ('Robert C.', 'Martin'),
        ('J.K.', 'Rowling'),
        ('George', 'Orwell'),
        ('J.R.R.', 'Tolkien')
    ]
    
    # Guardamos los objetos de autor en un diccionario para usarlos al crear los libros
    autores_db = {}
    for nombre, apellido in autores_data:
        autor, _ = Autor.objects.get_or_create(nombre=nombre, apellido=apellido)
        autores_db[apellido] = autor
        
    print("✅ 6 Autores listos.")

    # ==========================================
    # 3. CREAR LIBROS (6)
    # ==========================================
    libros_data = [
        {
            'titulo': 'Cien años de soledad', 
            'isbn': '9780307474728', 
            'autor': autores_db['García Márquez'], 
            'categoria': cat_ficcion, 
            'precio': Decimal('550.00')
        },
        {
            'titulo': 'Fundación', 
            'isbn': '9788499083209', 
            'autor': autores_db['Asimov'], 
            'categoria': cat_ciencia, 
            'precio': Decimal('480.00')
        },
        {
            'titulo': 'Clean Code', 
            'isbn': '9780132350884', 
            'autor': autores_db['Martin'], 
            'categoria': cat_software, 
            'precio': Decimal('1250.50')
        },
        {
            'titulo': 'Harry Potter y la piedra filosofal', 
            'isbn': '9788498384376', 
            'autor': autores_db['Rowling'], 
            'categoria': cat_ficcion, 
            'precio': Decimal('620.00')
        },
        {
            'titulo': '1984', 
            'isbn': '9780451524935', 
            'autor': autores_db['Orwell'], 
            'categoria': cat_ciencia, 
            'precio': Decimal('400.00')
        },
        {
            'titulo': 'El Señor de los Anillos: La Comunidad del Anillo', 
            'isbn': '9788445071793', 
            'autor': autores_db['Tolkien'], 
            'categoria': cat_ficcion, 
            'precio': Decimal('890.00')
        }
    ]

    for data in libros_data:
        Libro.objects.get_or_create(
            isbn=data['isbn'],  # El ISBN es único, lo usamos para buscar si ya existe
            defaults={
                'titulo': data['titulo'],
                'autor': data['autor'],
                'categoria': data['categoria'],
                'precio': data['precio'],
                'stock': 5, # Les ponemos 5 de stock a todos por defecto
                'estado': Libro.DISPONIBLE
            }
        )
        
    print("✅ 6 Libros listos.")
    print("🚀 ¡Catálogo poblado exitosamente!")

# Ejecutar la función
poblar_catalogo()