## 质点运动学（天体系统模拟）

- 显式积分

  - 用当前速度更新位置，用当前加速度更新速度
  - 所有状态更新都依赖当前状态，数值稳定性差

- 半隐式积分

  - 用当前加速度更新速度，用新速度更新位置
  - 数值稳定性较高

显式积分函数：

```py
@ti.kernel
def update_explicit_euler():
    for i in range(N):
        pos[i] += vel[i] * dt
        vel[i] += force[i] / mass[i] * dt

```

半隐式积分函数：

```py
@ti.kernel
def update_semi_implicit_euler():
    for i in range(N):
        vel[i] += force[i] / mass[i] * dt
        pos[i] += vel[i] * dt

```

??? remarks "Solar System 完整代码"

    ```py
    import taichi as ti
    import math
    import numpy as np
    import matplotlib.pyplot as plt


    ti.init(ti.gpu)  # ti.cpu / ti.gpu

    # Simulation parameters
    # 区分显式和半隐式：dt=6e-6
    dt = 3e-5
    G = 1
    N = 5

    # Mass, initial positions and velocities
    mass_np = np.array([20000.0, 1000.0, 2000.0, 150.0, 20.0], dtype=np.float32)
    pos_np = np.array([[0.3, 0.7], [0.3, 0.6], [0.3, 0.5], [0.4, 0.4], [0.35, 0.4]], dtype=np.float32)
    vel_np = np.array([[0, 0], [280, 0], [260, 0], [140, 0], [180, 20]], dtype=np.float32)

    # Planet radius for rendering
    planet_radius = np.array([max(1, x**(1/3)) for x in mass_np], dtype=np.float32)

    # Taichi fields
    mass = ti.field(ti.f32, N)
    pos = ti.Vector.field(2, ti.f32, N)
    vel = ti.Vector.field(2, ti.f32, N)
    force = ti.Vector.field(2, ti.f32, N)

    mass.from_numpy(mass_np)
    pos.from_numpy(pos_np)
    vel.from_numpy(vel_np)

    # History
    MAX_HISTORY = 1000
    history = ti.Vector.field(2, ti.f32, shape=(N, MAX_HISTORY))
    history_idx = ti.field(ti.i32, shape=N)
    traj_np = np.zeros((N, MAX_HISTORY, 2), dtype=np.float32)

    # 定义每个天体的轨迹颜色
    traj_colors = np.array([
        0x63b2ee,
        0xeddd86 ,
        0x76da91,
        0xf89588,
        0x7cd6cf
    ], dtype=np.int32)


    @ti.kernel
    def clear_force():
        for i in range(N):
            force[i] = ti.Vector([0.0, 0.0])


    @ti.kernel
    def compute_force():
        for i in range(N):
            for j in range(i + 1, N):
                dist = pos[i] - pos[j]
                radius = dist.norm() + 1e-6
                f = G * mass[i] * mass[j] / (radius ** 3) * dist
                force[j] += f
                force[i] -= f

    @ti.kernel
    def update_explicit_euler():
        for i in range(N):
            pos[i] += vel[i] * dt
            vel[i] += force[i] / mass[i] * dt


    @ti.kernel
    def update_semi_implicit_euler():
        for i in range(N):
            vel[i] += force[i] / mass[i] * dt
            pos[i] += vel[i] * dt


    @ti.kernel
    def record_history():
        for i in range(N):
            idx = history_idx[i] % MAX_HISTORY
            history[i, idx] = pos[i]
            history_idx[i] += 1


    @ti.kernel
    def copy_history_to_numpy(traj_np: ti.types.ndarray()):
        for i in range(N):
            for j in range(MAX_HISTORY):
                traj_np[i, j, 0] = history[i, j][0]
                traj_np[i, j, 1] = history[i, j][1]


    def update():
        clear_force()
        compute_force()
        update_semi_implicit_euler()
        # update_explicit_euler()

    @ti.kernel
    def compute_energy() -> ti.f32:
        total_energy = 0.0
        for i in range(N):
            kinetic = 0.5 * mass[i] * vel[i].dot(vel[i])
            potential = 0.0
            for j in range(N):
                if i != j:
                    dist = (pos[i] - pos[j]).norm() + 1e-6
                    potential -= G * mass[i] * mass[j] / dist
            total_energy += kinetic + potential
        return total_energy


    gui = ti.GUI('N-body problem', (1024, 1024))
    t = 0


    # 记录每个时间步的能量
    energies = []

    while gui.running:
        t += 1
        update()
        record_history()

        if t % 10 == 0:
            gui.clear(0x000000)
            copy_history_to_numpy(traj_np)

            # 绘制轨迹，每条轨迹分段绘制，防止首尾连线
            for i in range(N):
                color = int(traj_colors[i])  # 使用对应的颜色
                idx = history_idx[i] % MAX_HISTORY
                length = min(history_idx[i], MAX_HISTORY)
                if length < MAX_HISTORY:
                    traj = traj_np[i, :length]
                    for j in range(1, length):
                        gui.line(traj[j-1], traj[j], radius=1, color=color)
                else:
                    # 历史数组已满，分两段绘制
                    traj_part1 = traj_np[i, idx:]
                    for j in range(1, len(traj_part1)):
                        gui.line(traj_part1[j-1], traj_part1[j], radius=1, color=color)
                    traj_part2 = traj_np[i, :idx]
                    for j in range(1, len(traj_part2)):
                        gui.line(traj_part2[j-1], traj_part2[j], radius=1, color=color)

            # 绘制行星
            gui.circles(pos.to_numpy(), color=0xdcdcdc, radius=planet_radius)
            gui.show()

    ```

## 前向运动学（机械臂计算）

### 二维单支机械臂

前向动力学：由关节角度的列表计算末端位置

从第 0 个关节（轴）开始，依次遍历每个关节，每个机械臂的角度为之前所有关节处角度的累加。  
每个关节相对上一个关节的移动为机械臂长度\*当前角度，即$\mathrm{d}x=len\times\cos\theta $ ,$\mathrm{d}y=len\times\sin\theta $。  
每个关节的位置为上一个关节的位置+相对移动量

代码：

```py
def forward_kinematics(angles_rad):
    positions = [np.array([0.0, 0.0])] # 末端位置
    current_angle = 0.0 # 每个关节当前角度
    current_pos = np.array([0.0, 0.0])

    # 从轴开始依次遍历每个关节
    for i in range(n_links):
        current_angle += angles_rad[i] # 更新关节的角度
        dx = link_lengths[i] * np.cos(current_angle) # 更新xy
        dy = link_lengths[i] * np.sin(current_angle)
        current_pos = current_pos + np.array([dx, dy]) # 更新末端位置
        positions.append(current_pos.copy())

    return np.array(positions)
```

