import json


class RQ(object):
    def __init__(self):
        super(RQ, self).__init__()

    def as_dict(self):
        res = {}
        for k, v in self.__dict__.items():
            if v:
                res[k] = v
        return res

    @property
    def data(self):
        return json.dumps(self.as_dict())


class StartRQ(RQ):
    def __init__(self, name=None, description=None, tags=None,
                 start_time=None):
        super(StartRQ, self).__init__()
        #Field 'name' should have size from '1' to '256'.
        if len(name) > 255:
            self.name = "{0} ...".format(name[:250])
        else:
            self.name = name
        self.description = description
        self.tags = tags
        self.start_time = start_time


class StartLaunchRQ(StartRQ):
    def __init__(self, name=None, description=None, tags=None, start_time=None,
                 mode=None):
        super(StartLaunchRQ, self).__init__(name=name, description=description,
                                            tags=tags, start_time=start_time)
        self.mode = mode


class FinishExecutionRQ(RQ):
    def __init__(self, end_time=None, status=None):
        super(FinishExecutionRQ, self).__init__()
        self.end_time = end_time
        self.status = status


class StartTestItemRQ(StartRQ):
    def __init__(self, name=None, description=None, tags=None,
                 start_time=None, launch_id=None, type=None):
        """
        type can be (SUITE, STORY, TEST, SCENARIO, STEP, BEFORE_CLASS,
        BEFORE_GROUPS, BEFORE_METHOD, BEFORE_SUITE, BEFORE_TEST, AFTER_CLASS,
        AFTER_GROUPS, AFTER_METHOD, AFTER_SUITE, AFTER_TEST)
        :param launch_id:
        :param type:
        """
        super(StartTestItemRQ, self).__init__(name=name,
                                              description=description,
                                              tags=tags, start_time=start_time)
        self.launch_id = launch_id
        self.type = type


class FinishTestItemRQ(FinishExecutionRQ):
    def __init__(self, end_time=None, status=None, issue=None):
        super(FinishTestItemRQ, self).__init__(end_time=end_time,
                                               status=status)
        self.issue = issue


class File(RQ):
    def __init__(self, name, content):
        super(File, self).__init__()
        self.name = name
        self.content = content


class SaveLogRQ(RQ):
    def __init__(self, item_id=None, time=None, message=None, level=None,
                 file_obj=None):
        super(SaveLogRQ, self).__init__()
        self.item_id = item_id
        self.time = time
        self.message = message
        self.level = level
        self.file = None
        if file_obj is not None:
            self.file = file_obj.data
