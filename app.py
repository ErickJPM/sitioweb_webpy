import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/list', 'mvc.controllers.list.List',
    '/insert', 'mvc.controllers.insert.Insert',
    '/delete', 'mvc.controllers.delete.Delete',
    '/view', 'mvc.controllers.view.View',
    '/update', 'mvc.controllers.update.Update'
)
app = web.application(urls, globals())



if __name__ == "__main__":
    app.run()