??? remarks "完整代码"

    ```py
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider, Button

    from matplotlib import rcParams

    rcParams['font.family'] = 'serif'
    rcParams['mathtext.fontset'] = 'cm'
    rcParams['axes.linewidth'] = 1.2
    rcParams['xtick.direction'] = 'in'
    rcParams['ytick.direction'] = 'in'
    rcParams['xtick.major.size'] = 6
    rcParams['ytick.major.size'] = 6

    # 机械臂参数
    link_lengths = [2.0, 1.5, 1.0]  # 长度
    n_links = len(link_lengths)  # 机械臂总数


    # 前向动力学，由关节角度的列表计算末端位置
    def forward_kinematics(angles_rad):
        positions = [np.array([0.0, 0.0])] # 末端位置
        current_angle = 0.0 # 每个关节当前角度
        current_pos = np.array([0.0, 0.0])

        # 从轴开始依次遍历每个关节
        for i in range(n_links):
            current_angle += angles_rad[i] # 更新关节的角度
            dx = link_lengths[i] * np.cos(current_angle) # 更新xy
            dy = link_lengths[i] * np.sin(current_angle)
            current_pos = current_pos + np.array([dx, dy]) # 更新末端位置
            positions.append(current_pos.copy())

        return np.array(positions)


    # 可视化设置
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.35)  # space for sliders

    arm_line, = ax.plot([], [], 'o-', lw=4, color='blue', label='Links')
    end_point, = ax.plot([], [], 'ro', label='End-Effector')  # single point
    ax.set_xlim(-sum(link_lengths) - 0.5, sum(link_lengths) + 0.5)
    ax.set_ylim(-sum(link_lengths) - 0.5, sum(link_lengths) + 0.5)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title("Interactive 2D Robotic Arm")
    ax.legend()

    coord_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=10,
                        verticalalignment='top', bbox=dict(facecolor='white', alpha=0.6))

    # 滑动条设置
    sliders = []
    for i in range(n_links):
        ax_slider = plt.axes([0.1, 0.25 - i * 0.07, 0.8, 0.03])  # x, y, width, height
        slider = Slider(ax_slider, f'Joint {i + 1} (deg)', -180.0, 180.0, valinit=0.0)
        sliders.append(slider)


    # 显示更新
    def update(val):
        joint_angles = [s.val for s in sliders] # 从滑动条获取角度参数
        angles_rad = [np.deg2rad(a) for a in joint_angles]
        positions = forward_kinematics(angles_rad)

        # 更新绘制机械臂
        arm_line.set_data(positions[:, 0], positions[:, 1])

        # 更新末端坐标显示
        x_e, y_e = positions[-1, 0], positions[-1, 1]
        end_point.set_data([x_e], [y_e])
        coord_text.set_text(f'End-Effector (x, y) = ({x_e:.3f}, {y_e:.3f})')

        fig.canvas.draw_idle()


    for s in sliders:
        s.on_changed(update)

    # 重置按钮设计
    reset_ax = plt.axes([0.8, 0.05, 0.1, 0.04])
    button = Button(reset_ax, 'Reset', color='lightgray', hovercolor='lightblue')


    def reset(event):
        for s in sliders:
            s.reset()


    button.on_clicked(reset)

    # 起始情况
    update(None)
    plt.show()
    ```

### 二维分叉机械臂

如果机械臂分叉，开始几个关节共享，后面的关节对应不同机械臂，先计算共享部分，再依次计算各个分支。

代码：（以一个分支为例）

```py
def forward_kinematics(angle_rad_base, angles_rad_1, angles_rad_2):
    # 计算共享的关节位置
    base_positions = [np.array([0.0, 0.0])]
    base_end = [np.array([0.0, 0.0])]
    base_angle = 0.0
    for i in range(n_linds_base):
        base_angle += angle_rad_base[i]
        dx = base_joint_length[i] * np.cos(base_angle)
        dy = base_joint_length[i] * np.sin(base_angle)
        base_end += np.array([dx, dy])
        base_positions.append(base_end.copy())

    # 计算分支1的位置（从分叉关节开始）
    positions_1 = [base_end.copy()]
    current_angle_1 = base_angle
    current_pos_1 = base_end.copy()
    for i in range(n_links_1):
        current_angle_1 += angles_rad_1[i]
        dx = link_lengths_1[i] * np.cos(current_angle_1)
        dy = link_lengths_1[i] * np.sin(current_angle_1)
        current_pos_1 += np.array([dx, dy])
        positions_1.append(current_pos_1.copy())

    # 计算分支2的位置（从分叉关节开始）
    positions_2 = [base_end.copy()]
    current_angle_2 = base_angle
    current_pos_2 = base_end.copy()
    for i in range(n_links_2):
        current_angle_2 += angles_rad_2[i]
        dx = link_lengths_2[i] * np.cos(current_angle_2)
        dy = link_lengths_2[i] * np.sin(current_angle_2)
        current_pos_2 += np.array([dx, dy])
        positions_2.append(current_pos_2.copy())

    return np.array(base_positions), np.array(positions_1), np.array(positions_2)

```

### 三维机械臂

三维空间中用$theta$和$phi$两个参数定义方向，$theta$表示与 Z 轴的夹角（极角），$phi$表示在 XY 平面的投影与 X 轴的夹角（方位角）

三维和二维的相对性区别：

- 2D 常用相对角度，每个关节的角度表示相对于上一关节的角度
- 3D 常用绝对角度，每个关节的角度表示在全局坐标系中的方向，角度不用累加

先从$theta$和$phi$的球坐标变换到笛卡尔系，得到方向向量 d：

$$
\vec{d}=\begin{bmatrix}
\sin\theta\cos\phi \\
\sin\theta\sin\phi \\
\cos\theta
\end{bmatrix}
$$

每个关节相对于上一关节的移动量为方向 d 乘标量长度

代码：

```py
def forward_kinematics(angles_rad):
    positions = [np.array([0.0, 0.0, 0.0])]  # 末端位置初始化
    current_pos = np.array([0.0, 0.0, 0.0])  # 当前关节位置

    # 遍历每个关节
    for i in range(n_links):
        # 获取当前关节的theta和phi角度
        theta, phi = angles_rad[i]

        # 计算方向向量 (使用球坐标到笛卡尔坐标的转换)
        direction = np.array([
            np.sin(theta) * np.cos(phi),
            np.sin(theta) * np.sin(phi),
            np.cos(theta)
        ])

        # 计算新的位置
        displacement = link_lengths[i] * direction
        current_pos += displacement  # 更新末端位置
        positions.append(current_pos.copy())

    return np.array(positions)

```

