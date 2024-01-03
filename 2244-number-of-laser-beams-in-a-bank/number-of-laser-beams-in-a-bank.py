class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        devices = []
        for row in bank:
            device_cnt = row.count('1')
            if device_cnt > 0:
                devices.append(device_cnt)
        if len(devices) == 0:
            return 0
        prev_cnt = devices[0]
        result = 0
        for cnt in devices[1:]:
            result+=prev_cnt*cnt
            prev_cnt = cnt
        return result