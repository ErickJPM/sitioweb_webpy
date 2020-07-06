import web
render = web.template.render('mvc/views/')
class List():
    
    def GET(self):
        return render.list()