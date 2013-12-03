class Trace:
    '''
    Represents a file system trace containing read and write events to a large
    file system.  The trace file should be in a standard format (generated by
    a separate tool).  Each entry must contain the following:

    Time
    File name
    File path
    File type
    File size
        (note: the above 4 attributes should probably be combined into a file
        object)
    Access type (read or write)
    '''

    # TODO: need to write a tool that converts the file system traces we find
    # (presumably each in a separate format) into a common trace format and
    # assigns file types to each file in the trace based on a given
    # distribution.  That tool will generate the files that are read by this
    # class.


    trace_file_name = None


    def __init__(self, file_name):
        self.trace_file_name = file_name
        # TODO: open the file; perform other initialization


    def next_event(self):
        # TODO: return the next file access event in the trace
        return None


    def more_events(self):
        # TODO: return a boolean indicating if there are more events in the
        # trace.
        return False


    def close(self):
        # TODO: close the file; perform any other shut down
        pass
