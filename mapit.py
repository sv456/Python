import webbrowser,sys
if sys.argv>=1:
    address=' '.join(sys.argv[1:])

webbrowser.open('https://www.google.com/maps/place/' + address)
    
