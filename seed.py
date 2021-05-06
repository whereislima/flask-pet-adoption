from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

Oscar = Pet(name="Oscar", species="dog", photo_url="https://bit.ly/3vLtzsr", age=8, notes="mellow, introverted, husky", available=True)
Porky = Pet(name="Porky", species="porcupine", photo_url="https://bit.ly/3vNZV5I", age=3, notes="loves to eat pumpkin and make cute noises", available=True)
Umi = Pet(name="Umi", species="cat", photo_url="https://bit.ly/3vMs6SB", age=15, notes="hyper, friendly, sleeps a lot", available=False)
Miu = Pet(name="Miu", species="cat", photo_url="", age=15, notes="", available=False)



db.session.add_all([Oscar, Porky, Umi, Miu])
db.session.commit()

