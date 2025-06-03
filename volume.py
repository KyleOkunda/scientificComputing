import scipy.integrate as spi

def calculate_volume():


    # function to integrate: f(y, x) = x^2 + y^2
    def f(y, x):
        return x**2 + y**2

    # Define the limits of integration for x and y
    # The lower limit for y (gfun) can be a function of x, but here it's constant
    def gfun(x):
        return 0

    # The upper limit for y (hfun) can be a function of x, but here it's constant
    def hfun(x):
        return 1

    # Integrate
    volume, abserr = spi.dblquad(f, 0, 1, gfun, hfun)

    print(f"The calculated volume under the surface is: {volume:.6f}")
    print(f"Estimated absolute error: {abserr:.2e}")


calculate_volume()
