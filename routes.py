from melody import render

def index(request):
    return render('index.html', variables={'flavors': [
        {'id': 'flavor1', 'name': 'Flavor 1', 'description': 'A delightful new flavor for your musical journey.'},
        {'id': 'flavor2', 'name': 'Flavor 2', 'description': 'An exciting twist to enhance your melody experience.'},
        {'id': 'flavor3', 'name': 'Flavor 3', 'description': 'A unique flavor that brings a fresh perspective to your music.'},
        
        ]})

def install_package(request):
    package = request.params['package_name']
    
    return package

routes = {
    '/': index,
    '/install/<string:package_name>': install_package,
}