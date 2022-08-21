from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, ButtonHolder
      
class StudentForm(forms.Form):
    USNR = 'USNR'
    USMCR = 'USMCR'
    USN = 'USN'
    USMC = 'USMC'
    MIDN = 'Midshipman'
    OC = 'Officer Candidate'

    STUDENT_RANKS = [
        (MIDN, 'Midshipman'),
        (OC, 'Officer Candidate')
    ]

    SERVICE = [
        (USN, 'USN'),
        (USMC, 'USMC'),
        (USNR, 'USNR'),
        (USMCR, 'USMCR')
    ] 

    student_name = forms.CharField(
        label='Student',
        max_length=50,
        widget=forms.TextInput({'class':'text-end'}),
        required=True,
        help_text='First M. Last'
        )
    student_rank  = forms.ChoiceField(
        label=False, choices=STUDENT_RANKS)
    student_service  = forms.ChoiceField(label=False, choices=SERVICE)

class SeniorForm(forms.Form):
    USN = 'USN'
    USMC = 'USMC'
    LT = 'LT'
    LCDR = 'LCDR'
    CDR = 'CDR'
    CAPT = 'CAPT'
    Capt = 'Capt'
    Maj = 'Maj'
    LtCol = 'LtCol'
    Col = 'Col'

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
        (USN, 'USN'),
        (USMC, 'USMC'),
    ] 
    
    senior_name = forms.CharField(
        label='Senior Member',
        max_length=50,
        widget=forms.TextInput({'class':'text-end' }),
        required=True,
        help_text='First M. Last'
        )
    senior_rank  = forms.ChoiceField(label=False, choices=RANKS)
    senior_service  = forms.ChoiceField(label=False, choices=SERVICE)

class MemberOneForm(forms.Form):
    USN = 'USN'
    USMC = 'USMC'
    LT = 'LT'
    LCDR = 'LCDR'
    CDR = 'CDR'
    CAPT = 'CAPT'
    Capt = 'Capt'
    Maj = 'Maj'
    LtCol = 'LtCol'
    Col = 'Col'

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
        (USN, 'USN'),
        (USMC, 'USMC'),
    ] 

    member1_name = forms.CharField(
        label='Member One',
        max_length=50,
        widget=forms.TextInput({'class':'text-end' }),
        required=True,
        help_text='First M. Last'
        )
    member1_rank  = forms.ChoiceField(label=False, choices=RANKS)
    member1_service  = forms.ChoiceField(label=False, choices=SERVICE)

class MemberTwoForm(forms.Form):
    USN = 'USN'
    USMC = 'USMC'
    LT = 'LT'
    LCDR = 'LCDR'
    CDR = 'CDR'
    CAPT = 'CAPT'
    Capt = 'Capt'
    Maj = 'Maj'
    LtCol = 'LtCol'
    Col = 'Col'

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
        (USN, 'USN'),
        (USMC, 'USMC'),
    ] 

    member2_name = forms.CharField(
        label='Member Two',
        max_length=50,
        widget=forms.TextInput({'class':'text-end' }),
        required=True,
        help_text='First M. Last'
        )
    member2_rank  = forms.ChoiceField(label=False, choices=RANKS)
    member2_service  = forms.ChoiceField(label=False, choices=SERVICE)

class RecorderForm(forms.Form):
    USN = 'USN'
    USMC = 'USMC'
    LT = 'LT'
    LCDR = 'LCDR'
    CDR = 'CDR'
    CAPT = 'CAPT'
    Capt = 'Capt'
    Maj = 'Maj'
    LtCol = 'LtCol'
    Col = 'Col'

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
        (USN, 'USN'),
        (USMC, 'USMC'),
    ] 

    recorder_name = forms.CharField(
        label='Recorder',
        max_length=50,
        widget=forms.TextInput({'class':'text-end' }),
        required=True,
        help_text='First M. Last'
        )
    recorder_rank  = forms.ChoiceField(label=False, choices=RANKS)
    recorder_service  = forms.ChoiceField(label=False, choices=SERVICE)

