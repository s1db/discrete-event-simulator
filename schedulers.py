from des import SchedulerDES
from process import ProcessStates
from event import Event, EventTypes
# importing process and event states, updating self.time

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
        process_with_least_burst = self.processes[cur_event.process_id]
        for process in self.processes:
            if (process.process_state == ProcessStates.READY) and ((process.remaining_time < process_with_least_burst.remaining_time) or (process_with_least_burst.process_state == ProcessStates.TERMINATED)):
                process_with_least_burst = process
                print(process)
        return process_with_least_burst
        
    def dispatcher_func(self, cur_process):
        cur_process.process_state = ProcessStates.RUNNING
        self.time += cur_process.run_for(cur_process.remaining_time, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        return Event(process_id=cur_process.process_id, event_type=EventTypes.PROC_CPU_DONE, event_time=self.time)


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
        process_with_least_burst = self.processes[cur_event.process_id]
        for process in self.processes:
            if (process.process_state == ProcessStates.READY) and ((process.remaining_time < process_with_least_burst.remaining_time) or (process_with_least_burst.process_state == ProcessStates.TERMINATED)):
                process_with_least_burst = process
        return process_with_least_burst

    def dispatcher_func(self, cur_process):
        cur_process.process_state = ProcessStates.RUNNING
        self.time += cur_process.run_for(0.5, self.time)
        cur_process.process_state = ProcessStates.TERMINATED
        if cur_process.remaining_time == 0:
            newEventType = EventTypes.PROC_CPU_DONE
        else:
            cur_process.process_state = ProcessStates.READY
            newEventType = EventTypes.PROC_CPU_REQ
        return Event(process_id=cur_process.process_id, event_type=newEventType, event_time=self.time)