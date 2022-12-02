# Documentacion
Esta es una aplicacion web utilizando el framework flask y bootstrap. Su proposito es ejemplificar un CRUD utilizando el recurso mensaje.
Los datos se guardan en la base de datos postgres utilizando migraciones.

Las dependencias del proyecto de gestionan con pipenv.

## Dependencias
Para correr este proyecto de necesita previamente tener instalado python 3 y su herramienta pip.
Para revisar si las tienes instalado debes ejecutar los siguientes comandos:
```
python -V
pip -V
```

El resultado debe indicar el número superior a 3.
Luego de clonar el repositorio y para instalar las dependencias debe ejecutar el comando 
`pipenv install`

## Migraciones
Para ejecutar las migraciones el comando es el siguiente:
```
flask db upgrade
```

En caso de modificar un modelo agregando o modificando un atributo , debemos generar una nueva migración con el comando 

```
flask db migrate -m "Mensaje de la migracion"
```

**not**:
Los comandos anteriores se deben ejecutar dentro de `pipenv shell`

## Levantando la aplicación
Para ejecutar el servidor de desarrollo el comando es el siguiente
```
flask --app app-- debug run
```

Cuando hacemos algun camnio en un modelo y necesitamos considerar esos datos tambien en la base de datos, hay que generar un nueva migracion

```
flask db migrate -m"mensaje de la migracion"
```


**nota**: Los comandos anterios se deben ejecuta dentro de 'pipenv shell'

## Blueprint

los blueprint permiten componer aplicaciones desde componentes pequeños. Cada componente es como una mini aplicación.  Permiten crear apliacaciones grandes manteniendolas simples.

## Modulos 

Para que los blueprint esten bien organizados, es mejor trabajarlos como modulos, es decir que esten dentro de una carpeta. Los modulos se pueden anidar, de hecho, nosotros hicimos el modulo `app` con su respectivo `__init__.py` y dentro tenemos otro módulo, como el módulo `messages` que es ademas u blueprint.

## Tarea 
Crear un nuevo recurso sencillo, sin base de datos, como blueprint bajo a url `/memes` y debe renderiar un html lleno de memes.

En una arquitectura para separar las responsabilidades en la manipulacion de las solicitudes y respuestas. Quien recibe las solicitdes es el controlador o en flask, las rutas.Los controladores se encargan de revisar que la solicitud cumpla con las caracteristicas necesarias para entregar una respuesta acorde (que tengo todos los datos). Si el controlador lo permite, se podria opcionalmente llamar al modelo para obtener o modificar los datos de la BBDD. Y finalmente enviar una respuesta que contenga la presentacion de la aplicacion. En nuestro caso la capa de presentacion comunmente conocida como Vistas (view) se llaman Templates.

Por lo tanto en Flask el MVC podria ser adaptado como MTR(Modelo, Template, Ruta), pero es lo mismo en terminos de separar la responsabilidad 