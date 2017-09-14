from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    POS_CHOICES = [
        ('', ''), ('S', '舉球'), ('WS', '大砲/攻擊手'),
        ('MB', '攔中'), ('O', '輔舉'), ('L', '自由')
    ]
    pos = models.CharField(
        max_length=2,   
        choices=POS_CHOICES,
        default=POS_CHOICES[0],
    )
    MG_POS_CHOICES = [
        ('player', '球員'), ('leader', '隊長'),
        ('vice leader', '副隊長'), ('financial', '總務'), 
        ('manager_m', '男排球經'), ('manager_w', '女排球經')
    ]
    mg_pos = models.CharField(
        max_length=20,
        choices=MG_POS_CHOICES,
        default=MG_POS_CHOICES[0],
    )
    photo = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    # Bachelor = [('B1', '資管一'), ('B2', '資管二'), ('B3', '資管三'), ('B4', '資管四')]
    # Master = [('M1', '資管所碩一'), ('M2', '資管所碩二')]
    # PhD = [
    #     ('P1', '資管所博一'), ('P2', '資管所博二'), ('P3', '資管所博三')
    #     ('P4', '資管所博四'), ('P5', '資管所博五'), ('P6', '資管所博六'), ('P7', '資管所博七')
    # ]
    # Graduated = [('G', '已畢業')]
    # GRADE_CHOICES = []
    # for db_value, web_show in Bachelor, Master, PhD, Graduated:
    #   GRADE_CHOICES.append((db_value, web_show))
    # grade_in_school = models.CharField(
    #     max_length=5,
    #     choices=GRADE_CHOICES,
    #     default=Bachelor[0],
    # )

    def __str__(self):
        return self.name