def within(hitbox, x, y):
        if (x > hitbox["X1"] and x < hitbox["X2"] and y > hitbox["Y1"] and y < hitbox["Y2"]):
            return True
        else:
            return False 