from flask import Flask, jsonify, request, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


usuarios = [
    {
        "id": 1,
        "user": "profecarlos",
        "password": "clave1",
        "nombre": "Carlos Andrade",
        "perfil": 1,
        "correo": "docente@gmail.com",
        "fotoPerfil": "imagen_profecarlos.png"
    },
    {
        "id": 2,
        "user": "profeana",
        "password": "clave2",
        "nombre": "Ana Torres",
        "perfil": 1,  
        "correo": "ana.torres@gmail.com",
        "fotoPerfil": "imagen_profeana.png"
    },
    {
        "id": 3,
        "user": "profemarco",
        "password": "clave3",
        "nombre": "Marco Alvarez",
        "perfil": 1,
        "correo": "marco.alvarez@gmail.com",
        "fotoPerfil": "imagen_profemarco.png"
    },
    {
        "id": 4,
        "user": "profemarta",
        "password": "clave4",
        "nombre": "Marta Sánchez",
        "perfil": 1,
        "correo": "marta.sanchez@gmail.com",
        "fotoPerfil": "imagen_profemarta.png"
    },
    {
        "id": 5,
        "user": "profesofia",
        "password": "clave5",
        "nombre": "Sofía Rojas",
        "perfil": 1,
        "correo": "sofia.rojas@gmail.com",
        "fotoPerfil": "imagen_profesofia.png"
    },
    {
    "id": 6,
    "user": "valentin",
    "password": "clave1",
    "nombre": "Valentin Navarro",
    "perfil": 2,
    "correo": "valentin.navarro@gmail.com",
    "fotoPerfil": "valentinnavarro.png"
  },
  {
    "id": 7,
    "user": "mariaruiz",
    "password": "clave2",
    "nombre": "Maria Ruiz",
    "perfil": 2,
    "correo": "maria.ruiz@gmail.com",
    "fotoPerfil": "mariaruiz.png"
  },
  {
    "id": 8,
    "user": "ian",
    "password": "clave3",
    "nombre": "Ian Lopez",
    "perfil": 2,
    "correo": "ian.lopez@gmail.com",
    "fotoPerfil": "ianlopez.png"
  },
  {
    "id": 9,
    "user": "fernando",
    "password": "clave4",
    "nombre": "Fernando Alvarez",
    "perfil": 2,
    "correo": "fernando.alvarez@gmail.com",
    "fotoPerfil": "fernandoalvarez.png"
  },
  {
    "id": 10,
    "user": "contigonzalez",
    "password": "clave5",
    "nombre": "Constanza Gonzalez",
    "perfil": 2,
    "correo": "conti.gonzalez@gmail.com",
    "fotoPerfil": "contigonzalez.png"
  }
]

