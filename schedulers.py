from des import SchedulerDES
from process import ProcessStates
from event import Event, EventTypes

PRIORITY_QUEUE = []

class FCFS(SchedulerDES):
    def scheduler_func(self, cur_event):
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_process):
        arrival_time, quantum, process_id = cur_process.arrival_time, cur_process.service_time, cur_process.process_id
        cur_process.process_state = ProcessStates.RUNNING
        cur_process.run_for(quantum, self.time)
        self.time += quantum
        cur_process.process_state = ProcessStates.TERMINATED
        newEvent = Event(process_id=process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)
        return newEvent


class SJF(SchedulerDES):
    def scheduler_func(self, cur_event):
        pass
    
    def dispatcher_func(self, cur_process):
        pass


class RR(SchedulerDES):
    def scheduler_func(self, cur_event):
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_process):
        arrival_time, service_time, quantum, process_id = cur_process.arrival_time, cur_process.service_time, cur_process.quantum, cur_process.process_id
        cur_process.process_state = ProcessStates.RUNNING
        self.time += cur_process.run_for(quantum, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        newEvent = Event(process_id=process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)
        return newEvent


class SRTF(SchedulerDES):
    def scheduler_func(self, cur_event):
        pass

    def dispatcher_func(self, cur_process):
        pass
