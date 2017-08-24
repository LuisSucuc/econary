@auth.requires_login()
def index():
    ''' Manage dictionary elements  '''
    words = db(db.dictionary).select()
    if request.vars.msg:
        response.flash = T('Saved')
    return dict(words = words)


@auth.requires_login()
def edit():
    ''' Edit word '''
    word_id = request.vars.word_id

    form = SQLFORM(db.dictionary,
                    showid = False,
                    record = word_id,)
    if form.process().accepted:
        redirect(URL('index', vars = dict(msg = True)))
    elif form.errors:
        response.flash = T('¡ERROR!') + ' ' + T('Review the data')
    return dict(form = form,
                word_id = word_id)

@auth.requires_login()
def delete():
    ''' Delete word '''
    word_id = request.vars.word_id
    db(db.dictionary.id == word_id).delete()
    redirect(URL('index', vars=dict(msg=True)))


@cache.action()
def download():
    return response.download(request, db)
