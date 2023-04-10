import multiprocessing
import sys
import traceback


class Process(multiprocessing.Process):

    def __init__(self, *args, **kwargs):
        multiprocessing.Process.__init__(self, *args, **kwargs)
        self._pconn, self._cconn = multiprocessing.Pipe()
        self._exception = None

    def run(self):
        try:
            multiprocessing.Process.run(self)
            self._cconn.send(None)
        except Exception as e:
            tb = traceback.format_exc()
            self._cconn.send((e, tb))
            #raise e  # You can still rise this exception if you need to
            exc_type, exc_value, _ = sys.exc_info()
            print("Child Process Returned an error")
            print("Exception type:", exc_type)
            print("Exception message:", exc_value)


    @property
    def exception(self):
        if self._pconn.poll():
            self._exception = self._pconn.recv()
        return self._exception
