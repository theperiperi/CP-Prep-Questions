class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        start_cooking = customers[0][0]
        total_wait = 0
        for customer in customers:
            if customer[0] > start_cooking :
                start_cooking = customer[0]
            finished_cooking = start_cooking + customer[1]
            waiting_time = finished_cooking - customer[0]
            total_wait += waiting_time
            start_cooking = finished_cooking
        return total_wait/(len(customers))
