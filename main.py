import tkinter as tk
from datetime import datetime, timedelta

class WorkTimerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("퇴근 시간 카운트다운 ⏳")
        self.master.geometry("400x250")
        self.master.configure(bg="#f0f0f5")

        # 스타일 정의
        self.bg_color = "#f0f0f5"
        self.primary_color = "#2e86de"
        self.font = ("Helvetica", 12)

        # 라벨
        self.title_label = tk.Label(master, text="출근 시간을 입력하세요", bg=self.bg_color, font=("Helvetica", 14, "bold"))
        self.title_label.pack(pady=(20, 10))

        # 입력창
        self.start_entry = tk.Entry(master, font=self.font, justify="center", width=10, bd=2, relief="groove")
        self.start_entry.insert(0, "09:00")
        self.start_entry.pack(pady=5)

        # 버튼
        self.start_button = tk.Button(master, text="⏱ 시작", bg=self.primary_color, fg="white",
                                      font=self.font, command=self.start_timer,
                                      width=15, relief="flat", padx=10, pady=5)
        self.start_button.pack(pady=10)

        # 결과 표시
        self.countdown_label = tk.Label(master, text="", bg=self.bg_color, font=("Helvetica", 18, "bold"), fg="#333")
        self.countdown_label.pack(pady=20)

        self.leave_time = None
        self.running = False

    def start_timer(self):
        user_input = self.start_entry.get()
        try:
            start_time = datetime.strptime(user_input, "%H:%M")
            now = datetime.now()
            self.leave_time = datetime.combine(now.date(), start_time.time()) + timedelta(hours=9)
            self.running = True
            self.update_countdown()
        except ValueError:
            self.countdown_label.config(text="❌ 형식: HH:MM")

    def update_countdown(self):
        if not self.running:
            return

        now = datetime.now()

        if now >= self.leave_time:
            self.countdown_label.config(text="퇴근했습니다 🎉")
            self.running = False
        else:
            remaining = self.leave_time - now
            hours, remainder = divmod(remaining.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.countdown_label.config(
                text=f"남은 시간: {hours:02d}:{minutes:02d}:{seconds:02d}"
            )
            self.master.after(1000, self.update_countdown)

if __name__ == "__main__":
    root = tk.Tk()
    app = WorkTimerApp(root)
    root.mainloop()
