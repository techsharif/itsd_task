import datetime


def process(request):
    result = dict()
    result['today'] = datetime.date.today()
    result['date'] = str(datetime.date.today())
    if request.user.is_authenticated():
        result['user'] = request.user
    return {'cp':result}