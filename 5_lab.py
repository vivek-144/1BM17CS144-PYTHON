class CallDetail:
    def __init__(self,phoneno,called_no,duration,call_type):
        self.__phoneno=phoneno
        self.__called_no=called_no
        self.__duration=duration
        self.__call_type=call_type

    def details(self) :
        print('\nPhone no.',self.__phoneno,'\nduration ',self.__duration,' \ncall type', self.__call_type)
    

class Util:
    def __init__(self):
        self.list_of_call_objects=None

    def parse_customer(self,list_of_call_string):
        self.list_of_call_objects=[]
        for i in list_of_call_string:
            phoneno,called_no,duration,call_type=map(str,i.split(","))
            cl=CallDetail(phoneno,called_no,duration,call_type)
            cl.details()    

call1='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string=[call1,call2,call3]
Util().parse_customer(list_of_call_string)

