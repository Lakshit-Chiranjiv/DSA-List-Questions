class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_availability_time = [0] * n
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            min_room_availability_time = inf
            min_available_time_room = 0
            found_unused_room = False
            for i in range(n):
                if room_availability_time[i] <= start:
                    found_unused_room = True
                    meeting_count[i] += 1
                    room_availability_time[i] = end
                    break
                if min_room_availability_time > room_availability_time[i]:
                    min_room_availability_time = room_availability_time[i]
                    min_available_time_room = i
            if not found_unused_room:
                room_availability_time[min_available_time_room] += end - start
                meeting_count[min_available_time_room] += 1

        return meeting_count.index(max(meeting_count))

# 2402. Meeting Rooms III
# Time: O(nlogn)
# Space: O(n)
    
# We first sort the meetings based on the start time. We then iterate through the meetings and keep track of the room availability time. We then iterate through the room availability time and find the room with the minimum availability time. If we find a room which is available, we increment the meeting count and update the room availability time. If we do not find a room which is available, we update the room availability time of the room with the minimum availability time and increment the meeting count. We then return the index of the room with the maximum meeting count.