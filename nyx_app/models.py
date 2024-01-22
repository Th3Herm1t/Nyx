from django.db import models

# mbti_app/models.py


class UserInput(models.Model):
    text = models.TextField()
    predicted_mbti = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.text} - {self.predicted_mbti}"

class Feedback(models.Model):
    user_input = models.ForeignKey(UserInput, on_delete=models.CASCADE, null=True)
    feedback_text = models.TextField()
