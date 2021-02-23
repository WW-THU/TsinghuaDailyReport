# 清华日报与紫荆码填报

当前填报情况： [![Daily Report](../../actions/workflows/daily.yml/badge.svg?event=schedule)](../../actions/workflows/daily.yml)
[![Zijing Code Report](../../actions/workflows/zijing_code.yml/badge.svg?event=schedule)](../../actions/workflows/zijing_code.yml)

---

## 简介

**学生每日健康和出行情况报告** + **紫荆码体温** 自动填报脚本。

整合自以下项目：

> [xmk2222/TsinghuaDailyReport](https://github.com/xmk2222/TsinghuaDailyReport)
>
> [Konano/report_temp.py](https://gist.github.com/Konano/b1576acfe61e0fdf2b3b60ab535ef6ae)

## 使用方式

建议使用第二种方式，简单易行.

### a. 计划任务

- pip install -r requirements.txt
- 配置 conf.ini 输入清华 info 用户名与密码
- python report.py
- python report_zijing_code.py
- 创建定时任务 Windows/Linux
  > [Windows 创建定时任务](https://www.cnblogs.com/wensiyang0916/p/5773828.html)

### b. GitHub Actions

> 如果你没有服务器，或者自己电脑也不能保证都开启，那么使用 Github Actions 可以作为你的服务器，并且非常安全。

- 创建 GitHub 账户
- fork 该仓库到你的项目，下面都是设置你的项目（注意 fork 的仓库的 GitHub Actions 是默认禁用的，需要手动打开）
- 设置 -> Secrets-> 添加 USER_NAME 与 USER_PASS 为你 Info 的用户名与密码
  ![添加Secrets](results/c.png)
- 进入 Actions 点击 Understand

OK!

说明:
Github Actions 的配置文件 (`.github/workflows` 下的 `daily.yml` 和 `zijing_code.yml`) 中分别配置了日报和紫荆码的填报时间。

## 效果

- ![效果图1](results/a.png)
- ![效果图2](results/b.png)
- 假装这里还有个紫荆码的效果图...
