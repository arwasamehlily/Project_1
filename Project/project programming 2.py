from datetime import datetime

# SRP: كلاس Task مسؤوليته الوحيدة هي إدارة تفاصيل المهام وتحديث حالتها

class Task:
    """Class for adding and updating task status"""
    def __init__(self, title, priority="Medium"):
        self.title = title
        self.completed = False
        self.priority = priority
        self.created_at = datetime.now()

    def update_status(self, status):
        """Update task status"""
        self.completed = status


# SRP: كلاس Reminder مسؤوليته الوحيدة هي إرسال التذكيرات

class Reminder:
    """Class for sending reminders"""
    def __init__(self, reminder_type):
        self.reminder_type = reminder_type  # نوع التذكير (SMS أو Email)

    def send_reminder(self, task):
        """Send a reminder for the task"""
        print(f"Reminder sent for task: {task.title} via {self.reminder_type}")


# OCP: كلاس PriorityTask بيضيف ميزة الأولوية بدون ما نغير الكود اللي في كلاس Task

class PriorityTask(Task):
    """Class for setting task priorities"""
    def __init__(self, title, priority="High"):
        super().__init__(title, priority)


# OCP: كلاس RecurringTask بيضيف ميزة التكرار بدون ما نغير الكود اللي في كلاس Task

class RecurringTask(Task):
    """Class for recurring tasks"""
    def __init__(self, title, recurrence):
        super().__init__(title)
        self.recurrence = recurrence
        
        
        

