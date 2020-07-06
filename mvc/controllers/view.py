import web
render = web.template.render('mvc/views/')
class View():

    def GET(self):
        return render.view()