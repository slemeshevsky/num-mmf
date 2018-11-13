import numpy as np

from jacobi import jacobi, generate_problem

def test_generate_problem():
    A, b = generate_problem(0.5, 3)
    A_expected = np.array([[2., -1.5, 0.], [-0.5, 2., -1.5], [0., -0.5, 2.]])
    b_expected = np.array([0.5, 0., 1.5])
    matrix_success = (A == A_expected).any()
    b_success = (b == b_expected).any()
    msg = "A = %s, b = %s" % (A, b)

    assert matrix_success and b_success, msg

def test_jacobi():
    A, b = generate_problem(0.5, 3)
    max_it = 1
    x, it = jacobi(A, b, max_it=max_it)
    expected = np.array([0.25, 1.25, 0.75])
    success = (x == expected).any()
    msg = "x = %s, expected = %s, b = %s, it = %s" % (x, expected, b, it)

    assert success, msg

def test_convergence():
    A, b = generate_problem(0.5, 100)
    exact = np.linalg.solve(A, b)
    tol = 1e-15
    x, it = jacobi(A, b, tol=tol)
    error = np.linalg.norm(exact - x)
    success = (error - tol*np.linalg.norm(A)) < tol
    msg = "error = %s, tol*norm(A) = %s, " % (error, tol*np.linalg.norm(A))

    assert success, msg