profesores = [
    {
        "id": 1,
        "nombre": "Carlos Andrade",
        "cursos": [
            {
                "id": 1,
                "nombre": "Inglés",
                "codigo": "ING0001",
                "seccion": "013V",
                "imagen": "ingles.png",
                "alumnos": [
                    {"id": 1, "nombre": "Luis", "apellido": "Gómez", "rut": "18.765.432-1", "status": 0},
                    {"id": 2, "nombre": "María", "apellido": "Torres", "rut": "12.345.678-9", "status": 1},
                    {"id": 3, "nombre": "Carlos", "apellido": "Pérez", "rut": "13.876.234-5", "status": 0},
                    {"id": 4, "nombre": "Ana", "apellido": "Ramírez", "rut": "21.567.891-2", "status": 1},
                    {"id": 5, "nombre": "Pedro", "apellido": "Sánchez", "rut": "16.543.210-3", "status": 0},
                    {"id": 6, "nombre": "Valentin", "apellido": "Navarro", "rut": "19.432.567-8", "status": 0},
                    {"id": 7, "nombre": "Miguel", "apellido": "Hernández", "rut": "11.234.567-4", "status": 0},
                    {"id": 8, "nombre": "Ian", "apellido": "Lopez", "rut": "10.987.654-3", "status": 0},
                    {"id": 9, "nombre": "Clara", "apellido": "Vargas", "rut": "14.321.098-7", "status": 0},
                    {"id": 10, "nombre": "Fernando", "apellido": "Figueroa", "rut": "17.654.321-6", "status": 0},
                    {"id": 10, "nombre": "Fernando", "apellido": "Figueroa", "rut": "17.654.321-6", "status": 0},
                    {"id": 10, "nombre": "Fernando", "apellido": "Figueroa", "rut": "17.654.321-6", "status": 0},
                    {"id": 10, "nombre": "Mariana", "apellido": "Diaz", "rut": "17.654.321-6", "status": 0}
                ]
            },
            {
                "id": 2,
                "nombre": "Español",
                "codigo": "ESP0001",
                "seccion": "015V",
                "imagen": "espana.png",
                "alumnos": [
                    {"id": 11, "nombre": "Valeria", "apellido": "Bravo", "rut": "22.765.431-0", "status": 0},
                    {"id": 12, "nombre": "Iván", "apellido": "Ortiz", "rut": "13.654.987-1", "status": 0},
                    {"id": 13, "nombre": "Rosa", "apellido": "Mendoza", "rut": "19.876.543-0", "status": 0},
                    {"id": 14, "nombre": "Daniel", "apellido": "Vera", "rut": "21.654.987-2", "status": 0},
                    {"id": 15, "nombre": "Mónica", "apellido": "Navarro", "rut": "14.765.321-9", "status": 0},
                    {"id": 16, "nombre": "Raúl", "apellido": "Paredes", "rut": "17.890.123-5", "status": 0},
                    {"id": 17, "nombre": "Elena", "apellido": "Morales", "rut": "16.543.987-8", "status": 0},
                    {"id": 18, "nombre": "Andrés", "apellido": "Fuentes", "rut": "18.654.321-7", "status": 0},
                    {"id": 19, "nombre": "Sara", "apellido": "Rojas", "rut": "13.432.109-5", "status": 0},
                    {"id": 20, "nombre": "Lucas", "apellido": "Lagos", "rut": "11.543.678-4", "status": 0}
                ]
            },
            {
                "id": 3,
                "nombre": "Portugués",
                "codigo": "POR0001",
                "seccion": "018V",
                "imagen": "portugal.png",
                "alumnos": [
                    {"id": 21, "nombre": "Gabriela", "apellido": "Fernández", "rut": "12.876.543-2", "status": 0},
                    {"id": 22, "nombre": "Rafael", "apellido": "García", "rut": "14.654.987-0", "status": 0},
                    {"id": 23, "nombre": "Isabel", "apellido": "Cárdenas", "rut": "19.098.765-4", "status": 0},
                    {"id": 24, "nombre": "José", "apellido": "Rivera", "rut": "21.543.876-1", "status": 0},
                    {"id": 25, "nombre": "Marta", "apellido": "Espinoza", "rut": "17.876.543-9", "status": 0},
                    {"id": 26, "nombre": "Cristina", "apellido": "Guzmán", "rut": "14.098.765-4", "status": 0},
                    {"id": 27, "nombre": "Sergio", "apellido": "Contreras", "rut": "18.765.432-1", "status": 0},
                    {"id": 28, "nombre": "Beatriz", "apellido": "Salinas", "rut": "13.432.567-2", "status": 0},
                    {"id": 29, "nombre": "Luis", "apellido": "Castillo", "rut": "16.543.098-5", "status": 0},
                    {"id": 30, "nombre": "Carla", "apellido": "Sepúlveda", "rut": "12.876.098-3", "status": 0}
                ]
            }
        ]
    },
    {
        "id": 2,
        "nombre": "Ana Torres",
        "cursos": [
            {
                "id": 4,
                "nombre": "Inglés",
                "codigo": "ING0002",
                "seccion": "014V",
                "imagen": "ingles.png",
                "alumnos": [
                    {"id": 31, "nombre": "Pedro", "apellido": "López", "rut": "19.123.456-7", "status": 0},
                    {"id": 32, "nombre": "Sofía", "apellido": "González", "rut": "16.432.198-0", "status": 0},
                    {"id": 33, "nombre": "Pablo", "apellido": "Jiménez", "rut": "13.876.543-2", "status": 0},
                    {"id": 34, "nombre": "Sara", "apellido": "Aguilar", "rut": "10.987.654-3", "status": 0},
                    {"id": 35, "nombre": "Martín", "apellido": "Flores", "rut": "18.765.432-1", "status": 0},
                    {"id": 36, "nombre": "Inés", "apellido": "Tapia", "rut": "14.654.321-9", "status": 0},
                    {"id": 37, "nombre": "Rodrigo", "apellido": "Cruz", "rut": "12.543.987-5", "status": 0},
                    {"id": 38, "nombre": "Elena", "apellido": "Díaz", "rut": "21.345.678-2", "status": 0},
                    {"id": 39, "nombre": "Manuel", "apellido": "Carrasco", "rut": "16.543.210-8", "status": 0},
                    {"id": 40, "nombre": "Teresa", "apellido": "León", "rut": "17.654.321-5", "status": 0}
                ]
            },
            {
                "id": 5,
                "nombre": "Francés",
                "codigo": "FRN0002",
                "seccion": "016V",
                "imagen": "francia.png",
                "alumnos": [
                    {"id": 41, "nombre": "Lucas", "apellido": "Ríos", "rut": "19.543.876-0", "status": 0},
                    {"id": 42, "nombre": "Camila", "apellido": "Soto", "rut": "18.432.543-1", "status": 0},
                    {"id": 43, "nombre": "Cristóbal", "apellido": "Valdés", "rut": "14.765.098-7", "status": 0},
                    {"id": 44, "nombre": "Santiago", "apellido": "Vidal", "rut": "10.123.654-3", "status": 0},
                    {"id": 45, "nombre": "Valentina", "apellido": "Ibáñez", "rut": "11.876.543-2", "status": 0},
                    {"id": 46, "nombre": "Emilia", "apellido": "Campos", "rut": "13.234.876-9", "status": 0},
                    {"id": 47, "nombre": "Hugo", "apellido": "Zúñiga", "rut": "17.654.123-4", "status": 0},
                    {"id": 48, "nombre": "Mariana", "apellido": "Jara", "rut": "12.543.987-0", "status": 0},
                    {"id": 49, "nombre": "Simón", "apellido": "Álvarez", "rut": "14.321.654-8", "status": 0},
                    {"id": 50, "nombre": "Álvaro", "apellido": "Pizarro", "rut": "19.098.765-1", "status": 0}
                ]
            },
            {
                "id": 6,
                "nombre": "Portugués",
                "codigo": "POR0002",
                "seccion": "017V",
                "imagen": "portugal.png",
                "alumnos": [
                    {"id": 51, "nombre": "Gabriela", "apellido": "Peña", "rut": "11.654.321-7", "status": 0},
                    {"id": 52, "nombre": "Rafael", "apellido": "Reyes", "rut": "12.543.678-2", "status": 0},
                    {"id": 53, "nombre": "Isabel", "apellido": "Correa", "rut": "15.987.654-3", "status": 0},
                    {"id": 54, "nombre": "José", "apellido": "Luna", "rut": "18.765.234-9", "status": 0},
                    {"id": 55, "nombre": "Marta", "apellido": "Olivares", "rut": "10.123.456-8", "status": 0},
                    {"id": 56, "nombre": "Cristina", "apellido": "Araya", "rut": "19.654.321-0", "status": 0},
                    {"id": 57, "nombre": "Sergio", "apellido": "Palma", "rut": "13.543.678-7", "status": 0},
                    {"id": 58, "nombre": "Beatriz", "apellido": "Arias", "rut": "21.987.654-5", "status": 0},
                    {"id": 59, "nombre": "Luis", "apellido": "Gatica", "rut": "17.432.543-2", "status": 0},
                    {"id": 60, "nombre": "Carla", "apellido": "Bravo", "rut": "16.654.321-9", "status": 0}
                ]
            }
        ]
    },
        {
        "id": 3,
        "nombre": "Marco Alvarez",
        "cursos": [
            {
                "id": 7,
                "nombre": "Holandés",
                "codigo": "ALE0001",
                "seccion": "019V",
                "imagen": "holanda.png",
                "alumnos": [
                    {"id": 61, "nombre": "Matías", "apellido": "López", "rut": "21.234.567-1", "status": 0},
                    {"id": 62, "nombre": "Sandra", "apellido": "Soto", "rut": "19.876.543-2", "status": 0},
                    {"id": 63, "nombre": "José", "apellido": "Hernández", "rut": "18.543.678-9", "status": 0},
                    {"id": 64, "nombre": "Cristina", "apellido": "Bravo", "rut": "17.654.321-4", "status": 0},
                    {"id": 65, "nombre": "Tomás", "apellido": "Castillo", "rut": "14.321.765-5", "status": 0},
                    {"id": 66, "nombre": "Patricia", "apellido": "Morales", "rut": "12.432.098-7", "status": 0},
                    {"id": 67, "nombre": "Gonzalo", "apellido": "Jiménez", "rut": "10.876.543-2", "status": 0},
                    {"id": 68, "nombre": "Alejandra", "apellido": "Valenzuela", "rut": "20.123.654-8", "status": 0},
                    {"id": 69, "nombre": "Julieta", "apellido": "Rivas", "rut": "15.432.987-0", "status": 0},
                    {"id": 70, "nombre": "Diego", "apellido": "Ortiz", "rut": "13.654.987-1", "status": 0}
                ]
            },
            {
                "id": 8,
                "nombre": "Italiano",
                "codigo": "ITA0001",
                "seccion": "020V",
                "imagen": "italia.png",
                "alumnos": [
                    {"id": 71, "nombre": "Roberto", "apellido": "Carrasco", "rut": "18.543.765-3", "status": 0},
                    {"id": 72, "nombre": "Verónica", "apellido": "Garrido", "rut": "16.987.432-9", "status": 0},
                    {"id": 73, "nombre": "Lucía", "apellido": "Campos", "rut": "14.543.678-2", "status": 0},
                    {"id": 74, "nombre": "Alfredo", "apellido": "Peña", "rut": "19.876.543-2", "status": 0},
                    {"id": 75, "nombre": "María", "apellido": "Molina", "rut": "21.098.765-7", "status": 0},
                    {"id": 76, "nombre": "Miguel", "apellido": "Navarrete", "rut": "17.432.765-8", "status": 0},
                    {"id": 77, "nombre": "Alicia", "apellido": "Fuentes", "rut": "15.321.654-3", "status": 0},
                    {"id": 78, "nombre": "José", "apellido": "Rojas", "rut": "20.432.876-0", "status": 0},
                    {"id": 79, "nombre": "Carmen", "apellido": "Pizarro", "rut": "22.098.654-1", "status": 0},
                    {"id": 80, "nombre": "Enrique", "apellido": "Aravena", "rut": "13.987.432-6", "status": 0}
                ]
            },
            {
                "id": 9,
                "nombre": "Ruso",
                "codigo": "RUS0001",
                "seccion": "021V",
                "imagen": "rusia.png",
                "alumnos": [
                    {"id": 81, "nombre": "Tatiana", "apellido": "González", "rut": "10.876.543-4", "status": 0},
                    {"id": 82, "nombre": "Igor", "apellido": "Ramírez", "rut": "11.234.567-8", "status": 0},
                    {"id": 83, "nombre": "Anastasia", "apellido": "Vera", "rut": "19.654.321-2", "status": 0},
                    {"id": 84, "nombre": "Vladimir", "apellido": "Figueroa", "rut": "21.876.543-5", "status": 0},
                    {"id": 85, "nombre": "Svetlana", "apellido": "Olivares", "rut": "14.321.876-0", "status": 0},
                    {"id": 86, "nombre": "Nikolai", "apellido": "Cáceres", "rut": "17.098.765-3", "status": 0},
                    {"id": 87, "nombre": "Olga", "apellido": "Pineda", "rut": "19.432.876-9", "status": 0},
                    {"id": 88, "nombre": "Boris", "apellido": "Cornejo", "rut": "15.765.432-2", "status": 0},
                    {"id": 89, "nombre": "Elena", "apellido": "Riquelme", "rut": "18.987.654-6", "status": 0},
                    {"id": 90, "nombre": "Mikhail", "apellido": "Mora", "rut": "16.543.789-1", "status": 0}
                ]
            }
        ]
    },
    {
        "id": 4,
        "nombre": "Marta Sánchez",
        "cursos": [
            {
                "id": 10,
                "nombre": "Chino",
                "codigo": "CHI0001",
                "seccion": "022V",
                "imagen": "china.png",
                "alumnos": [
                    {"id": 91, "nombre": "Cristina", "apellido": "Hernández", "rut": "18.765.432-0", "status": 0},
                    {"id": 92, "nombre": "Patricio", "apellido": "Fernández", "rut": "19.543.678-1", "status": 0},
                    {"id": 93, "nombre": "Andrés", "apellido": "Tapia", "rut": "20.987.654-5", "status": 0},
                    {"id": 94, "nombre": "Constanza", "apellido": "Vega", "rut": "17.876.543-9", "status": 0},
                    {"id": 95, "nombre": "Rodrigo", "apellido": "López", "rut": "19.432.109-3", "status": 0},
                    {"id": 96, "nombre": "Camila", "apellido": "Bravo", "rut": "21.098.765-6", "status": 0},
                    {"id": 97, "nombre": "Javier", "apellido": "Ortiz", "rut": "16.543.987-1", "status": 0},
                    {"id": 98, "nombre": "Tomás", "apellido": "Morales", "rut": "10.654.321-2", "status": 0},
                    {"id": 99, "nombre": "Esteban", "apellido": "Muñoz", "rut": "14.543.876-4", "status": 0},
                    {"id": 100, "nombre": "Pablo", "apellido": "Navarro", "rut": "18.432.654-9", "status": 0}
                ]
            },
            {
                "id": 11,
                "nombre": "Japonés",
                "codigo": "JAP0001",
                "seccion": "023V",
                "imagen": "japon.png",
                "alumnos": [
                    {"id": 101, "nombre": "Isidora", "apellido": "Rivas", "rut": "12.432.109-5", "status": 0},
                    {"id": 102, "nombre": "Benjamín", "apellido": "Pizarro", "rut": "16.765.432-9", "status": 0},
                    {"id": 103, "nombre": "Valentina", "apellido": "Fuentes", "rut": "14.543.678-2", "status": 0},
                    {"id": 104, "nombre": "Catalina", "apellido": "Peña", "rut": "19.876.543-2", "status": 0},
                    {"id": 105, "nombre": "Francisco", "apellido": "Molina", "rut": "21.098.765-7", "status": 0},
                    {"id": 106, "nombre": "Tomás", "apellido": "Navarrete", "rut": "17.432.765-8", "status": 0},
                    {"id": 107, "nombre": "Amanda", "apellido": "Fuentes", "rut": "15.321.654-3", "status": 0},
                    {"id": 108, "nombre": "Sebastián", "apellido": "Rojas", "rut": "20.432.876-0", "status": 0},
                    {"id": 109, "nombre": "Agustín", "apellido": "Pizarro", "rut": "22.098.654-1", "status": 0},
                    {"id": 110, "nombre": "Javiera", "apellido": "Aravena", "rut": "13.987.432-6", "status": 0}
                ]
            },
            {
                "id": 12,
                "nombre": "Coreano",
                "codigo": "COR0001",
                "seccion": "024V",
                "imagen": "corea.png",
                "alumnos": [
                    {"id": 111, "nombre": "Ignacio", "apellido": "Reyes", "rut": "18.432.765-0", "status": 0},
                    {"id": 112, "nombre": "Fernanda", "apellido": "Cáceres", "rut": "17.987.543-6", "status": 0},
                    {"id": 113, "nombre": "Manuel", "apellido": "Rivera", "rut": "16.543.876-4", "status": 0},
                    {"id": 114, "nombre": "Gabriela", "apellido": "Pérez", "rut": "20.432.987-1", "status": 0},
                    {"id": 115, "nombre": "Pablo", "apellido": "Zamorano", "rut": "15.098.654-2", "status": 0},
                    {"id": 116, "nombre": "Daniela", "apellido": "Jiménez", "rut": "14.765.987-0", "status": 0},
                    {"id": 117, "nombre": "Nicolás", "apellido": "Espinoza", "rut": "21.876.543-9", "status": 0},
                    {"id": 118, "nombre": "Rocío", "apellido": "Valdés", "rut": "19.654.987-4", "status": 0},
                    {"id": 119, "nombre": "Renato", "apellido": "Vargas", "rut": "16.432.198-7", "status": 0},
                    {"id": 120, "nombre": "Daniel", "apellido": "Baeza", "rut": "13.765.098-3", "status": 0}
                ]
            }
        ]
    },
    {
        "id": 5,
        "nombre": "Sofía Rojas",
        "cursos": [
            {
                "id": 13,
                "nombre": "Árabe",
                "codigo": "ARA0001",
                "seccion": "025V",
                "imagen": "united-arab-emirates.png",
                "alumnos": [
                    {"id": 121, "nombre": "Felipe", "apellido": "Ramírez", "rut": "11.987.654-3", "status": 0},
                    {"id": 122, "nombre": "Gabriel", "apellido": "Martínez", "rut": "19.876.543-1", "status": 0},
                    {"id": 123, "nombre": "Constanza", "apellido": "Gutiérrez", "rut": "18.543.210-9", "status": 0},
                    {"id": 124, "nombre": "Matías", "apellido": "Vargas", "rut": "17.432.654-8", "status": 0},
                    {"id": 125, "nombre": "Paula", "apellido": "Salinas", "rut": "16.876.543-4", "status": 0},
                    {"id": 126, "nombre": "Vicente", "apellido": "Gómez", "rut": "15.987.654-7", "status": 0},
                    {"id": 127, "nombre": "Daniela", "apellido": "Vega", "rut": "14.543.987-1", "status": 0},
                    {"id": 128, "nombre": "Francisca", "apellido": "Contreras", "rut": "19.432.765-6", "status": 0},
                    {"id": 129, "nombre": "Agustín", "apellido": "Carrasco", "rut": "21.654.321-0", "status": 0},
                    {"id": 130, "nombre": "Ignacio", "apellido": "Sánchez", "rut": "20.543.987-4", "status": 0}
                ]
            },
            {
                "id": 14,
                "nombre": "Turco",
                "codigo": "TUR0001",
                "seccion": "026V",
                "imagen": "turquia.png",
                "alumnos": [
                    {"id": 131, "nombre": "Joaquín", "apellido": "Figueroa", "rut": "17.432.987-9", "status": 0},
                    {"id": 132, "nombre": "Emilia", "apellido": "Rojas", "rut": "19.654.321-0", "status": 0},
                    {"id": 133, "nombre": "Nicolás", "apellido": "Moreno", "rut": "21.098.765-4", "status": 0},
                    {"id": 134, "nombre": "Antonia", "apellido": "Silva", "rut": "20.432.876-2", "status": 0},
                    {"id": 135, "nombre": "Cristóbal", "apellido": "Pérez", "rut": "19.876.543-5", "status": 0},
                    {"id": 136, "nombre": "Isidora", "apellido": "Álvarez", "rut": "15.432.987-1", "status": 0},
                    {"id": 137, "nombre": "Vicente", "apellido": "Reyes", "rut": "13.876.543-7", "status": 0},
                    {"id": 138, "nombre": "Amanda", "apellido": "Correa", "rut": "18.765.432-9", "status": 0},
                    {"id": 139, "nombre": "Pablo", "apellido": "Acuña", "rut": "16.543.987-2", "status": 0},
                    {"id": 140, "nombre": "Benjamín", "apellido": "Riquelme", "rut": "14.654.321-6", "status": 0}
                ]
            },
            {
                "id": 15,
                "nombre": "Hebreo",
                "codigo": "HEB0001",
                "seccion": "027V",
                "imagen": "israel.png",
                "alumnos": [
                    {"id": 141, "nombre": "Martín", "apellido": "Lara", "rut": "20.543.987-9", "status": 0},
                    {"id": 142, "nombre": "Daniel", "apellido": "Palacios", "rut": "17.987.654-6", "status": 0},
                    {"id": 143, "nombre": "Andrea", "apellido": "Ruiz", "rut": "18.654.321-7", "status": 0},
                    {"id": 144, "nombre": "Sofía", "apellido": "Espinoza", "rut": "19.432.876-2", "status": 0},
                    {"id": 145, "nombre": "Tomás", "apellido": "Salazar", "rut": "16.543.987-3", "status": 0},
                    {"id": 146, "nombre": "Bárbara", "apellido": "Cruz", "rut": "13.765.098-2", "status": 0},
                    {"id": 147, "nombre": "Gonzalo", "apellido": "Zambrano", "rut": "21.098.654-0", "status": 0},
                    {"id": 148, "nombre": "Catalina", "apellido": "Muñoz", "rut": "14.543.876-9", "status": 0},
                    {"id": 149, "nombre": "Valentina", "apellido": "Farfán", "rut": "19.765.432-8", "status": 0},
                    {"id": 150, "nombre": "Sebastián", "apellido": "Gallardo", "rut": "10.432.654-1", "status": 0}
                ]
            }
        ]
    }

]

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('user')
    password = request.json.get('password')
    
    usuario = next((u for u in usuarios if u["user"] == username and u["password"] == password), None)
    
    if usuario:
        if "fotoPerfil" in usuario:
            fotoPerfilUrl = url_for('static', filename=f'images/{usuario["fotoPerfil"]}', _external=True)
        else:
            fotoPerfilUrl = None  
        
        return jsonify({
            "id": usuario["id"],
            "nombre": usuario["nombre"],
            "user": usuario["user"],
            "correo": usuario["correo"],
            "tipoPerfil": usuario["perfil"],
            "fotoPerfil": fotoPerfilUrl  
        }), 200
    else:
        return jsonify({"message": "Credenciales incorrectas"}), 401

