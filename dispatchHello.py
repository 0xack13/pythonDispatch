# Sample of python dispatcher

from dispatch import Signal

log_it = Signal(providing_args=['level', 'message'])
def simple_receiver(**kwargs):
    message, level = kwargs['message'], kwargs['level']
    print 'Receiver # 1'
    print '\tLevel: %d, Message: %s\n' % (level, message)

def picky_receiver(**kwargs):
    message, level = kwargs['message'], kwargs['level']
    print 'Receiver # 2'
    if level < 2:
        print "\tSome unimportant message was sent. Ignoring it!\n"


log_it.connect(simple_receiver)
log_it.connect(picky_receiver)
def a_cool_sender():
    # Do something cool here
    # Now send a signal to all receivers
    log_it.send(sender='a_cool_sender', message='Hello!', level=1)

a_cool_sender()
