import sys, os
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message: Exception, error_detail: sys):
        self.error_message = error_message
        _,_, exc_tb = error_detail.exc_info()
        
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno
        
        
