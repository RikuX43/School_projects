def newton(x):

    def f(x, estimate):
        if abs(x-estimate ** 2) <= 0.000001:
            return estimate
        else:
            return f(x, (estimate + x / estimate) / 2)

    return f(x, 1.0)

def limitReached(x, estimate):
    if abs(x-estimate ** 2) <= 0.000001:
        return True
    return False

def improveEstimate(x, estimate):
    return (estimate + x / estimate) / 2



 
def main():
    main()
