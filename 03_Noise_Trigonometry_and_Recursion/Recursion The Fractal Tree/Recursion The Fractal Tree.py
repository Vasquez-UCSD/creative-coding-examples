def branch(length):
    line(0, 0, 0, -length)
    translate(0, -length)
    if length > 4:
        push_matrix()
        rotate(0.5)
        branch(length * 0.7)
        pop_matrix()
        push_matrix()
        rotate(-0.5)
        branch(length * 0.7)
        pop_matrix()

def setup():
    size(800, 600)
    translate(width / 2, height)
    branch(150)