class PRBConvOrderForm(RecorderForm, MemberTwoForm, MemberOneForm, SeniorForm, StudentForm):
    Yes = 'Yes'
    No = 'No'

    YESNO = [
        (No, 'No'),
        (Yes, 'Yes')
    ]

    CO_name = forms.CharField(
        label='CO Name',
        max_length=50,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='F. M. LAST'
        )

    origin_code = forms.CharField(
        label='Origin Code', 
        max_length=6, 
        widget=forms.TextInput({'class':'text-center', 'size':21}), 
        required=True,
        help_text='ex: 00'
        )
    serial_num = forms.CharField(
        label='Serial Number',
        max_length=6,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: 148'
        )
    letter_date = forms.CharField(
        label = 'Letter Date',
        max_length=8,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='DDMONYY'
        )
    unit = forms.CharField(
        label = 'Unit Name',
        max_length=25,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: NROTCU Carnegie Mellon University'
        )
    trigger = forms.CharField(
        label = 'Trigger Reason',
        max_length=100,
        widget=forms.Textarea({"placeholder": '"A performance review board (PRB) shall be convened to investigate and make recommendations on your  _________"\n\nexample:\nfailure to pass a program required course', 'class':'text-center'}),
        required=True,
        help_text='Fill in the blank. Do not use a period at the end.'
        )
    prb_time = forms.CharField(
        label = 'PRB Time',
        max_length=4,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: 1330'
        )
    prb_date = forms.CharField(
        label = 'PRB Date',
        max_length=8,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='DDMMYY'
        )
    prb_location = forms.CharField(
        label = 'PRB Location',
        max_length=50,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: conference room (do not use a period)'
        )
    student_uniform = forms.CharField(
        label = 'Student Uniform',
        max_length=25,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: Service Dress Blues'
        )

    student_on_LOA  = forms.ChoiceField(
        label = 'Student will go on LOA?',
        choices=YESNO,
        required=True
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form_PRB_conv_order'
        self.helper.form_method = 'post'
        self.helper.form_action = 'download'
        self.helper.form_show_errors = False 
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('student_name', css_class='row mb-2'),
                    Div('student_rank', css_class='row mb-2'),
                    Div('student_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                Div(
                    Div('senior_name', css_class='row mb-2'),
                    Div('senior_rank', css_class='row mb-2'),
                    Div('senior_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                Div(
                    Div('member1_name', css_class='row mb-2'),
                    Div('member1_rank', css_class='row mb-2'),
                    Div('member1_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                Div(
                    
                    Div('member2_name', css_class='row mb-2'),
                    Div('member2_rank', css_class='row mb-2'),
                    Div('member2_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                Div(
                    Div('recorder_name', css_class='row mb-2'),
                    Div('recorder_rank', css_class='row mb-2'),
                    Div('recorder_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                css_class = 'row m-3 text-end',
            ),

            Div(
                Div(
                    Div('prb_time', css_class='col mb-2 mt-4'),
                    Div('prb_date', css_class='col mb-2'),
                    Div('prb_location', css_class='col mb-2'),
                    Div('student_uniform', css_class='col mb-2'),
                    Div('student_on_LOA', css_class='col mb-2'),
                    css_class = 'col m-1 text-end form-control'
                ),
                Div(
                    Div('origin_code', css_class='col mb-2 mt-4'),
                    Div('serial_num', css_class='col mb-2'),
                    Div('letter_date', css_class='col mb-2'),
                    Div('unit', css_class='col mb-2'),
                    Div('CO_name', css_class='col mb-2'),
                    css_class = 'col m-1 text-end form-control' 
                ),
                Div(
                    Div('trigger', css_class='col  mb-2'),
                    css_class = 'col m-1 text-center form-control' 
                ),
                css_class = 'row m-3'
            ),

            ButtonHolder(
                Div(css_class='col'),
                Submit('submit', 'Generate', css_class='col btn-outline-primary btn-lg justify-content-md-center'),
                Div(css_class='col'),
                css_class = 'row'
            )
        )

class PRBReportForm(PRBConvOrderForm):
    Yes = ''
    No = ''

    PRESENT = [
        (Yes, 'Yes'),
        (No, 'No')
    ]

    present  = forms.ChoiceField(
        label = 'Was the student present?',
        choices=PRESENT,
        required=True
        )

    college = forms.CharField(
        label='Studen\'s University',
        max_length=50,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: Carnegie Mellon University'
        )

    major = forms.CharField(
        label='Major', 
        max_length=25, 
        widget=forms.TextInput({'class':'text-center', 'size':21}), 
        required=True,
        help_text='ex: Mechanical Engineering'
        )

    gpa = forms.CharField(
        label='GPA',
        max_length=4,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: 2.75'
        )

    credits = forms.CharField(
        label = 'Credits',
        max_length=3,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: 57'
        )

    aptitude = forms.CharField(
        label = 'Military Aptitude',
        max_length=4,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: 3.05'
        )

    academic_history = forms.CharField(
        label = 'Academic History',
        max_length=500,
        widget=forms.Textarea({"placeholder": '"A performance review board (PRB) shall be convened to investigate and make recommendations on your  _________"\n\nexample:\nfailure to pass a program required course', 'class':'text-center'}),
        required=True,
        help_text='Brief academic history description. Do not use a period at the end.'
        )

    disciplinary_problems = forms.CharField(
        label = 'Disciplinary History',
        max_length=4,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='Brief disciplinary history description. Do not use a period at the end.'
        )

    performance_history = forms.CharField(
        label = 'Performance History',
        max_length=8,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='Brief performance history description. Do not use a period at the end.'
        )

    board_findings = forms.CharField(
        label = 'Board Findings',
        max_length=50,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: conference room (do not use a period)'
        )

    board_rec = forms.CharField(
        label = 'Board Recommendation',
        max_length=25,
        widget=forms.TextInput({'class':'text-center', 'size':21}),
        required=True,
        help_text='ex: Service Dress Blues'
        )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form_PRB_report'
        self.helper.form_method = 'post'
        self.helper.form_action = 'download'
        self.helper.form_show_errors = False 
        self.helper.layout = Layout(
            Div(
                Div(
                    Div('student_name', css_class='row mb-2'),
                    Div('student_rank', css_class='row mb-2'),
                    Div('student_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                Div(
                    Div('senior_name', css_class='row mb-2'),
                    Div('senior_rank', css_class='row mb-2'),
                    Div('senior_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                Div(
                    Div('member1_name', css_class='row mb-2'),
                    Div('member1_rank', css_class='row mb-2'),
                    Div('member1_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                Div(
                    
                    Div('member2_name', css_class='row mb-2'),
                    Div('member2_rank', css_class='row mb-2'),
                    Div('member2_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                Div(
                    Div('recorder_name', css_class='row mb-2'),
                    Div('recorder_rank', css_class='row mb-2'),
                    Div('recorder_service', css_class='row mb-2'),
                    css_class = 'col form-control m-1',
                ),
                css_class = 'row m-3 text-end',
            ),

            Div(
                Div(
    
                    Div('college', css_class='col mt-4'),
                    Div('major', css_class='col mb-2'),
                    Div('gpa', css_class='col mb-2'),
                    Div('credits', css_class='col mb-2'),
                    Div('aptitude', css_class='col mb-2'),
                    Div('present', css_class='col mb-2'),
                    css_class = 'col m-1 text-end form-control'
                ),
                Div(
                    Div('prb_time', css_class='col mb-2 mt-4'),
                    Div('prb_date', css_class='col mb-2'),
                    Div('prb_location', css_class='col mb-2'),
                    Div('origin_code', css_class='col mb-2 mt-4'),
                    Div('serial_num', css_class='col mb-2'),
                    Div('letter_date', css_class='col mb-2'),
                    Div('unit', css_class='col mb-2'),
                    css_class = 'col m-1 text-end form-control' 
                ),
                Div(
                    Div('academic_history', css_class='col  mb-2'),
                    Div('disciplinary_problems', css_class='col  mb-2'),
                    Div('performance_history', css_class='col  mb-2'),
                    Div('board_findings', css_class='col  mb-2'),
                    Div('board_rec', css_class='col  mb-2'),
                    css_class = 'col m-1 text-center form-control' 
                ),
                css_class = 'row m-3'
            ),

            ButtonHolder(
                Div(css_class='col'),
                Submit('submit', 'Generate', css_class='col btn-outline-primary btn-lg justify-content-md-center'),
                Div(css_class='col'),
                css_class = 'row'
            )
        )
    
    