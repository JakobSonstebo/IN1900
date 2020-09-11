def triangle_area(vertices):
    """Calculates the area of a triangle with vertices [[x0, y0], [x1, y1], [x2, y2]]."""
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]
    return 1/2*abs(x[1]*y[2] - x[2]*y[1] - x[0]*y[2] + x[2]*y[0] + x[0]*y[1] - x[1]*y[0])


def test_triangle_area():
    """Verifies the calculated area of a triangle with vertices (0,0), (1,0), and (0,2)."""
    v1 = [0, 0]; v2 = [1, 0]; v3 = [0, 2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg

test_triangle_area()

"""
Terminal >> python triangle_area.py

"""
