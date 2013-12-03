from processor import CompressionResult
from processor import Processor


class Simulation:
    '''
    Master file that runs through a file system trace and simulates executing
    the trace on a MAID array while selectively applying compression according
    to a provided algorithm.
    '''


    trace = None
    compression_alg = None
    selection_alg = None
    processor = None
    disk_array = None
    previous_time = None
    total_read_time = None
    read_count = None
    total_write_time = None
    write_count = None


    def __init__(self, trace, compression_alg, selection_alg, 
                 processor_model, disk_array):
        self.trace = trace
        self.compression_alg = compression_alg
        self.selection_alg = selection_alg
        self.processor = Processor(processor_model)
        self.disk_array = disk_array
        self.previous_time = 0
        self.total_read_time = 0
        self.read_count = 0
        self.total_write_time = 0
        self.write_count = 0


    def execute_trace(self):

        while self.trace.more_events():

            # Get the next event
            event = self.trace.next_event()

            # Make sure time is not going backwards
            if event.time < self.previous_time:
                raise ValueError("Time is going backwards: current time = " +
                                 str(event.time) +
                                 ", previous time = " +
                                 str(self.previous_time))
            event.previous_time = event.time

            # Update the time in the rest of the simulation
            self.processor.update_time(event.time)
            self.disk_array.update_time(event.time)

            # Determine if this file should be compressed
            do_compress = self.selection_alg.should_compress(event.file)

            # Compress and write or read and decompress the file
            if event.access_type is EventType.READ:
                read_time = self.disk_array.read(event.file)
                if do_compress:
                    read_time += \
                        self.processor.decompress(event.file, compression_alg)
                self.total_read_time += read_time
                self.read_count += 1
            else:
                size = event.file.size
                compression_result = CompressionResult()
                if do_compress:
                    compression_result = self.processor.compress(
                        event.file, compression_alg)
                write_time = compression_result.execution_time
                write_time += self.disk_array.write(
                    event.file, compression_result.compressed_size)
                self.total_write_time += write_time
                self.write_count += 1

        # Clean up
        self.trace.close()


    def run(self):
        # TODO: any set up that's not already done in __init__

        # Simulate the provided trace
        print "Starting trace execution"
        self.execute_trace()
        print "Trace execution complete"

        # TODO: gather and report results
