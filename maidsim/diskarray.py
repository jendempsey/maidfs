

from disk import Disk


class DiskArray:
    '''
    Implements a MAID array.  This class is responsible for managing an array
    of disks and dispatching file system accesses to specific disks.  This
    class will also manage cache disks if they are used.
    '''


    cache_disks = None
    passive_disks = None


    def __init__(self, num_cache_disks, cache_disk_model,
                 num_passive_disks, passive_disk_model, spin_down_timeout):

        # Create lists to hold the cache disks and passive disks
        if num_cache_disks > 0:
            # Cache disks are not implemented for now
            raise NotImplementedError("Cache disks are currently not implemented.");
        self.cache_disks = []
        '''
        self.cache_disks = \
            [Disk(cache_disk_model, float("inf")) \
            for _ in range(num_cache_disks)]
        '''
        self.passive_disks = \
            [Disk(passive_disk_model, spin_down_timeout) \
            for _ in range(num_passive_disks)]

        # TODO: other initialization (set up metadata)


    def update_time_for_disks(self, disk_list, time):
        # Update the time for the given list of disks
        for theDisk in disk_list:
            theDisk.update_time(time)


    def update_time(self, time):
        # Update time for the cache disks and passive disks
        self.update_time_for_disks(self.cache_disks, time)
        self.update_time_for_disks(self.passive_disks, time)

        # TODO: perform any other time related calculations (may be nothing
        # at this level).


    def read(self, file_info):
        # TODO: read the given file from the correct disk
        # TODO: need to update this to handle the fact that the compressed size
        # is different from the file size
        # TODO: return the total amount of time it took to do the read
        return None


    def write(self, file_info):
        # TODO: write the given file to the correct disk
        # TODO: need to update this to handle the fact that the compressed size
        # is different from the file size
        # TODO: return the total amount of time it took to do the write
        return None


    def get_energy_usage(self):
        # TODO: sum up the energy used by the disks in this array during the
        # entire simulation
        return None