## 逆向运动学（二维机械臂）

逆向运动学：已知末端位置，求每个关节的角度

### 几何法（两节为例）

分别以轴线、末端目标位置为圆心，以第一、第二段机械臂长度为半径画圆，两个圆交点为关节的位置。

$$
\begin{cases}
\begin{align*}
a^2+h^2&=l_1^2 \\
(d-a)^2+h^2&=l_2^2
\end{align*}
\end{cases}
$$

$$d^2+2ad=l_2^2-l_1^2$$

$$ a=\frac{l_2^2-l_1^2-d^2}{2d}$$

代码：

```py
def inverse_kinematics_geom(target, elbow_up=True, ax=None):
    global warning_text
    x, y = target
    d = np.sqrt(x ** 2 + y ** 2)

    # 检查是否可达
    if d > l1 + l2:
        # 缩放目标点
        scale = (l1 + l2) / d
        x *= scale
        y *= scale
        d = l1 + l2
        # 显示红色警告
        if ax is not None:
            if warning_text is not None:
                warning_text.remove()
            warning_text = ax.text(0.5, 0.95, "Cannot reach!", color='red',
                                   fontsize=14, ha='center', va='top',
                                   transform=ax.transAxes)
    else:
        if warning_text is not None:
            warning_text.remove()
            warning_text = None

    # 圆交点公式
    a = (l1 ** 2 - l2 ** 2 + d ** 2) / (2 * d)
    h = np.sqrt(np.clip(l1 ** 2 - a ** 2, 0, None))
    x2 = a * x / d
    y2 = a * y / d
    rx = -y * (h / d)
    ry = x * (h / d)

    if elbow_up:
        joint = np.array([x2 + rx, y2 + ry])
    else:
        joint = np.array([x2 - rx, y2 - ry])

    theta1 = np.arctan2(joint[1], joint[0])
    theta2 = np.arctan2(y - joint[1], x - joint[0]) - theta1
    return np.array([theta1, theta2]), joint

```

### 梯度下降法

从初始条件开始，先用正向运动学计算当前末端位置。

计算误差`error`为目标位置和当前末端位置之间的偏差向量，目的是使这个量最小化。当误差小于某个阈值时停止计算。

雅可比矩阵`J`表示末端位置对当前关节角度的偏导：

$$\delta \mathbf{p} = J \cdot \delta \theta, \quad J=\frac{\partial\mathbf{p}}{\partial \theta}$$

计算雅可比矩阵方法：给当前角度增加微小量`delta`，计算末端移动距离，距离/增加的角度得到雅可比矩阵。

`J`的转置用于表示反向传播，即用末端位置变化反向计算得到每个关节的角度变化。

希望改变小角度后使误差向量最小，即：

$$ \mathrm{error}=J\cdot \mathrm{delta}$$

梯度下降法更新角度：角度增量 = 学习率 \* 雅可比矩阵的转置和误差向量的乘积

- 学习率`lr`：决定每次调整关节角度的步长大小，每次计算增量后乘学习率表示实际调整的值
- 雅可比矩阵的转置和误差向量的乘积`J.T@error`：得到每个关节角度的调整增量

代码：

```py
def inverse_kinematics(target, initial_angles, lr=0.05, iterations=200):
    angles = np.array(initial_angles, dtype=float)
    for _ in range(iterations):
        # 计算当前末端的位置
        positions = forward_kinematics(angles)
        end_pos = positions[-1]

        # 计算误差
        error = target - end_pos
        # 误差小于阈值时停止
        if np.linalg.norm(error) < 1e-3:
            break

        # 计算雅可比矩阵，用于优化
        J = np.zeros((2, n_links))
        delta = 1e-5
        for i in range(n_links):
            # 计算偏导数
            perturbed = angles.copy()
            perturbed[i] += delta
            new_pos = forward_kinematics(perturbed)[-1]
            J[:, i] = (new_pos - end_pos) / delta

        # 角度增量=步长*雅可比矩阵的转置*偏差
        d_theta = lr * J.T @ error
        # 更新角度
        angles += d_theta

    return angles

```

