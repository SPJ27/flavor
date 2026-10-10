from melody import render

def index(request):
    return render('index.html')

def install_package(request):
    package = request.params['package_name']
    
    return package

routes = {
    '/': index,
    '/install/<string:package_name>': install_package,
}