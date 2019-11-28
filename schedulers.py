from des import SchedulerDES
from process import ProcessStates
from event import Event, EventTypes

PRIORITY_QUEUE = []

class FCFS(SchedulerDES):
    def scheduler_func(self, cur_event):
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_process):
        cur_process.process_state = ProcessStates.RUNNING
        self.time += cur_process.run_for(cur_process.service_time, self.time)
        if cur_process.remaining_time == 0:
            cur_process.process_state = ProcessStates.TERMINATED
        return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)


class SJF(SchedulerDES):
    def scheduler_func(self, cur_event):
        return self.processes[cur_event.process_id]
    
    def dispatcher_func(self, cur_process):
        pass


class RR(SchedulerDES):
    def scheduler_func(self, cur_event):
        return self.processes[cur_event.process_id]

    def dispatcher_func(self, cur_process):
        cur_process.process_state = ProcessStates.RUNNING
        self.time += cur_process.run_for(self.quantum, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        if cur_process.remaining_time == 0:
            newEventType = EventTypes.PROC_CPU_DONE
        else:
            cur_process.process_state = ProcessStates.READY
            newEventType = EventTypes.PROC_CPU_REQ
        return Event(process_id=cur_process.process_id, event_type=newEventType, event_time=self.time)


class SRTF(SchedulerDES):
    def scheduler_func(self, cur_event):
        pass

    def dispatcher_func(self, cur_process):
        pass