??? remarks "完整代码"

    ```py
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Button
    from matplotlib.widgets import Slider

    from matplotlib import rcParams

    rcParams['font.family'] = 'serif'
    rcParams['mathtext.fontset'] = 'cm'
    rcParams['axes.linewidth'] = 1.2
    rcParams['xtick.direction'] = 'in'
    rcParams['ytick.direction'] = 'in'
    rcParams['xtick.major.size'] = 6
    rcParams['ytick.major.size'] = 6

    # 机械臂参数
    link_lengths = [2.0, 1.5, 1.0]
    n_links = len(link_lengths)
    total_len = 0
    for l in link_lengths:
        total_len += l


    # 前向运动学
    def forward_kinematics(angles_rad):
        positions = [np.array([0.0, 0.0])]
        current_angle = 0.0
        current_pos = np.array([0.0, 0.0])
        for i in range(n_links):
            current_angle += angles_rad[i]
            dx = link_lengths[i] * np.cos(current_angle)
            dy = link_lengths[i] * np.sin(current_angle)
            current_pos = current_pos + np.array([dx, dy])
            positions.append(current_pos.copy())
        return np.array(positions)


    # 逆向运动学
    def inverse_kinematics(target, initial_angles, lr=0.05, iterations=200):
        angles = np.array(initial_angles, dtype=float)
        for _ in range(iterations):
            # 计算当前末端的位置
            positions = forward_kinematics(angles)
            end_pos = positions[-1]

            # 计算误差
            error = target - end_pos
            # 误差小于阈值时停止
            if np.linalg.norm(error) < 1e-3:
                break

            # 计算雅可比矩阵，用于优化
            J = np.zeros((2, n_links))
            delta = 1e-5
            for i in range(n_links):
                # 计算偏导数
                perturbed = angles.copy()
                perturbed[i] += delta
                new_pos = forward_kinematics(perturbed)[-1]
                J[:, i] = (new_pos - end_pos) / delta

            # 角度增量=步长*雅可比矩阵的转置*偏差
            d_theta = lr * J.T @ error
            # 更新角度
            angles += d_theta

        return angles


    # 用末端绘制圆
    def circle_trajectory(radius=2.0, points=100):
        t = np.linspace(0, 2 * np.pi, points)
        return np.vstack([radius * np.cos(t), radius * np.sin(t)]).T


    # 用末端绘制正方形
    def square_trajectory(side=2.0, points=100):
        half = side / 2
        p = []
        for t in np.linspace(-half, half, points // 4, endpoint=False):
            p.append([t, -half])
        for t in np.linspace(-half, half, points // 4, endpoint=False):
            p.append([half, t])
        for t in np.linspace(half, -half, points // 4, endpoint=False):
            p.append([t, half])
        for t in np.linspace(half, -half, points // 4, endpoint=False):
            p.append([-half, t])
        return np.array(p)


    # 用末端绘制五角星
    def star_trajectory(radius=1.0, points=100):
        # 五角星顶点角度（5个顶点）
        angles = np.linspace(0, 2 * np.pi, 6)[:-1]  # 0~2pi，去掉重复的顶点
        # 五角星连线顺序（五角星的跳线顺序）
        order = [0, 2, 4, 1, 3, 0]  # 回到起点
        # 生成顶点坐标
        vertices = np.array([[radius * np.cos(angles[i]), radius * np.sin(angles[i])] for i in range(5)])

        # 生成轨迹点
        trajectory = []
        points_per_edge = points // 5  # 每条边分配点数
        for i in range(5):
            start = vertices[order[i]]
            end = vertices[order[i + 1]]
            for t in np.linspace(0, 1, points_per_edge, endpoint=False):
                trajectory.append(start + t * (end - start))

        return np.array(trajectory)


    # 可视化
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)

    arm_line, = ax.plot([], [], 'o-', lw=4, color='blue', label='Robot Arm')
    target_dot, = ax.plot([], [], 'rx', label='Target')
    traj_line, = ax.plot([], [], 'g--', lw=1, label='Trajectory')  # 轨迹线

    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_xlim(-6, 6)
    ax.set_ylim(-6, 6)
    ax.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax.set_title("Inverse Kinematics")

    coord_text = ax.text(0.02, 0.95, "", transform=ax.transAxes, fontsize=10,
                        verticalalignment='top', bbox=dict(facecolor='white', alpha=0.6))

    # 窗口控制
    running = [False]
    trajectory_type = ['circle']
    trajectory = circle_trajectory()
    step = [0]
    angles = [0.0, 0.0, 0.0]
    end_effector_history = []


    def update_frame(frame):
        if not running[0]:
            return

        idx = step[0] % len(trajectory)
        target = trajectory[idx]
        target_dot.set_data([target[0]], [target[1]])

        new_angles = inverse_kinematics(target, angles)
        pos = forward_kinematics(new_angles)
        arm_line.set_data(pos[:, 0], pos[:, 1])

        # 更新末端轨迹
        end_effector_history.append(pos[-1])
        traj_array = np.array(end_effector_history)
        traj_line.set_data(traj_array[:, 0], traj_array[:, 1])

        coord_text.set_text(f"Step: {step[0]}\nTarget: ({target[0]:.2f}, {target[1]:.2f})")
        angles[:] = new_angles
        step[0] += 1
        fig.canvas.draw_idle()
        fig.canvas.start_event_loop(0.05)


    def start(event):
        running[0] = True
        while running[0]:
            update_frame(None)


    def stop(event):
        running[0] = False


    def switch(event):
        size = size_slider.val  # 获取当前滑动条值
        if trajectory_type[0] == 'circle':
            trajectory_type[0] = 'square'
            trajectory[:] = square_trajectory(side=size)
        elif trajectory_type[0] == 'square':
            trajectory_type[0] = 'star'
            trajectory[:] = star_trajectory(radius=size)
        else:
            trajectory_type[0] = 'circle'
            trajectory[:] = circle_trajectory(radius=size)

        # 重置状态
        step[0] = 0
        angles[:] = [0.0, 0.0, 0.0]
        end_effector_history.clear()
        arm_line.set_data([], [])
        traj_line.set_data([], [])
        target_dot.set_data([], [])


    # 按钮设置
    start_ax = plt.axes([0.1, 0.05, 0.1, 0.04])
    stop_ax = plt.axes([0.25, 0.05, 0.1, 0.04])
    switch_ax = plt.axes([0.4, 0.05, 0.2, 0.04])
    start_btn = Button(start_ax, 'Start', color='lightgreen', hovercolor='lime')
    stop_btn = Button(stop_ax, 'Stop', color='lightcoral', hovercolor='red')
    switch_btn = Button(switch_ax, 'Switch Trajectory', color='lightblue', hovercolor='skyblue')

    start_btn.on_clicked(start)
    stop_btn.on_clicked(stop)
    switch_btn.on_clicked(switch)

    # 滑动条设置
    size_ax = plt.axes([0.65, 0.05, 0.25, 0.03])
    size_slider = Slider(size_ax, 'Size', 0.5, 6.0, valinit=2.0)  # 最小0.5，最大4，初始2


    def update_size(val):
        size = size_slider.val
        # 清除之前的警告文字
        if hasattr(update_size, "warning_text") and update_size.warning_text:
            update_size.warning_text.remove()
            update_size.warning_text = None

        # 如果 size 超过总长度，显示红色提示
        if size > total_len:
            update_size.warning_text = ax.text(0.5, 0.95, 'Too long!', color='red',
                                            fontsize=12, ha='center', va='top',
                                            transform=ax.transAxes)
        else:
            update_size.warning_text = None

        if trajectory_type[0] == 'circle':
            trajectory[:] = circle_trajectory(radius=size)
        elif trajectory_type[0] == 'square':
            trajectory[:] = square_trajectory(side=size)
        elif trajectory_type[0] == 'star':
            trajectory[:] = star_trajectory(radius=size)
        step[0] = 0
        end_effector_history.clear()


    size_slider.on_changed(update_size)

    plt.show()
    ```

### 解析法

列数学表达式求解

代码：略 ~~其实是 ai 写的有 bug，不放这里了~~

### 有限差分法

有限差分法（FDM）用于计算梯度

有限差分法用于数值计算导数，它通过计算函数值的变化率来近似导数。具体来说，对于一个函数 $f(x)$，其导数 $f'(x)$ 可以通过如下公式进行近似：

- 前向差分法：

$$
f'(x) \approx \frac{f(x + h) - f(x)}{h}
$$

- 后向差分法：

$$
f'(x) \approx \frac{f(x) - f(x - h)}{h}
$$

- 中心差分法（精度更高）：

$$
f'(x) \approx \frac{f(x + h) - f(x - h)}{2h}
$$

其中 $h$ 是一个小的增量，通常选取非常小的数值（如 $h = 1e-6$）。

Pros：

- **实现简单**：适用于没有复杂微分工具的情况。
- **通用性强**：可以用来近似任何类型的函数的导数。

Cons：

