import web
render = web.template.render('mvc/views/')
class Insert():

    def GET(self):
        return render.insert()