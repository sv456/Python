def div(divideby):
    try:
        return 42/divideby
    except ZeroDivisionError:
        print 'invalid arguement'

print div(2)
div(0)
print div(1)