- **效率较低**：每次计算导数都需要多次计算函数值，尤其在多维问题中会非常低效。
- **精度受限**：取 $h$ 的值时需要权衡计算精度与数值稳定性，且可能引入数值误差。

### 自动微分法

自动微分法同样用于计算函数的导数或梯度，可调用 python 中 autograd 或 jax

下面为 jax 的版本，其中`loss_fn`为损失函数，希望使这个值最小。

代码：

```py
# 前向运动学 (jax 版本)
def forward_kinematics_jax(angles):
    positions = [jnp.array([0.0, 0.0])]
    current_angle = 0.0
    current_pos = jnp.array([0.0, 0.0])
    for i in range(n_links):
        current_angle += angles[i]
        dx = link_lengths[i] * jnp.cos(current_angle)
        dy = link_lengths[i] * jnp.sin(current_angle)
        current_pos = current_pos + jnp.array([dx, dy])
        positions.append(current_pos)
    return jnp.stack(positions)

# 逆向运动学 (jax自动微分)
def inverse_kinematics_autodiff(target, initial_angles, lr=0.05, iterations=200):
    angles = jnp.array(initial_angles, dtype=float)

    # 损失函数：末端执行器与目标点的距离平方
    def loss_fn(angles):
        end_pos = forward_kinematics_jax(angles)[-1]
        return jnp.sum((end_pos - target) ** 2)

    grad_fn = jax.grad(loss_fn)

    for _ in range(iterations):
        gradients = grad_fn(angles)
        if jnp.linalg.norm(gradients) < 1e-6:
            break
        angles = angles - lr * gradients

    return np.array(angles)

```

## 刚体动力学（机器人仿真）

略

代码说明见下一个文件“rigid_body 代码说明” （ai 参与，仅供参考）

