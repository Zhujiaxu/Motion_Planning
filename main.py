'''111vvv444
def sum_demo(x, y):
    for _ in range(2):
        x += 1
        y += 1
        result = x + y
    return result

if __name__ == '__main__':
    result = sum_demo(1, 1)
    print(result)
'''
class PID:
    def __init__(self, kp, ki, kd, setpoint=0.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint

        self._prev_error = 0.0
        self._integral = 0.0

    def update(self, current_value, dt=1.0):
        error = self.setpoint - current_value
        self._integral += error * dt
        derivative = (error - self._prev_error) / dt if dt > 0 else 0.0

        output = (
            self.kp * error +
            self.ki * self._integral +
            self.kd * derivative
        )
        self._prev_error = error
        return output

# 示例用法
if __name__ == "__main__":
    import time

    pid = PID(kp=0.1, ki=2, kd=0.05, setpoint=10.0)
    current_value = 0.0

    for i in range(50):
        dt = 0.1  # 时间步长
        control = pid.update(current_value, dt)
        # 此处用简单模拟“响应” (如系统被控制的过程)
        current_value += control * 0.1-current_value*0.1
        print(f"Step {i}, Control: {control:.2f}, Value: {current_value:.2f}")
        time.sleep(0.1)
'''