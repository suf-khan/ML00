import sys 
import os 


def error_message_detail(error, error_detail:sys):   
    _,_,exc_tb = error_detail.exc_info()    #could also simply be sys.exc_info() 
                                            #if an exception (e) is currently handled, exc_info() returns the tuple(type(e), e, e.__traceback__)
                                            #a traceback object typically encapsulates the call stack at the point where the exception last occured. 
    filename= exc_tb.tb_frame.f_code.co_filename

    error_message = "error occured and the file name is [{0}] and the linenumber is [{1}] and error is [{2}]".format(filename, exc_tb.tb_lineno, str(error))

    return error_message


class SensorException(Exception): 
    
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)

        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):  #print(e) automaticalluy calls __str__()
        return self.error_message