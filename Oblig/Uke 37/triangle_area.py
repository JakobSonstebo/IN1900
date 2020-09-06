def triangle_area(vertices):
    term1 = vertices[1][0]*vertices[2][1]
    term2 = vertices[2][0]*vertices[1][1]
    term3 = vertices[0][0]*vertices[2][1]
    term4 = vertices[2][0]*vertices[0][1]
    term5 = vertices[0][0]*vertices[1][1]
    term6 = vertices[1][0]*vertices[0][1]
    return 1/2*abs(term1-term2-term3+term4+term5-term6)


def test_triangle_area():
    """
    Verify the area of a triangle with vertices
    (0,0), (1,0), and (0,2).
    """
    v1 = [0, 0]; v2 = [1, 0]; v3 = [0, 2]
    vertices = [v1, v2, v3]
    expected = 1
    computed = triangle_area(vertices)
    tol = 1E-14
    success = abs(expected - computed) < tol
    msg = f"computed area={computed} != {expected}(expected)"
    assert success, msg


test_triangle_area()
