from flask import Flask, request, jsonify, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

# Configuration de la base de données
username = 'root'
password = 'rootpassword'
host = 'mysql'  # Nom du service Docker
dbname = 'yourdatabase'
DATABASE_URL = f'mysql+mysqlconnector://{username}:{password}@{host}/{dbname}'

# Création de l'objet Engine
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Définition du modèle Employé
class Employe(Base):
    __tablename__ = 'employe'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String(100))
    prenom = Column(String(100))
    email = Column(String(100))
    date_embauche = Column(Date)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    session = Session()
    print(data)
    new_employee = Employe(
        nom=data['nom'],
        prenom=data['prenom'],
        email=data['email'],
        date_embauche=data['date_embauche']
    )
    session.add(new_employee)
    session.commit()
    session.close()
    return jsonify({'message': 'Employé ajouté avec succès !'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)