@app.route('/profesores', methods=['GET'])
def obtener_profesores():
   return jsonify(profesores), 



@app.route('/profesores/<int:profesor_id>/cursos', methods=['GET'])
def obtener_cursos_profesor(profesor_id):
    profesor = next((p for p in profesores if p["id"] == profesor_id), None)
    if not profesor:
        return jsonify({"message": "Profesor no encontrado"}), 404
    
 
    for curso in profesor["cursos"]:
        if not curso["imagen"].startswith('http'):
            curso["imagen"] = url_for('static', filename=f'images/{curso["imagen"]}', _external=True)
    
    return jsonify(profesor["cursos"]), 200

@app.route('/profesores/<int:profesor_id>/cursos/<int:curso_id>/alumnos/<int:alumno_id>/asistencia', methods=['PUT'])
def actualizar_asistencia(profesor_id, curso_id, alumno_id):
    # Buscar el profesor por su ID
    profesor = next((p for p in profesores if p["id"] == profesor_id), None)
    if not profesor:
        return jsonify({"message": "Profesor no encontrado"}), 404

    # Buscar el curso por su ID en la lista del profesor
    curso = next((c for c in profesor["cursos"] if c["id"] == curso_id), None)
    if not curso:
        return jsonify({"message": "Curso no encontrado"}), 404

    # Buscar el alumno por su ID en la lista del curso
    alumno = next((a for a in curso["alumnos"] if a["id"] == alumno_id), None)
    if not alumno:
        return jsonify({"message": "Alumno no encontrado"}), 404

    # Cambiar el estado de asistencia del alumno a "presente"
    alumno["status"] = 1

    return jsonify({"message": "Asistencia actualizada correctamente", "alumno": alumno}), 200



@app.route('/cursos/<int:curso_id>/profesor', methods=['GET'])
def obtener_profesor_por_curso(curso_id):
    for profesor in profesores:
        for curso in profesor["cursos"]:
            if curso["id"] == curso_id:
                return jsonify({"profesor_id": profesor["id"]}), 200
    return jsonify({"message": "Profesor no encontrado"}), 404

@app.route('/cursos/<int:curso_id>/alumnos', methods=['GET'])
def obtener_alumnos_por_curso(curso_id):
    # Recorre la lista de profesores y sus cursos para encontrar el curso solicitado
    for profesor in profesores:
        curso = next((c for c in profesor["cursos"] if c["id"] == curso_id), None)
        if curso:
            # Devuelve la lista de alumnos del curso
            return jsonify({"alumnos": curso["alumnos"]}), 200
    return jsonify({"message": "Curso no encontrado"}), 404







if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