??? remarks "rigid_body.py 完整代码"

    ```py
    from robot_config import robots
    import sys
    import taichi as ti
    import math
    import numpy as np
    import os
    import pickle
    import cv2

    real = ti.f32
    ti.init(default_fp=real)

    max_steps = 4096
    vis_interval = 256
    output_vis_interval = 16
    steps = 2048
    assert steps * 2 <= max_steps

    vis_resolution = 1024

    scalar = lambda: ti.field(dtype=real)
    vec = lambda: ti.Vector.field(2, dtype=real)

    loss = scalar()

    use_toi = False

    x = vec()
    v = vec()
    rotation = scalar()
    # angular velocity
    omega = scalar()

    halfsize = vec()

    inverse_mass = scalar()
    inverse_inertia = scalar()

    v_inc = vec()
    x_inc = vec()
    rotation_inc = scalar()
    omega_inc = scalar()

    head_id = 3
    goal = vec()

    n_objects = 0
    # target_ball = 0
    elasticity = 0.0
    ground_height = 0.1
    gravity = -9.8
    friction = 1.0
    penalty = 1e4
    damping = 10

    gradient_clip = 30
    spring_omega = 30
    default_actuation = 0.05

    n_springs = 0
    spring_anchor_a = ti.field(ti.i32)
    spring_anchor_b = ti.field(ti.i32)
    # spring_length = -1 means it is a joint
    spring_length = scalar()
    spring_offset_a = vec()
    spring_offset_b = vec()
    spring_phase = scalar()
    spring_actuation = scalar()
    spring_stiffness = scalar()

    n_sin_waves = 10

    n_hidden = 32
    weights1 = scalar()
    bias1 = scalar()
    hidden = scalar()
    weights2 = scalar()
    bias2 = scalar()
    actuation = scalar()


    def n_input_states():
        return n_sin_waves + 6 * n_objects + 2


    def allocate_fields():
        ti.root.dense(ti.i,
                    max_steps).dense(ti.j,
                                    n_objects).place(x, v, rotation,
                                                        rotation_inc, omega, v_inc,
                                                        x_inc, omega_inc)
        ti.root.dense(ti.i, n_objects).place(halfsize, inverse_mass,
                                            inverse_inertia)
        ti.root.dense(ti.i, n_springs).place(spring_anchor_a, spring_anchor_b,
                                            spring_length, spring_offset_a,
                                            spring_offset_b, spring_stiffness,
                                            spring_phase, spring_actuation)
        ti.root.dense(ti.ij, (n_hidden, n_input_states())).place(weights1)
        ti.root.dense(ti.ij, (n_springs, n_hidden)).place(weights2)
        ti.root.dense(ti.i, n_hidden).place(bias1)
        ti.root.dense(ti.i, n_springs).place(bias2)
        ti.root.dense(ti.ij, (max_steps, n_springs)).place(actuation)
        ti.root.dense(ti.ij, (max_steps, n_hidden)).place(hidden)
        ti.root.place(loss, goal)
        ti.root.lazy_grad()


    dt = 0.001
    learning_rate = 1.0


    @ti.kernel
    def nn1(t: ti.i32):
        for i in range(n_hidden):
            actuation = 0.0
            for j in ti.static(range(n_sin_waves)):
                actuation += weights1[i, j] * ti.sin(spring_omega * t * dt +
                                                    2 * math.pi / n_sin_waves * j)
            for j in ti.static(range(n_objects)):
                offset = x[t, j] - x[t, head_id]
                # use a smaller weight since there are too many of them
                actuation += weights1[i, j * 6 + n_sin_waves] * offset[0] * 0.05
                actuation += weights1[i,
                                    j * 6 + n_sin_waves + 1] * offset[1] * 0.05
                actuation += weights1[i, j * 6 + n_sin_waves + 2] * v[t,
                                                                    j][0] * 0.05
                actuation += weights1[i, j * 6 + n_sin_waves + 3] * v[t,
                                                                    j][1] * 0.05
                actuation += weights1[i, j * 6 + n_sin_waves +
                                    4] * rotation[t, j] * 0.05
                actuation += weights1[i, j * 6 + n_sin_waves + 5] * omega[t,
                                                                        j] * 0.05

            actuation += weights1[i, n_objects * 6 + n_sin_waves] * goal[None][0]
            actuation += weights1[i,
                                n_objects * 6 + n_sin_waves + 1] * goal[None][1]
            actuation += bias1[i]
            actuation = ti.tanh(actuation)
            hidden[t, i] = actuation


    @ti.kernel
    def nn2(t: ti.i32):
        for i in range(n_springs):
            act = 0.0
            for j in ti.static(range(n_hidden)):
                act += weights2[i, j] * hidden[t, j]
            act += bias2[i]
            act = ti.tanh(act)
            actuation[t, i] = act


    @ti.func
    def rotation_matrix(r):
        return ti.Matrix([[ti.cos(r), -ti.sin(r)], [ti.sin(r), ti.cos(r)]])


    @ti.kernel
    def initialize_properties():
        for i in range(n_objects):
            inverse_mass[i] = 1.0 / (4 * halfsize[i][0] * halfsize[i][1])
            inverse_inertia[i] = 1.0 / (4 / 3 * halfsize[i][0] * halfsize[i][1] *
                                        (halfsize[i][0] * halfsize[i][0] +
                                        halfsize[i][1] * halfsize[i][1]))


    @ti.func
    def to_world(t, i, rela_x):
        rot = rotation[t, i]
        rot_matrix = rotation_matrix(rot)

        rela_pos = rot_matrix @ rela_x
        rela_v = omega[t, i] * ti.Vector([-rela_pos[1], rela_pos[0]])

        world_x = x[t, i] + rela_pos
        world_v = v[t, i] + rela_v

        return world_x, world_v, rela_pos


    @ti.func
    def apply_impulse(t, i, impulse, location, toi_input):
        # *********每行代码添加注释************
        delta_v = impulse * inverse_mass[i]
        delta_omega = (location - x[t, i]).cross(impulse) * inverse_inertia[i]

        toi = ti.min(ti.max(0.0, toi_input), dt)

        ti.atomic_add(x_inc[t + 1, i], toi * (-delta_v))
        ti.atomic_add(rotation_inc[t + 1, i], toi * (-delta_omega))

        ti.atomic_add(v_inc[t + 1, i], delta_v)
        ti.atomic_add(omega_inc[t + 1, i], delta_omega)


    @ti.kernel
    def collide(t: ti.i32):
        # *********每行代码添加注释************
        for i in range(n_objects):
            hs = halfsize[i]
            for k in ti.static(range(4)):
                # the corner for collision detection
                offset_scale = ti.Vector([k % 2 * 2 - 1, k // 2 % 2 * 2 - 1])

                corner_x, corner_v, rela_pos = to_world(t, i, offset_scale * hs)
                corner_v = corner_v + dt * gravity * ti.Vector([0.0, 1.0])

                # Apply impulse so that there's no sinking
                normal = ti.Vector([0.0, 1.0])
                tao = ti.Vector([1.0, 0.0])

                rn = rela_pos.cross(normal)
                rt = rela_pos.cross(tao)
                impulse_contribution = inverse_mass[i] + (rn) ** 2 * \
                                    inverse_inertia[i]
                timpulse_contribution = inverse_mass[i] + (rt) ** 2 * \
                                        inverse_inertia[i]

                rela_v_ground = normal.dot(corner_v)

                impulse = 0.0
                timpulse = 0.0
                new_corner_x = corner_x + dt * corner_v
                toi = 0.0
                if rela_v_ground < 0 and new_corner_x[1] < ground_height:
                    impulse = -(1 +
                                elasticity) * rela_v_ground / impulse_contribution
                    if impulse > 0:
                        # friction
                        timpulse = -corner_v.dot(tao) / timpulse_contribution
                        timpulse = ti.min(friction * impulse,
                                        ti.max(-friction * impulse, timpulse))
                        if corner_x[1] > ground_height:
                            toi = -(corner_x[1] - ground_height) / ti.min(
                                corner_v[1], -1e-3)

                apply_impulse(t, i, impulse * normal + timpulse * tao,
                            new_corner_x, toi)

                penalty = 0.0
                if new_corner_x[1] < ground_height:
                    # apply penalty
                    penalty = -dt * penalty * (
                        new_corner_x[1] - ground_height) / impulse_contribution

                apply_impulse(t, i, penalty * normal, new_corner_x, 0)


    @ti.kernel
    def apply_spring_force(t: ti.i32):
        # *********每行代码添加注释************
        for i in range(n_springs):
            a = spring_anchor_a[i]
            b = spring_anchor_b[i]
            pos_a, vel_a, rela_a = to_world(t, a, spring_offset_a[i])
            pos_b, vel_b, rela_b = to_world(t, b, spring_offset_b[i])
            dist = pos_a - pos_b
            length = dist.norm() + 1e-4

            act = actuation[t, i]

            is_joint = spring_length[i] == -1

            target_length = spring_length[i] * (1.0 + spring_actuation[i] * act)
            if is_joint:
                target_length = 0.0
            impulse = dt * (length -
                            target_length) * spring_stiffness[i] / length * dist

            if is_joint:
                rela_vel = vel_a - vel_b
                rela_vel_norm = rela_vel.norm() + 1e-1
                impulse_dir = rela_vel / rela_vel_norm
                impulse_contribution = inverse_mass[a] + \
                impulse_dir.cross(rela_a) ** 2 * inverse_inertia[
                                        a] + inverse_mass[b] + impulse_dir.cross(rela_b) ** 2 * \
                                    inverse_inertia[
                                        b]
                # project relative velocity
                impulse += rela_vel_norm / impulse_contribution * impulse_dir

            apply_impulse(t, a, -impulse, pos_a, 0.0)
            apply_impulse(t, b, impulse, pos_b, 0.0)


    @ti.kernel
    def advance_toi(t: ti.i32):
        # *********每行代码添加注释************
        for i in range(n_objects):
            s = math.exp(-dt * damping)
            v[t, i] = s * v[t - 1, i] + v_inc[t, i] + dt * gravity * ti.Vector(
                [0.0, 1.0])
            x[t, i] = x[t - 1, i] + dt * v[t, i] + x_inc[t, i]
            omega[t, i] = s * omega[t - 1, i] + omega_inc[t, i]
            rotation[t, i] = rotation[t - 1,
                                    i] + dt * omega[t, i] + rotation_inc[t, i]

    @ti.kernel
    def compute_loss(t: ti.i32):
        loss[None] = (x[t, head_id] - goal[None]).norm()


    gui = ti.GUI('Rigid Body Simulation', (512, 512), background_color=0xFFFFFF)


    def forward(output=None, visualize=True):
        initialize_properties()

        interval = vis_interval
        total_steps = steps
        if output:
            print(output)
            interval = output_vis_interval
            file = f'results/{output}'
            path = os.path.join(dir_path, file)
            os.makedirs(path, exist_ok=True)
            total_steps *= 2

        goal[None] = [0.9, 0.15]
        for t in range(1, total_steps):
            nn1(t - 1)
            nn2(t - 1)
            collide(t - 1)
            apply_spring_force(t - 1)
            advance_toi(t)


            if (t + 1) % interval == 0 and visualize:

                for i in range(n_objects):
                    points = []
                    for k in range(4):
                        offset_scale = [[-1, -1], [1, -1], [1, 1], [-1, 1]][k]
                        rot = rotation[t, i]
                        rot_matrix = np.array([[math.cos(rot), -math.sin(rot)],
                                            [math.sin(rot),
                                                math.cos(rot)]])

                        pos = np.array([x[t, i][0], x[t, i][1]
                                        ]) + offset_scale * rot_matrix @ np.array(
                                            [halfsize[i][0], halfsize[i][1]])

                        points.append((pos[0], pos[1]))

                    for k in range(4):
                        gui.line(points[k],
                                points[(k + 1) % 4],
                                color=0x0,
                                radius=2)

                for i in range(n_springs):

                    def get_world_loc(i, offset):
                        rot = rotation[t, i]
                        rot_matrix = np.array([[math.cos(rot), -math.sin(rot)],
                                            [math.sin(rot),
                                                math.cos(rot)]])
                        pos = np.array([[x[t, i][0]], [
                            x[t, i][1]
                        ]]) + rot_matrix @ np.array([[offset[0]], [offset[1]]])
                        return pos

                    pt1 = get_world_loc(spring_anchor_a[i], spring_offset_a[i])
                    pt2 = get_world_loc(spring_anchor_b[i], spring_offset_b[i])

                    color = 0xFF2233

                    if spring_actuation[i] != 0 and spring_length[i] != -1:
                        a = actuation[t - 1, i] * 0.5
                        color = ti.rgb_to_hex((0.5 + a, 0.5 - abs(a), 0.5 - a))

                    if spring_length[i] == -1:
                        gui.line(pt1, pt2, color=0x000000, radius=9)
                        gui.line(pt1, pt2, color=color, radius=7)
                    else:
                        gui.line(pt1, pt2, color=0x000000, radius=7)
                        gui.line(pt1, pt2, color=color, radius=5)

                gui.line((0.05, ground_height - 5e-3),
                        (0.95, ground_height - 5e-3),
                        color=0x0,
                        radius=5)

                path = None
                if output:
                    file = f'results/{output}/{t:04d}.png'
                    path = os.path.join(dir_path, file)
                if path:
                    img = gui.get_image()
                    img_u8 = (np.clip(img, 0, 1) * 255).astype(np.uint8)
                    img_u8 = cv2.rotate(img_u8, cv2.ROTATE_90_COUNTERCLOCKWISE)
                    _, buf = cv2.imencode('.png', img_u8)
                    with open(path, "wb") as f:
                        buf.tofile(f)  # 这个写法支持中文路径
                gui.show()

        loss[None] = 0
        compute_loss(steps - 1)


    @ti.kernel
    def clear_states():
        for t in range(0, max_steps):
            for i in range(0, n_objects):
                v_inc[t, i] = ti.Vector([0.0, 0.0])
                x_inc[t, i] = ti.Vector([0.0, 0.0])
                rotation_inc[t, i] = 0.0
                omega_inc[t, i] = 0.0


    def setup_robot(objects, springs, h_id):
        global head_id
        head_id = h_id
        global n_objects, n_springs
        n_objects = len(objects)
        n_springs = len(springs)
        allocate_fields()

        print('n_objects=', n_objects, '   n_springs=', n_springs)

        for i in range(n_objects):
            x[0, i] = objects[i][0]
            halfsize[i] = objects[i][1]
            rotation[0, i] = objects[i][2]

        for i in range(n_springs):
            s = springs[i]
            spring_anchor_a[i] = s[0]
            spring_anchor_b[i] = s[1]
            spring_offset_a[i] = s[2]
            spring_offset_b[i] = s[3]
            spring_length[i] = s[4]
            spring_stiffness[i] = s[5]
            if s[6]:
                spring_actuation[i] = s[6]
            else:
                spring_actuation[i] = default_actuation


    def optimize(visualize=True):
        for i in range(n_hidden):
            for j in range(n_input_states()):
                weights1[i, j] = np.random.randn() * math.sqrt(
                    2 / (n_hidden + n_input_states())) * 0.5

        for i in range(n_springs):
            for j in range(n_hidden):
                # TODO: n_springs should be n_actuators
                weights2[i, j] = np.random.randn() * math.sqrt(
                    2 / (n_hidden + n_springs)) * 1

        losses = []
        for iter in range(20):
            clear_states()

            with ti.ad.Tape(loss):
                forward(visualize=visualize)

            print('Iter=', iter, 'Loss=', loss[None])

            total_norm_sqr = 0
            for i in range(n_hidden):
                for j in range(n_input_states()):
                    total_norm_sqr += weights1.grad[i, j]**2
                total_norm_sqr += bias1.grad[i]**2

            for i in range(n_springs):
                for j in range(n_hidden):
                    total_norm_sqr += weights2.grad[i, j]**2
                total_norm_sqr += bias2.grad[i]**2

            print(total_norm_sqr)

            gradient_clip = 0.2
            scale = learning_rate * min(
                1.0, gradient_clip / (total_norm_sqr**0.5 + 1e-4))
            for i in range(n_hidden):
                for j in range(n_input_states()):
                    weights1[i, j] -= scale * weights1.grad[i, j]
                bias1[i] -= scale * bias1.grad[i]

            for i in range(n_springs):
                for j in range(n_hidden):
                    weights2[i, j] -= scale * weights2.grad[i, j]
                bias2[i] -= scale * bias2.grad[i]

            losses.append(loss[None])
        return losses

    def main():
        setup_robot(*robots[robot_id]())

        if cmd == 'plot':
            ret = {}
            for toi in [False, True]:
                ret[toi] = []
                for i in range(5):
                    losses = optimize(toi=toi, visualize=False)
                    ret[toi].append(losses)
            path = os.path.join(dir_path, 'losses.pkl')
            pickle.dump(ret, open(path, 'wb'))
            print(f"Losses saved to {path}")
        else:
            optimize(visualize=True)

        clear_states()
        forward('final{}'.format(robot_id), visualize=True)


    if __name__ == '__main__':
        dir_path = os.path.dirname(os.path.realpath(__file__))
        robot_id = 1 # robot_id=0, 1, 2
        cmd = 'train' # train/plot
        main()
    ```

