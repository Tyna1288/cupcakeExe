"""seed file to create smaple data for db"""

from models import db, connect_db, Cupcake
from cup import app


"""create tables"""
with app.app_context():
    db.drop_all()
    db.create_all()


    cupcakes = [
        Cupcake(id='1', flavor='Vanilla', size='Small', rating='7',
                image='https://images.unsplash.com/photo-1519869325930-281384150729?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=866&q=80'),
        Cupcake(id='2', flavor='Chocholate', size='Large', rating='9',
                image='https://images.unsplash.com/photo-1426869884541-df7117556757?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=870&q=80'),
        Cupcake(id='3', flavor='Strawberry', size='Medium', rating='6',
                image='https://media.istockphoto.com/id/167120918/photo/pink-and-white-frosted-cupcake-isolated-on-white.jpg?s=1024x1024&w=is&k=20&c=QxtunnwldZiQBg8khDn86GRr-6sxqEyeVsZp25GpY1A='),
        Cupcake(id='4', flavor='Lemon', size='Large', rating='8',
                image='https://images.unsplash.com/photo-1576618148400-f54bed99fcfd?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=580&q=80'),
        Cupcake(id='5', flavor='Redvelvet', size='Small', rating='5',
                image='https://media.istockphoto.com/id/1457502416/photo/red-velvet-cupcakes-on-a-cooling-rack.webp?b=1&s=170667a&w=0&k=20&c=5wPORXxxlqPjmCylQemtKCA_hxctX7RlKnvMvm8i6XY=')
    ]

    db.session.add_all(cupcakes)
    db.session.commit()

