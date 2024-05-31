class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # Filter out rows that contain no devices
        device_counts = [row.count('1') for row in bank if '1' in row]
        
        # If there is only one row or no rows with devices, there are no beams
        if len(device_counts) < 2:
            return 0
        
        # Calculate the number of beams
        laser_count = 0
        for i in range(len(device_counts) - 1):
            laser_count += device_counts[i] * device_counts[i + 1]
        
        return laser_count
