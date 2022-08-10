from django.db import models

class Members(models.Model):
    USNR = 'USNR'
    USMCR = 'USMCR'
    USN = 'USN'
    USMC = 'USMC'
    MIDN = 'Midshipman'
    OC = 'Officer Candidate'
    LT = 'LT'
    LCDR = 'LCDR'
    CDR = 'CDR'
    CAPT = 'CAPT'
    Capt = 'Capt'
    Maj = 'Maj'
    LtCol = 'LtCol'
    Col = 'Col'
    Yes = 'Yes'
    No = 'No'

    YESNO = [
        (Yes, 'Yes'),
        (No, 'No')
    ]

    STUDENT_RANKS = [
        (MIDN, 'Midshipman'),
        (OC, 'Officer Candidate')
    ]

    RANKS = [
        (LT, 'LT'),
        (LCDR, 'LCDR'),
        (CDR, 'CDR'),
        (CAPT, 'CAPT'),
        (Capt, 'Capt'),
        (Maj, 'Major'),
        (LtCol, 'LtCol'),
        (Col, 'Col')
    ]
    SERVICE = [
        (USNR, 'USNR'),
        (USMCR, 'USMCR'),
        (USN, 'USN'),
        (USMC, 'USMC')
    ]   

    student_name = models.CharField(max_length=50, default='student_name')
    student_rank = models.CharField(max_length=20, choices=STUDENT_RANKS)
    student_service = models.CharField(max_length=5, choices=SERVICE, default=USNR)

    senior_name = models.CharField(max_length=50, default='senior_name')
    senior_rank = models.CharField(max_length=20, choices=RANKS)
    senior_service = models.CharField(max_length=5, choices=SERVICE, default=USN)

    member1_name = models.CharField(max_length=50, default='member1_name')
    member1_rank = models.CharField(max_length=20, choices=RANKS)
    member1_service = models.CharField(max_length=5, choices=SERVICE, default=USN)

    member2_name = models.CharField(max_length=50, default='member2_name')
    member2_rank = models.CharField(max_length=20, choices=RANKS)
    member2_service = models.CharField(max_length=5, choices=SERVICE, default=USN)

    recorder_name = models.CharField(max_length=50, default='recorder_name')
    recorder_rank  = models.CharField(max_length=20, choices=RANKS)
    recorder_service  = models.CharField(max_length=5, choices=SERVICE, default=USN)

    CO_name = models.CharField(max_length=50, default='CO_name')

    origin_code = models.CharField(max_length=5, default='origin_code')
    serial_num = models.CharField(max_length=5, default='serial_num')
    letter_date = models.CharField(max_length=8, default = 'letter_date')

    #prb convening order
    unit = models.CharField(max_length=50, default='unit')
    trigger = models.CharField(max_length=50, default='trigger')
    prb_time = models.CharField(max_length=4, default='prb_time')
    prb_date = models.CharField(max_length=8, default='prb_date')
    prb_location = models.CharField(max_length=25, default='prb_location')
    student_uniform = models.CharField(max_length=25, default='student_uniform')
    student_on_LOA = models.CharField(max_length=5, choices=YESNO, default='No')

    #prb report
    present = models.CharField(max_length=5, choices=YESNO, default='No')
    university = models.CharField(max_length=50, default='university')
    major = models.CharField(max_length=50, default='major')
    gpa = models.CharField(max_length=4, default='gpa')
    credits = models.CharField(max_length=3, default='credits')
    aptitude = models.CharField(max_length=4, default='aptittude')
    academic_history = models.CharField(max_length=200, default='academic_history')
    disciplinary_history = models.CharField(max_length=200, default='disciplinary_history')
    performance_history = models.CharField(max_length=200, default='performance_history')
    board_findings = models.CharField(max_length=200, default='board_findings')
    board_rec = models.CharField(max_length=200, default='board_rec')
    
    def __str__(self):
        return f'{self.student_name}, {self.senior_name}, {self.member1_name}, {self.member2_name}, {self.recorder_name}'