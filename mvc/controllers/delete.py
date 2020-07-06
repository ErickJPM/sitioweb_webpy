import web
render = web.template.render('mvc/views/')
class Delete():

    def GET(self):
        return render.delete()