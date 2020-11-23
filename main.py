from Box2D import b2World, b2PolygonShape

dt = 1.0/60.0
vel_iters, pos_iters = 10, 10

world = b2World()
groundBody = world.CreateStaticBody(
        position=(0,-10),
        shapes=b2PolygonShape(box=(50,10))
        )

body = world.CreateDynamicBody(position=(0,4))
box = body.CreatePolygonFixture(box=(1,1), density=1, friction=.3)

for _ in range(60):
    world.Step(dt, vel_iters, pos_iters)
    world.ClearForces()

    print(body.position, body.angle)
