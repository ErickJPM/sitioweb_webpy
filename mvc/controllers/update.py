import web
render = web.template.render('mvc/views/')
class Update():

    def GET(self):
        return render.update()