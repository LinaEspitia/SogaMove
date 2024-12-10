from flask import Blueprint, jsonify, request, render_template
from models import db, TravelHistory
from models import db, User
from models import db, Comment
from flask import redirect, url_for
from flask import session


main_routes = Blueprint('main', __name__)

@main_routes.route('/travel_history', methods=['POST'])
def add_travel():
    data = request.get_json()
    new_travel = TravelHistory(
        start_location=data['start_location'],
        end_location=data['end_location'],
        timestamp=data['timestamp']
    )
    db.session.add(new_travel)
    db.session.commit()
    return jsonify(new_travel.to_dict()), 201

@main_routes.route('/travel_history', methods=['GET'])
def get_travel_history():
    travels = TravelHistory.query.all()
    return jsonify([travel.to_dict() for travel in travels])



@main_routes.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        new_user = User(
            document_type=data['document_type'],
            number_Id=data['number_Id'],
            birth_date=data['birth_date'],
            expedition_date=data['expedition_date'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=data['password']  # Asegúrate de encriptar la contraseña en producción
        )
        db.session.add(new_user)
        db.session.commit()
        session['user_id'] = new_user.id  # Almacenar el ID del usuario en la sesión
        return jsonify({"message": "Usuario registrado exitosamente"}), 200

    except Exception as e:
        db.session.rollback()
        print(f"Error al registrar usuario: {str(e)}")  # Imprimir el error para depuración
        return jsonify({"error": str(e)}), 500


@main_routes.route('/comentarios', methods=['GET'])
def comments():
    user_id = session.get('user_id')  # Obtener el ID desde la sesión
    if user_id:
        comments = Comment.query.filter_by(user_id=user_id).all()  # Consultar por el ID del usuario
        return render_template('comentarios.html', comments=comments)
    else:
        return redirect(url_for('login'))

# Ruta para obtener todos los comentarios
@main_routes.route('/comments', methods=['GET'])
def get_comments():
    comments = Comment.query.order_by(Comment.timestamp.desc()).all()
    return jsonify([comment.to_dict() for comment in comments])

# Ruta para crear un nuevo comentario
@main_routes.route('/comments', methods=['POST'])
def add_comment():
    data = request.get_json()

    try:
        user = User.query.get(data['user_id'])  # Buscar al usuario por ID
        if not user:
            return jsonify({"error": "Usuario no encontrado"}), 404

        new_comment = Comment(
            user_id=user.id,
            username=f"{user.first_name} {user.last_name}",
            content=data['content']
        )
        db.session.add(new_comment)
        db.session.commit()
        return jsonify(new_comment.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "No se pudo publicar el comentario", "details": str(e)}), 400

@main_routes.route('/perfil', methods=['GET'])
def user_profile():
    user_id = session.get('user_id')  # Obtener el ID desde la sesión
    if user_id:
        user = User.query.get(user_id)
        if user:
            return render_template('perfil.html', user=user)
        else:
            return "Usuario no encontrado", 404
    else:
        return redirect(url_for('login'))  # Redirigir si el usuario no está autenticado


@main_routes.route('/historial', methods=['GET'])
def travel_history():
    user_id = session.get('user_id')  # Obtener el ID desde la sesión
    if user_id:
        travels = TravelHistory.query.filter_by(user_id=user_id).all()  # Consultar por el ID del usuario
        return render_template('historial.html', travels=travels)
    else:
        return redirect(url_for('login'))

@main_routes.route('/logout')
def logout():
    session.pop('user_id', None)  # Eliminar el ID del usuario de la sesión
    return redirect(url_for('login'))  # Redirigir a la página de inicio de sesión