??? remarks "robot_config.py 完整代码"

    ```py
    import math

    objects = []
    springs = []


    def add_object(x, halfsize, rotation=0):
        objects.append([x, halfsize, rotation])
        return len(objects) - 1


    # actuation 0.0 will be translated into default actuation
    def add_spring(a, b, offset_a, offset_b, length, stiffness, actuation=0.0):
        springs.append([a, b, offset_a, offset_b, length, stiffness, actuation])


    def robotA():
        add_object(x=[0.3, 0.25], halfsize=[0.15, 0.03])
        add_object(x=[0.2, 0.15], halfsize=[0.03, 0.02])
        add_object(x=[0.3, 0.15], halfsize=[0.03, 0.02])
        add_object(x=[0.4, 0.15], halfsize=[0.03, 0.02])
        add_object(x=[0.4, 0.3], halfsize=[0.005, 0.03])

        l = 0.12
        s = 15
        add_spring(0, 1, [-0.03, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 1, [-0.1, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 2, [-0.03, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 2, [0.03, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 3, [0.03, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 3, [0.1, 0.00], [0.0, 0.0], l, s)
        # -1 means the spring is a joint
        add_spring(0, 4, [0.1, 0], [0, -0.05], -1, s)

        return objects, springs, 0


    def robotC():
        add_object(x=[0.3, 0.25], halfsize=[0.15, 0.03])
        add_object(x=[0.2, 0.15], halfsize=[0.03, 0.02])
        add_object(x=[0.3, 0.15], halfsize=[0.03, 0.02])
        add_object(x=[0.4, 0.15], halfsize=[0.03, 0.02])

        l = 0.12
        s = 15
        add_spring(0, 1, [-0.03, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 1, [-0.1, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 2, [-0.03, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 2, [0.03, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 3, [0.03, 0.00], [0.0, 0.0], l, s)
        add_spring(0, 3, [0.1, 0.00], [0.0, 0.0], l, s)

        return objects, springs, 3


    l_thigh_init_ang = 10
    l_calf_init_ang = -10
    r_thigh_init_ang = 10
    r_calf_init_ang = -10
    initHeight = 0.15

    hip_pos = [0.3, 0.5 + initHeight]
    thigh_half_length = 0.11
    calf_half_length = 0.11

    foot_half_length = 0.08


    def rotAlong(half_length, deg, center):
        ang = math.radians(deg)
        return [
            half_length * math.sin(ang) + center[0],
            -half_length * math.cos(ang) + center[1]
        ]


    half_hip_length = 0.08


    def robotLeg():
        #hip
        add_object(hip_pos, halfsize=[0.06, half_hip_length])
        hip_end = [hip_pos[0], hip_pos[1] - (half_hip_length - 0.01)]

        #left
        l_thigh_center = rotAlong(thigh_half_length, l_thigh_init_ang, hip_end)
        l_thigh_end = rotAlong(thigh_half_length * 2.0, l_thigh_init_ang, hip_end)
        add_object(l_thigh_center,
                halfsize=[0.02, thigh_half_length],
                rotation=math.radians(l_thigh_init_ang))
        add_object(rotAlong(calf_half_length, l_calf_init_ang, l_thigh_end),
                halfsize=[0.02, calf_half_length],
                rotation=math.radians(l_calf_init_ang))
        l_calf_end = rotAlong(2.0 * calf_half_length, l_calf_init_ang, l_thigh_end)
        add_object([l_calf_end[0] + foot_half_length, l_calf_end[1]],
                halfsize=[foot_half_length, 0.02])

        #right
        add_object(rotAlong(thigh_half_length, r_thigh_init_ang, hip_end),
                halfsize=[0.02, thigh_half_length],
                rotation=math.radians(r_thigh_init_ang))
        r_thigh_end = rotAlong(thigh_half_length * 2.0, r_thigh_init_ang, hip_end)
        add_object(rotAlong(calf_half_length, r_calf_init_ang, r_thigh_end),
                halfsize=[0.02, calf_half_length],
                rotation=math.radians(r_calf_init_ang))
        r_calf_end = rotAlong(2.0 * calf_half_length, r_calf_init_ang, r_thigh_end)
        add_object([r_calf_end[0] + foot_half_length, r_calf_end[1]],
                halfsize=[foot_half_length, 0.02])

        s = 200

        thigh_relax = 0.9
        leg_relax = 0.9
        foot_relax = 0.7

        thigh_stiff = 5
        leg_stiff = 20
        foot_stiff = 40

        #left springs
        add_spring(0, 1, [0, (half_hip_length - 0.01) * 0.4],
                [0, -thigh_half_length],
                thigh_relax * (2.0 * thigh_half_length + 0.22), thigh_stiff)
        add_spring(1, 2, [0, thigh_half_length], [0, -thigh_half_length],
                leg_relax * 4.0 * thigh_half_length, leg_stiff, 0.08)
        add_spring(
            2, 3, [0, 0], [foot_half_length, 0],
            foot_relax *
            math.sqrt(pow(thigh_half_length, 2) + pow(2.0 * foot_half_length, 2)),
            foot_stiff)

        add_spring(0, 1, [0, -(half_hip_length - 0.01)], [0.0, thigh_half_length],
                -1, s)
        add_spring(1, 2, [0, -thigh_half_length], [0.0, thigh_half_length], -1, s)
        add_spring(2, 3, [0, -thigh_half_length], [-foot_half_length, 0], -1, s)

        #right springs
        add_spring(0, 4, [0, (half_hip_length - 0.01) * 0.4],
                [0, -thigh_half_length],
                thigh_relax * (2.0 * thigh_half_length + 0.22), thigh_stiff)
        add_spring(4, 5, [0, thigh_half_length], [0, -thigh_half_length],
                leg_relax * 4.0 * thigh_half_length, leg_stiff, 0.08)
        add_spring(
            5, 6, [0, 0], [foot_half_length, 0],
            foot_relax *
            math.sqrt(pow(thigh_half_length, 2) + pow(2.0 * foot_half_length, 2)),
            foot_stiff)

        add_spring(0, 4, [0, -(half_hip_length - 0.01)], [0.0, thigh_half_length],
                -1, s)
        add_spring(4, 5, [0, -thigh_half_length], [0.0, thigh_half_length], -1, s)
        add_spring(5, 6, [0, -thigh_half_length], [-foot_half_length, 0], -1, s)

        return objects, springs, 3


    def robotB():
        body = add_object([0.15, 0.25], [0.1, 0.03])
        back = add_object([0.08, 0.22], [0.03, 0.10])
        front = add_object([0.22, 0.22], [0.03, 0.10])

        rest_length = 0.22
        stiffness = 50
        act = 0.03
        add_spring(body,
                back, [0.08, 0.02], [0.0, -0.08],
                rest_length,
                stiffness,
                actuation=act)
        add_spring(body,
                front, [-0.08, 0.02], [0.0, -0.08],
                rest_length,
                stiffness,
                actuation=act)

        add_spring(body, back, [-0.08, 0.0], [0.0, 0.03], -1, stiffness)
        add_spring(body, front, [0.08, 0.0], [0.0, 0.03], -1, stiffness)

        return objects, springs, body


    robots = [robotA, robotB, robotLeg]
    ```
